# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 01:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0009_auto_20171203_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 1, 10, 29, 90999), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 1, 10, 29, 90973), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='due',
            field=models.CharField(default=datetime.datetime(2017, 12, 4, 1, 10, 29, 90747), max_length=20),
        ),
    ]
