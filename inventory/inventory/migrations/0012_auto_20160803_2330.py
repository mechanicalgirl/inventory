# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 23:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_remove_item_dimensions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etsyitem',
            options={'verbose_name': 'Etsy Data', 'verbose_name_plural': 'Etsy Data'},
        ),
        migrations.AlterModelOptions(
            name='spoonfloweritem',
            options={'verbose_name': 'Spoonflower Data', 'verbose_name_plural': 'Spoonflower Data'},
        ),
    ]
