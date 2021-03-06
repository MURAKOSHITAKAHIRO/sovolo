from django.shortcuts import redirect
from social_core.pipeline.partial import partial
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import uuid
import urllib
import random
import string

from .models import User

@partial
def get_profile_image(strategy, details, response,
                      user=None, is_new=False, *args, **kwargs):
    backend = kwargs.get('backend')
    if is_new:
        if backend.name == 'facebook':
            url = "http://graph.facebook.com/%(id)s/picture?type=large" % {
                'id': response['id'],
            }
        elif backend.name == 'twitter':
            url = response.get('profile_image_url', '').replace('_normal', '')
        if url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib.request.urlopen(url).read())
            img_temp.flush()

            user.image.save(str(uuid.uuid4()), File(img_temp))
            pass


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    # backend = kwargs.get('backend')
    if user and user.email:
        # The user we're logging in already has their email attribute set
        return

    if is_new:
        # quick fix: check if username is registered, add random string if so
        # todo: rethink about username uniqueness
        # todo: only check when form is posted (token cache will be reloaded, this will run twice)
        if details.get('username'):
            existingUser = User.objects.filter(username=details.get('username'))
            if existingUser.exists():
                randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
                details['username'] = details['username'] + randomString

    if is_new and not details.get('email'):
        # If we're creating a new user, and we can't find the email in the
        # details.  we'll attempt to request it from the data returned from our
        # backend strategy
        userEmail = strategy.request_data().get('email')
        if userEmail:
            # first check if email exists
            findUser = User.objects.filter(email=userEmail)
            if findUser.exists():
                current_partial = kwargs.get('current_partial')
                return strategy.redirect('/user/email_required?partial_token={0}&emailexists=1'.format(current_partial.token))
            else:
                details['email'] = userEmail

        else:
            # If there's no email information to be had, we need to ask the
            # user to fill it in.  This should redirect us to a view
            current_partial = kwargs.get('current_partial')
            return strategy.redirect('/user/email_required?partial_token={0}'.format(current_partial.token))
