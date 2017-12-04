# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0012_auto_20171204_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='canceled_reason_cus',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='quest',
            name='canceled_reason_del',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='quest',
            name='complete_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 4, 47, 17, 83603), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 4, 47, 17, 83557), max_length=20),
        ),
        migrations.AlterField(
            model_name='quest',
            name='due',
            field=models.CharField(default=datetime.datetime(2017, 12, 4, 4, 47, 17, 83746), max_length=20),
        ),
    ]
