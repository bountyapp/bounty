# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 21:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0008_auto_20171202_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 3, 21, 16, 28, 141308), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 3, 21, 16, 28, 141283), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='due',
            field=models.CharField(default=datetime.datetime(2017, 12, 3, 21, 16, 28, 141053), max_length=20),
        ),
    ]
