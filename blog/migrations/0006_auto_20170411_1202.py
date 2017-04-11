# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170408_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 6, 32, 23, 52960, tzinfo=utc), verbose_name='Created on:'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.ManyToManyField(related_name='_tag_name_+', to='blog.Tag'),
        ),
    ]