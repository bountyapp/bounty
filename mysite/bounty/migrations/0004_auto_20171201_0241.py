# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 02:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0003_auto_20171201_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 2, 41, 44, 660470), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='due',
            field=models.CharField(default=datetime.datetime(2017, 12, 1, 2, 41, 44, 660228), max_length=20),
        ),
    ]
