#!/usr/bin/env python3
# encoding: utf-8
"""
Created on 2016-12-21 under WTFPL software license.
See www.wtfpl.net/about/ for details.
"""

import requests

ask = bid = {}
firstCurrency = 'BTC'
secondCurrency = 'ETH'
thirdCurrency = 'ZEC'


def query(url):
  try:
    req = requests.get(url, verify=True, timeout=5)
    json = req.json()
  except Exception as e:
    print(e)
    json = {"error": e}
  return json


def collect_exchange_data(arg):
  if arg.lowestAsk:
    ask[arg.name] = arg.lowestAsk
  if arg.highestBid:
    bid[arg.name] = arg.highestBid
  if arg.last > 0:
    print(arg.name, '\t', round(arg.last, 5), '\t', round(arg.highestBid, 5), '\t', round(arg.lowestAsk, 5), '\t',
          round(arg.spread * 1, 3))


def analytical_report():
  # Sort the results
  ask_sorted = sorted(ask.items(), key=lambda q: q[1])
  bid_sorted = sorted(bid.items(), key=lambda q: q[1], reverse=True)

  # Calculate profit and profit percentage
  profit = bid_sorted[0][1] - ask_sorted[0][1]
  if ask_sorted[0][1]:
    profit_p = profit * 100 / ask_sorted[0][1]
  else:
    profit_p = None

  print('------------------------------------------------------------------')
  print('Buy on  ', end='')
  for key, value in ask_sorted:
    print(key + ': ' + str(value) + ', ', end='')
  print('.\nSell on ', end='')
  for key, value in bid_sorted:
    print(key + ': ' + str(value) + ', ', end='')

  print('.\n------------------------------------------------------------------')
  if profit < 0:
    print('CONCLUSION. No arbitrage opportunity detected :(')
  else:
    print('CONCLUSION. You could buy some ' + secondCurrency + ' for ' + str(ask_sorted[0][1]) + ' ' + firstCurrency +
          ' at ' + str(ask_sorted[0][0]) + ' and sell it for ' + str(bid_sorted[0][1]) + ' ' + firstCurrency +
          ' at ' + str(bid_sorted[0][0]) + ', and get ' + str(round(profit_p, 3)) +
          '% (or ' + str(round(profit * 1000, 4)) + ' m' + firstCurrency + ') profit. BWAHAHA!')
  print()


exchanges = {'CEX.io': {
              url: 'https://cex.io/api/ticker/' + secondCurrency + '/' + firstCurrency,
              lowestAsk : float(parsed_json['ask']),
              highestBid = float(parsed_json['bid']),
              },
            'cCEX': {
              url: 'https://c-cex.com/t/' + secondCurrency.lower() + '-' + firstCurrency.lower() + '.json',
              lowestAsk = float(parsed_json['ticker']['sell'])
              highestBid = float(parsed_json['ticker']['buy'])
            }
}



def Exchange(request):
  json_obj = requests.get(url)
  parsed_json = json_obj.json()
  spread = lowestAsk - highestBid
  CEX()
  cCEX()
  LiveCoin()
  Poloniex()
  HitBTC()
  Kraken()
  YoBit()
  BitFinex()
  Exmo()
  BTCE()
  XBTCE()
  ShapeShift()

  def CEX():
    url = 'https://cex.io/api/ticker/' + secondCurrency + '/' + firstCurrency
    name = 'CEX.io'

    try:
      lowestAsk = float(parsed_json['ask'])
      highestBid = float(parsed_json['bid'])
    except (IndexError, KeyError):
      lowestAsk = 0.0
      highestBid = 0.0

  def cCEX():
    url = 'https://c-cex.com/t/' + secondCurrency.lower() + '-' + firstCurrency.lower() + '.json'
    name = 'CCex'

    try:
      lowestAsk = float(parsed_json['ticker']['sell'])
      highestBid = float(parsed_json['ticker']['buy'])
    except (IndexError, KeyError):
      lowestAsk = 0.0
      highestBid = 0.0


class cCEX(object):
  def __init__(self):
    super(cCEX, self).__init__()
    self.url = 'https://c-cex.com/t/' + secondCurrency.lower() + '-' + firstCurrency.lower() + '.json'
    self.parsed_json = query(self.url)
    self.name = 'CCex'

    try:
      self.last = float(self.parsed_json['ticker']['lastprice'])
      self.lowestAsk = float(self.parsed_json['ticker']['sell'])
      self.highestBid = float(self.parsed_json['ticker']['buy'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class LiveCoin(object):
  def __init__(self):
    super(LiveCoin, self).__init__()
    self.url = 'https://api.livecoin.net/exchange/ticker/' + secondCurrency + '/' + firstCurrency
    self.parsed_json = query(self.url)
    self.name = 'LiveCoin'

    try:
      self.last = float(self.parsed_json['last'])
      self.lowestAsk = float(self.parsed_json['best_ask'])
      self.highestBid = float(self.parsed_json['best_bid'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class Poloniex(object):
  def __init__(self):
    super(Poloniex, self).__init__()
    self.url = 'https://poloniex.com/public?command=returnTicker'
    self.parsed_json = query(self.url)
    self.name = 'Poloniex'

    try:
      self.last = float(self.parsed_json[firstCurrency + '_' + secondCurrency + '']['last'])
      self.lowestAsk = float(self.parsed_json[firstCurrency + '_' + secondCurrency + '']['lowestAsk'])
      self.highestBid = float(self.parsed_json[firstCurrency + '_' + secondCurrency + '']['highestBid'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class HitBTC(object):
  def __init__(self):
    super(HitBTC, self).__init__()
    self.url = 'https://api.hitbtc.com/api/1/public/'+ secondCurrency + firstCurrency + '/ticker'
    self.parsed_json = query(self.url)
    self.name = 'HitBTC'

    try:
      self.last = float(self.parsed_json['last'])
      self.lowestAsk = float(self.parsed_json['ask'])
      self.highestBid = float(self.parsed_json['bid'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class Kraken(object):
  def __init__(self):
    super(Kraken, self).__init__()
    if firstCurrency == 'BTC':
      firstCurrencyKraken = 'XBT'
    else:
      firstCurrencyKraken = firstCurrency
    self.url = 'https://api.kraken.com/0/public/Ticker?pair=' + secondCurrency + firstCurrencyKraken
    self.parsed_json = query(self.url)
    self.name = 'Kraken'

    try:
      self.last = float(self.parsed_json['result']['X' + secondCurrency + 'XXBT']['c'][0])
      self.lowestAsk = float(self.parsed_json['result']['X' + secondCurrency + 'XXBT']['a'][0])
      self.highestBid = float(self.parsed_json['result']['X' + secondCurrency + 'XXBT']['b'][0])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class YoBit(object):
  def __init__(self):
    super(YoBit, self).__init__()
    if firstCurrency == 'RUB':
      firstCurrencyYobit = 'RUR'
    else:
      firstCurrencyYobit = firstCurrency
    self.url = 'https://yobit.net/api/3/ticker/' + secondCurrency.lower() + '_' + firstCurrencyYobit.lower()
    self.parsed_json = query(self.url)
    self.name = 'YoBit'

    try:
      self.last = float(self.parsed_json[secondCurrency.lower() + '_' + firstCurrencyYobit.lower()]['last'])
      self.lowestAsk = float(self.parsed_json[secondCurrency.lower() + '_' + firstCurrencyYobit.lower()]['sell'])
      self.highestBid = float(self.parsed_json[secondCurrency.lower() + '_' + firstCurrencyYobit.lower()]['buy'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.2
    collect_exchange_data(self)


class BitFinex(object):
  def __init__(self):
    super(BitFinex, self).__init__()
    self.url = 'https://api.bitfinex.com/v2/ticker/t' + secondCurrency + firstCurrency
    self.parsed_json = query(self.url)
    self.name = 'BitFinex'

    try:
      self.last = float(self.parsed_json[6])
      self.lowestAsk = float(self.parsed_json[2])
      self.highestBid = float(self.parsed_json[0])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class Exmo(object):
  def __init__(self):
    super(Exmo, self).__init__()
    self.url = 'https://api.exmo.com/v1/ticker/'
    self.parsed_json = query(self.url)
    self.name = 'Exmo'

    try:
      self.last = float(self.parsed_json[secondCurrency + '_' + firstCurrency]['last_trade'])
      self.lowestAsk = float(self.parsed_json[secondCurrency + '_' + firstCurrency]['sell_price'])
      self.highestBid = float(self.parsed_json[secondCurrency + '_' + firstCurrency]['buy_price'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class BTCE(object):
  def __init__(self):
    super(BTCE, self).__init__()

    if firstCurrency == 'RUB':
      firstCurrencyBTCe = 'RUR'
    else:
      firstCurrencyBTCe = firstCurrency

    if secondCurrency == 'DASH':
      secondCurrencyBTCe = 'DSH'
    else:
      secondCurrencyBTCe = secondCurrency

    self.url = 'https://btc-e.com/api/3/ticker/' + secondCurrencyBTCe.lower() + '_' + firstCurrencyBTCe.lower()
    self.parsed_json = query(self.url)
    self.name = 'BTC-E'

    try:
      self.last = float(self.parsed_json[secondCurrencyBTCe.lower() + '_' + firstCurrencyBTCe.lower()]['last'])
      self.lowestAsk = float(self.parsed_json[secondCurrencyBTCe.lower() + '_' + firstCurrencyBTCe.lower()]['buy'])
      self.highestBid = float(self.parsed_json[secondCurrencyBTCe.lower() + '_' + firstCurrencyBTCe.lower()]['sell'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class XBTCE(object):
  def __init__(self):
    super(XBTCE, self).__init__()
    if secondCurrency == 'DASH':
      secondCurrencyxBTCe = 'DSH'
    else:
      secondCurrencyxBTCe = secondCurrency
    self.url = 'https://cryptottlivewebapi.xbtce.net:8443/api/v1/public/ticker/' + secondCurrencyxBTCe + firstCurrency
    self.parsed_json = query(self.url)
    self.name = 'xBTC-E'

    try:
      self.last = float(self.parsed_json[0]['LastBuyPrice'])
      self.lowestAsk = float(self.parsed_json[0]['BestAsk'])
      self.highestBid = float(self.parsed_json[0]['BestBid'])
    except (IndexError, KeyError):
      self.last = 0.0
      self.lowestAsk = 0.0
      self.highestBid = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.fee = 0.0
    collect_exchange_data(self)


class ShapeShift(object):
  def __init__(self):
    super(ShapeShift, self).__init__()
    self.url = 'https://shapeshift.io/marketinfo/' + firstCurrency + '_' + secondCurrency
    self.parsed_json = query(self.url)
    self.name = 'ShapeShift'

    try:
      self.lowestAsk = 1 / float(self.parsed_json['rate'])
      self.fee = float(self.parsed_json['minerFee'])
    except (IndexError, KeyError):
      self.lowestAsk = 0.0
      self.fee = 0.0

    self.url = 'https://shapeshift.io/marketinfo/' + secondCurrency + '_' + firstCurrency
    self.parsed_json = query(self.url)

    try:
      self.highestBid = float(self.parsed_json['rate'])
      self.fee = float(self.parsed_json['minerFee'])
    except (IndexError, KeyError):
      self.highestBid = 0.0
      self.fee = 0.0

    self.spread = self.lowestAsk - self.highestBid
    self.last = (self.lowestAsk + self.highestBid) / 2
    collect_exchange_data(self)


def main():

  # Poll the exchanges
  CEX()
  cCEX()
  LiveCoin()
  Poloniex()
  HitBTC()
  Kraken()
  YoBit()
  BitFinex()
  Exmo()
  BTCE()
  XBTCE()
  ShapeShift()

  # Collect and print analytical report
  analytical_report()


if __name__ == '__main__':
  main()
