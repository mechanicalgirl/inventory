# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20160803_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spoonfloweritem',
            name='design_height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='In inches', max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='spoonfloweritem',
            name='design_width',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='In inches', max_digits=15, null=True),
        ),
    ]