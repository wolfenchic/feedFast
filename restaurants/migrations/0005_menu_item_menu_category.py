# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180327_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='menu_category',
            field=models.IntegerField(choices=[(1, 'Starter'), (2, 'Main'), (3, 'Dessert'), (4, 'Drinks')], default=1),
        ),
    ]
