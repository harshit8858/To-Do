# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['date', 'time']},
        ),
        migrations.AddField(
            model_name='todo',
            name='now',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.TimeField(),
        ),
    ]
