from django import template
from django.template import Node, Variable

import sys

register = template.Library()


@register.inclusion_tag('event/event_list.html')
def event_list(events, user):
    return {'events': events, 'user': user}

@register.inclusion_tag('event/user_list.html')
def user_list(users, title, event):
    return {'users': users, 'title': title, 'event':event}

@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for key, value in kwargs.items():
        updated[key] = value
    return updated.urlencode()

@register.inclusion_tag('event/comments.html', takes_context=True)
def comments(context, event):
    comment_list = event.comment_set.order_by('created')
    return {'comment_list': comment_list, 'request': context['request'], 'event': event}