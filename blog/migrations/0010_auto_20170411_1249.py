# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 07:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170411_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 7, 19, 2, 342610, tzinfo=utc), verbose_name='Created on:'),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
