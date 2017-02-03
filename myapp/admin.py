from django.contrib import admin

from .models import Bet_USD_BTC
# Register your models here.

# какие колонки выводятся
class Bet_USD_BTC_admin(admin.ModelAdmin):
    list_display = ['time', 'highest_bid', 'h_bid_stack', 'lowest_ask', 'l_ask_stack', 'spread', 'nice_spread']


admin.site.register(Bet_USD_BTC, Bet_USD_BTC_admin)
