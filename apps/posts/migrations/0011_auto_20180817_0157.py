# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20180817_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message_html',
            field=models.TextField(editable=False),
        ),
    ]