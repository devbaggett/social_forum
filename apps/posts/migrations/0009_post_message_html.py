# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20180817_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message_html',
            field=models.TextField(default=9, editable=False),
            preserve_default=False,
        ),
    ]
