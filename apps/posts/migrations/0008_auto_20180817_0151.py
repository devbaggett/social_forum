# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180817_0150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='post',
            name='message_html',
        ),
    ]
