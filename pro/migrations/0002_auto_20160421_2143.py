# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro_users',
            name='finish_working',
            field=models.TimeField(default='00-00-00'),
        ),
        migrations.AlterField(
            model_name='pro_users',
            name='start_working',
            field=models.TimeField(default='00-00-00'),
        ),
        migrations.AlterField(
            model_name='vstrecha',
            name='finish',
            field=models.TimeField(default='00-00-00'),
        ),
        migrations.AlterField(
            model_name='vstrecha',
            name='length',
            field=models.TimeField(default='00-00-00'),
        ),
        migrations.AlterField(
            model_name='vstrecha',
            name='start',
            field=models.TimeField(default='00-00-00'),
        ),
    ]
