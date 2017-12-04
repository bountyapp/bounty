# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 23:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(default='-', max_length=20)),
                ('deliver', models.CharField(default='-', max_length=20)),
                ('contents', models.CharField(default='-', max_length=200)),
                ('places', models.CharField(default='-', max_length=200)),
                ('destination', models.CharField(default='-', max_length=200)),
                ('due', models.CharField(default=datetime.datetime(2017, 11, 30, 23, 47, 8, 815826), max_length=20)),
                ('cost', models.FloatField(default=0, max_length=20)),
                ('reward', models.FloatField(default=0, max_length=20)),
                ('total', models.FloatField(default=0, max_length=20)),
                ('comments', models.CharField(default='-', max_length=100)),
                ('status', models.CharField(default='waiting', max_length=100)),
                ('confirm_cus', models.BooleanField(default=False)),
                ('confirm_del', models.BooleanField(default=False)),
                ('review_cus', models.CharField(default='-', max_length=200)),
                ('review_del', models.CharField(default='-', max_length=200)),
                ('score_cus', models.IntegerField(default=0)),
                ('score_del', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2017, 11, 30, 23, 47, 8, 816069), max_length=20)),
            ],
        ),
    ]
