# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.SmallIntegerField()),
                ('width', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'maze',
            },
        ),
    ]
