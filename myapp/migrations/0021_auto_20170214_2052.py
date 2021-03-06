# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_bet_usd_btc_nice_spread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet_usd_btc',
            name='highest_bid',
            field=models.DecimalField(decimal_places=6, max_digits=19),
        ),
        migrations.AlterField(
            model_name='bet_usd_btc',
            name='lowest_ask',
            field=models.DecimalField(decimal_places=6, max_digits=19),
        ),
        migrations.AlterField(
            model_name='bet_usd_btc',
            name='spread',
            field=models.DecimalField(decimal_places=6, max_digits=19),
        ),
    ]
