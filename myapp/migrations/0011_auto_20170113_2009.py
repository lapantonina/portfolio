# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20170113_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bets',
            old_name='to_sell',
            new_name='currency_to_sell',
        ),
    ]
