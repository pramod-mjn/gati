# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 05:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neptype', '0003_englishtext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='englishtext',
            old_name='text',
            new_name='typing_text',
        ),
    ]
