# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 00:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepserver', '0004_auto_20180405_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='end_date',
            field=models.DateField(verbose_name=datetime.date(2018, 4, 5)),
        ),
        migrations.AlterField(
            model_name='streak',
            name='start_date',
            field=models.DateField(verbose_name=datetime.date(2018, 4, 5)),
        ),
    ]
