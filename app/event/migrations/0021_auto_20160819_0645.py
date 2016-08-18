# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_auto_20160819_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='region',
            field=models.CharField(choices=[('Kyoto', '京都府'), ('Wakayama', '和歌山県'), ('Ehime', '愛媛県'), ('Yamagata', '山形県'), ('Okinawa', '沖縄県'), ('Tokushima', '徳島県'), ('Tokyo', '東京都'), ('Miyagi', '宮城県'), ('Nagano', '長野県'), ('Chiba', '千葉県'), ('Kanagawa', '神奈川県'), ('Nara', '奈良県'), ('Kumamoto', '熊本県'), ('Tochigi', '栃木県'), ('Miyazaki', '宮崎県'), ('Ibaraki', '茨城県'), ('Gifu', '岐阜県'), ('Fukuoka', '福岡県'), ('Osaka', '大阪府'), ('Iwate', '岩手県'), ('Okayama', '岡山県'), ('Shiga', '滋賀県'), ('Ooita', '大分県'), ('Hiroshima', '広島県'), ('Aomori', '青森県'), ('Toyama', '富山県'), ('Gunnma', '群馬県'), ('Mie', '三重県'), ('Kouchi', '高知県'), ('Kagoshima', '鹿児島県'), ('Niigata', '新潟県'), ('Ishikawa', '石川県'), ('Yamanashi', '山梨県'), ('Yamaguchi', '山口県'), ('Nagasaki', '長崎県'), ('Hokkaido', '北海道'), ('Fukui', '福井県'), ('Fukushima', '福島県'), ('Kagawa', '香川県'), ('Shizuoka', '静岡県'), ('Saitama', '埼玉県'), ('Akita', '秋田県'), ('Aichi', '愛知県'), ('Saga', '佐賀県'), ('Hyogo', '兵庫県'), ('Tottori', '鳥取県'), ('Shimane', '島根県')], max_length=10),
        ),
    ]
