# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0012_auto_20160803_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Number of individual units used in item')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
            options={
                'verbose_name': 'Item Supplies',
                'verbose_name_plural': 'Supplies Per Item',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, help_text='Cost per unit', max_digits=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('maker_name', models.CharField(blank=True, max_length=50, null=True)),
                ('seller_name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='itemsupply',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Supply'),
        ),
    ]
