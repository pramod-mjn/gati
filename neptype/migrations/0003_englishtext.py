# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neptype', '0002_auto_20160609_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Englishtext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]
