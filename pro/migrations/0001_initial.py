# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='pro_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_working', models.TimeField()),
                ('finish_working', models.TimeField()),
                ('date_of_working', models.DateField(default='2016-04-21')),
                ('holidays', models.DateField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='users_vstrecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.pro_users')),
            ],
        ),
        migrations.CreateModel(
            name='vstrecha',
            fields=[
                ('start', models.TimeField()),
                ('finish', models.TimeField()),
                ('length', models.TimeField()),
                ('date_of_meeting', models.DateField(default='2016-04-21')),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.AddField(
            model_name='users_vstrecha',
            name='vstrecha_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.vstrecha'),
        ),
    ]
