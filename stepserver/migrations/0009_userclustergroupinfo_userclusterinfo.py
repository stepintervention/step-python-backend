# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stepserver', '0008_auto_20180417_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClusterGroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserClusterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stepserver.UserClusterGroupInfo')),
            ],
        ),
    ]