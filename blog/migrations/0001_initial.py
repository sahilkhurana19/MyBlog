# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-30 17:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc_sh', models.TextField()),
                ('desc_lg', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2017, 3, 30, 17, 2, 33, 829881, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('read_time', models.IntegerField(default=5)),
            ],
        ),
    ]
