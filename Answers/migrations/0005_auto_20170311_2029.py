# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Answers', '0004_auto_20170311_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='change_pass_answer',
            field=models.CharField(max_length=255),
        ),
    ]
