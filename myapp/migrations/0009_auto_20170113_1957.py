# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 19:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_currency_pairs_currency_pairs_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency_pairs',
            old_name='currensy_1',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='currency_pairs',
            old_name='currensy_2',
            new_name='to_sell',
        ),
    ]
