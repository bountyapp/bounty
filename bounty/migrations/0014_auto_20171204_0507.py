# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 05:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0013_auto_20171204_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 5, 7, 12, 53734), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 5, 7, 12, 53660), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='due',
            field=models.CharField(default=datetime.datetime(2017, 12, 4, 5, 7, 12, 53886), max_length=20),
        ),
    ]
