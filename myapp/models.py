from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Bet_USD_BTC(models.Model):

	time = models.DateTimeField()
	highest_bid = models.DecimalField(max_digits=7, decimal_places=6)
	h_bid_stack = models.CharField(max_length=30)
	lowest_ask = models.DecimalField(max_digits=7, decimal_places=6)
	l_ask_stack = models.CharField(max_length=30)
	spread = models.DecimalField(max_digits=7, decimal_places=6)
	nice_spread = models.BooleanField(default=False)

