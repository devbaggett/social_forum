# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180817_0120'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([]),
        ),
    ]
