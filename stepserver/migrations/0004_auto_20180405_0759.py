# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 23:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stepserver', '0003_auto_20180328_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('difficulty', models.IntegerField(default=0)),
                ('is_target_step_level', models.BooleanField(default=False)),
                ('is_target_duration', models.BooleanField(default=False)),
                ('is_target_break', models.BooleanField(default=False)),
                ('is_target_consistency', models.BooleanField(default=False)),
                ('is_target_engagement', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StreakAttributeDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StreakGroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('step_level', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('break_length', models.CharField(max_length=100)),
                ('consistency', models.CharField(max_length=100)),
                ('engagement', models.CharField(max_length=100)),
                ('recommendation_id_ongoing', models.IntegerField(default=0)),
                ('recommendation_id_upcoming', models.IntegerField(default=0)),
                ('is_target_step_level', models.BooleanField(default=False)),
                ('is_target_duration', models.BooleanField(default=False)),
                ('is_target_break', models.BooleanField(default=False)),
                ('is_target_consistency', models.BooleanField(default=False)),
                ('is_target_engagement', models.BooleanField(default=False)),
                ('has_bad_prediction', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StreakInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('step_level', models.CharField(blank=True, default='', max_length=100)),
                ('duration', models.CharField(blank=True, default='', max_length=100)),
                ('break_length', models.CharField(blank=True, default='', max_length=100)),
                ('consistency', models.CharField(blank=True, default='', max_length=100)),
                ('engagement', models.CharField(blank=True, default='', max_length=100)),
                ('is_target_step_level', models.BooleanField(default=False)),
                ('is_target_duration', models.BooleanField(default=False)),
                ('is_target_break', models.BooleanField(default=False)),
                ('is_target_consistency', models.BooleanField(default=False)),
                ('is_target_engagement', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stepserver.StreakGroupInfo')),
            ],
        ),
        migrations.AddField(
            model_name='streak',
            name='cohort_end_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='streak',
            name='cohort_start_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='streak',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='streak',
            name='streak_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='streak',
            name='user_cluster_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='start_date',
            field=models.DateField(default=datetime.date(2018, 4, 5)),
        ),
        migrations.AlterField(
            model_name='stepcount',
            name='date',
            field=models.DateField(default=datetime.date(2018, 4, 5)),
        ),
        migrations.AlterField(
            model_name='streak',
            name='end_date',
            field=models.DateField(default=datetime.date(2018, 4, 5)),
        ),
        migrations.AlterField(
            model_name='streak',
            name='start_date',
            field=models.DateField(default=datetime.date(2018, 4, 5)),
        ),
    ]
