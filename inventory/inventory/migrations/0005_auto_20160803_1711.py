# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20160803_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_listed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
