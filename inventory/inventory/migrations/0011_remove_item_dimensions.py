# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20160803_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='dimensions',
        ),
    ]