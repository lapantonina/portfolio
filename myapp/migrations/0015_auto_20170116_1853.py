# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 18:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20170113_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet_usd_btc',
            old_name='BTC38_ask',
            new_name='highest_bid',
        ),
        migrations.RenameField(
            model_name='bet_usd_btc',
            old_name='BTC38_bid',
            new_name='lowest_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='BTCE_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='BTCE_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='BTER_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='BTER_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitcoin_Indonesia_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitcoin_Indonesia_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitcoin_de_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitcoin_de_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitfinex_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitfinex_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitstamp_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bitstamp_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bittrex_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Bittrex_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='CEX_IO_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='CEX_IO_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Coinbase_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Coinbase_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Coincheck_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Coincheck_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='CoinsBankCoinsBank_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='CoinsBank_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='CoinsBank_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Cryptopia_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Cryptopia_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='DABTC_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='DABTC_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Exmo_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Exmo_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='GDAX_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='GDAX_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Gemini_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Gemini_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='HitBTC_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='HitBTC_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Huobi_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Huobi_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Jubi_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Jubi_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Korbit_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Korbit_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Kraken_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Kraken_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Livecoin_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Livecoin_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='OKCoin_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='OKCoin_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='OkCoin_Intl_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='OkCoin_Intl_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Poloniex_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Poloniex_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='QuadrigaCX_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='QuadrigaCX_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Ripple_Gateways_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Ripple_Gateways_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='ShapeShift_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='ShapeShift_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='YoBit_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='YoBit_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Yuanbao_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='Yuanbao_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='itBit_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='itBit_bid',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='xBTCe_ask',
        ),
        migrations.RemoveField(
            model_name='bet_usd_btc',
            name='xBTCe_bid',
        ),
        migrations.AddField(
            model_name='bet_usd_btc',
            name='h_bid_stack',
            field=models.CharField(default=0.0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bet_usd_btc',
            name='l_ask_stack',
            field=models.CharField(default=0.0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bet_usd_btc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 18, 53, 3, 855256)),
        ),
    ]