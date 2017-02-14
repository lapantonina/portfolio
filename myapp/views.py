#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

# Create your views here.
import os, sys
import requests, json, base64
import textwrap
import math, time, datetime, random
import django.shortcuts
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.template import Template, Context, loader, RequestContext
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from django.db import connection
from .models import *
from .forms import *
from fractions import Fraction
from jsonpath_rw import jsonpath, parse
from objectpath import *

URL_BASE = 'https://api.flickr.com/services/rest/?'
API_KEY = 'a2a7084e3f260f580e687bc7a65c6b75'
FORMAT = 'json'
NOJSONCALLBACK = '1'
BASIC_REQUEST = (URL_BASE + 'api_key=' + API_KEY + '&format=' + FORMAT + '&nojsoncallback=' + NOJSONCALLBACK + '&method=')


def handler404(request):
    return TemplateResponse(request, '404.html')
    response.status_code = 404

def handler500(request):
    return TemplateResponse(request, '50x.html')
    response.status_code = 500

def user_photos(request):

  urlname = request.GET['username']
  profile_url = 'https://www.flickr.com/photos/' + urlname

  upper_text = 'Impossible considered invitation him men instrument saw celebrated unpleasant. \
  Put rest and must set kind next many near nay. He exquisite continued explained middleton am. \
  Voice hours young woody has she think equal. Estate moment he at on wonder at season little. \
  Six garden result summer set family esteem nay estate. End admiration mrs unreserved discovered comparison especially invitation.'
  above_text = '<p>Able an hope of body. Any nay shyness article matters own removal nothing his forming. \
  Gay own additions education satisfied the perpetual. If he cause manor happy. Without farther she exposed \
  saw man led. Along on happy could cease green oh. </p><p>Betrayed cheerful declared end and. Questions we \
  additions is extremely incommode. Next half add call them eat face. Age lived smile six defer bed their few. \
  Had admitting concluded too behaviour him she. Of death to or to being other. </p></div><div class="col-sm-6">\
  <p>Effects present letters inquiry no an removed or friends. Desire behind latter me though in. Supposing shameless \
  am he engrossed up additions. My possible peculiar together to. Desire so better am cannot he up before points. \
  Remember mistaken opinions it pleasure of debating. Court front maids forty if aware their at. Chicken use are pressed \
  removed. </p><p>Saw yet kindness too replying whatever marianne. Old sentiments resolution admiration unaffected its \
  mrs literature. Behaviour new set existence dashwoods. It satisfied to mr commanded consisted disposing engrossed. \
  Tall snug do of till on easy. Form not calm new fail. </p>'

  if 'p' not in request.GET:
    p = 1
  elif 'p' in request.GET:
    p = int(request.GET['p'])
  current_page = p
  next_page = current_page + 1
  prev_page = current_page - 1

  photo_list = []
  paginator = []


  method = 'flickr.urls.lookupUser'
  extra_param = ('&url=' + profile_url)

  user_id_request = (BASIC_REQUEST + method + extra_param)

  json_obj = requests.get(user_id_request)
  resp = json_obj.json()


  if resp['stat'] == 'fail': # There is no user with such name
    short_descr = 'There is no such user on Flickr'
    real_name = 'We know nothing about him'
    portfolio = ''
    userpic = '<img src="https://s.yimg.com/pw/images/buddyicon.jpg" alt="" class="img-responsive img-circle">'
    upper_text = ''
  
  elif resp['stat'] == 'ok': # There is a user with such name
    user = resp['user']
    user_id = user['id']
    username_stat = user['username']
    short_descr = 'About ' + urlname

    method = 'flickr.people.getInfo'
    extra_param = ('&user_id=' + user_id)

    user_info_request = ( BASIC_REQUEST + method + extra_param)

    json_obj = requests.get(user_info_request)
    resp = json_obj.json()

    person = resp['person']
    iconserver = str(person['iconserver'])
    iconfarm = str(person['iconfarm'])
    try:
      cont = person['realname']
      real_name = cont['_content']
    except KeyError:
      real_name = urlname
    
    text = ''

    method = 'flickr.people.getPublicPhotos'
    extra_param = ('&user_id=' + user_id + 
                  '&per_page=' + '60' + 
                  '&page=' + str(p)
                  )

    photo_info_request = (BASIC_REQUEST + method + extra_param)

    json_obj = requests.get(photo_info_request)
    resp = json_obj.json()

    photos = resp['photos']
    photo = photos['photo']
    pages = int(photos['pages'])


    if len(photo) == 0: # No public photos
      text = text + '<p>' + urlname + ' has no public photos yet</p>'

    else:

      for item in photo:
        farm = str(item['farm'])
        server = str(item['server'])
        photo_id = str(item['id'])
        secret = str(item['secret'])
        title = str(item['title'])

        photo_list.append('<div class="col-sm-2"><div class="box"><a href="https://farm' + farm + '.staticflickr.com/' + server + \
          '/' + photo_id + '_' + secret + '_z.jpg" alt="' + title + '" data-toggle="lightbox" data-gallery="portfolio" data-title="' + \
          title + '" data-footer="Some footer information"><img src="https://farm' + farm + '.staticflickr.com/' + server + '/' + photo_id + '_' + secret + '_q.jpg" \
          alt="" class="img-responsive"></a></div></div>')

      if pages > 1:

        paginator.append('<hr>\n    <div class="row text-center">\n     <div class="col-lg-12">\n      <ul class="pagination">\n       ')

        for page in range(1, pages+1):
          if page == current_page:
            paginator.append('       <li class="active">\n        <a href="/photos_of_?username=' + urlname + '&p=' + str(current_page) + '">' + str(current_page) + '</a>\n       </li>\n')
          else:
            paginator.append('       <li>\n        <a href="photos_of_?username=' + urlname + '&p=' + str(page) + '">' + str(page) + '</a>\n       </li>')       
        
        paginator.append('      </ul>\n     </div>\n    </div>\n')                

    userpic = '<img src="https://farm' + iconfarm + '.staticflickr.com/' + iconserver + '/buddyicons/' + user_id + '_r.jpg" alt="" class="img-responsive img-circle">'''
  t = get_template('photos_templ_bootstrap.html')
  html = t.render(Context({'userpic': userpic, 'upper_text': upper_text, 'above_text': above_text, 'short_descr': short_descr, 'about': real_name, 'username': urlname, 'photos': '\n'.join(photo_list), 'paginator': ''.join(paginator)}))
  del photo_list[:]
  del paginator[:]
  

  return HttpResponse(html)

def home_page(request):
  t = get_template('home_templ.html')
  html = t.render(Context())
  return HttpResponse(html)




@csrf_exempt
def contact_view(request):
  form = ContactForm()
  if request.method == 'POST':
    form = ContactForm(request.POST)
    # Если форма заполнена корректно, сохраняем все введённые пользователем значения
    if form.is_valid():
      subject = form.cleaned_data['subject']
      sender = form.cleaned_data['sender']
      message = form.cleaned_data['message']

      recepients = ['antoninacurafina@gmail.com']
      try:
          send_mail(subject, message, sender, recepients)
          return TemplateResponse(request, 'mail_sent.html')
      except BadHeaderError: #Защита от уязвимости
          return HttpResponse('Invalid header found')
      # Переходим на другую страницу, если сообщение отправлено
      return TemplateResponse(request, 'mail_sent.html')

    else:
        form = ContactForm()
  # Выводим форму в шаблон
  return TemplateResponse(request, 'contact.html', {'form': form, 'username': ''})


def maze(request):

  # количество клеток/ходов в высоту и ширину, задаются пользователем
  w = 0
  h = 0

  # длина стороны квадратной комнаты и ширина стенки (длина=длине комнаты), также есть в стилях шаблона
  room_width = 30
  wall_width = 10
  cell_width = room_width + wall_width

  # тут может быть любой набор символов, но с такими лабиринт нагляден даже в качестве построчного вывода массива
  space = ' '
  full = '*'
  line_hor = '_'
  line_ver = '|'

  maze = []
  pure_path = [] #список всех ходов без учета выбирания из тупиков
  keychain = [] #список всех ходов с учетом выбирания из тупиков (ходы, приводящие в тупики, убираются после выхода из тупика)


  #проверка на тупик (отсутствие ходов из данной позиции)
  def check_dead_end(maze, height, width, x, y):
    if (x == height-2 or maze[x+2][y] == space) and (y == width-2 or maze[x][y+2] == space) and (x == 1 or maze[x-2][y] == space) and (y == 1 or maze[x][y-2] == space):
      return 'yes'
    else:
      return 'no'

  if 'h' in request.GET and 'w' in request.GET:
    h = int(request.GET['h'])
    w = int(request.GET['w'])
    if h > 0 and w > 0:

      
      # по два символа на клетку (три подряд клетки выглядят так: |_|_|_) плюс доп. клетка в высоту и ширину (от нее оставим только стенку)
      height = h * 2 + 1
      width = w * 2 + 1
      h_px = str(h * cell_width + wall_width)+'px'
      w_px = str(w * cell_width + wall_width)+'px'

      # строим непройденный дабиринт, есть стенки клетка состоит из заполнение + 3/6 стенок, + доп. стенки для замыкающих клеток
      maze = [[line_ver, full] * (w+1) for q in range(height)]
      walls = [[line_hor, line_hor] * (w+1) for q in range(height)]

      for q in range(0, height, 2):
        maze[q] = walls[q]

      for q in range(height):
        del maze[q][-1]
        maze[q][0] = maze[q][-1] = line_ver

      # задаем (любые нечетные) координаты начала построения. Из середины, т к так лабиринт будет сложнее (больше тупиковых ответвлений)
      x = 2 * int(h//2) +1
      y = 2 * int(w//2) +1
      o = []


      ##################### MAIN ############################
      while len(pure_path) < w*h-1:

        maze[x][y] = space # пройденная клетка отмечается как пустая

        if check_dead_end(maze, height, width, x, y) == 'no':
          key = random.randint(0, 3)
          if key == 0:
            if x < height-2 and maze[x+2][y] == full:
              maze[x+1][y] = space
              x = x+2
              keychain.append(key)
              pure_path.append(key)
          elif key == 1:
            if y < width-2 and maze[x][y+2] == full:
              maze[x][y+1] = space
              y = y+2
              keychain.append(key)
              pure_path.append(key)
          elif key == 2:
            if x > 1 and maze[x-2][y] == full:
              maze[x-1][y] = space
              x = x-2
              keychain.append(key)
              pure_path.append(key)
          elif key == 3:
            if y > 2 and maze[x][y-2] == full:
              maze[x][y-1] = space
              y = y-2
              keychain.append(key)
              pure_path.append(key)
          
        elif check_dead_end(maze, height, width, x, y) == 'yes':
          last_key = keychain[-1]
          if last_key == 0:
            x = x-2
          elif last_key == 1:
            y = y-2
          elif last_key == 2:
            x = x+2
          elif last_key == 3:
            y = y+2
          del keychain[-1]


      
      get_a_surprise = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat'
      json_obj = requests.get(get_a_surprise)
      resp = json_obj.json()

      meta = resp['meta']
      if meta['msg'] == 'OK':
        img = resp['data']
        surprise = img['image_original_url']
        surprise_hight = img['image_height']
        surprise_width = img['image_width']
      else:
        surprise = '/static/img/zhevuzador.jpg'
        surprise_hight = '532px'
        surprise_width = '300px'


      ##################### MAIN ############################


      safe_web_colors = ['FFFFCC', 'FFFF99', 'FFFF66', 'FFFF33', 'FFFF00', 'CCCC00', 'FFCC66', 'FFCC00', 'FFCC33', \
      'CC9900', 'CC9933', '996600', 'FF9900', 'FF9933', 'CC9966', 'CC6600', '996633', '663300', 'FFCC99', 'FF9966', \
      'FF6600', 'CC6633', '993300', '660000', 'FF6633', 'CC3300', 'FF3300', 'FF0000', 'CC0000', '990000', 'FFCCCC', \
      'FF9999', 'FF6666', 'FF3333', 'FF0033', 'CC0033', 'CC9999', 'CC6666', 'CC3333', '993333', '990033', '330000', \
      'FF6699', 'FF3366', 'FF0066', 'CC3366', '996666', '663333', 'FF99CC', 'FF3399', 'FF0099', 'CC0066', '993366', \
      '660033', 'FF66CC', 'FF00CC', 'FF33CC', 'CC6699', 'CC0099', '990066', 'FFCCFF', 'FF99FF', 'FF66FF', 'FF33FF', \
      'FF00FF', 'CC3399', 'CC99CC', 'CC66CC', 'CC00CC', 'CC33CC', '990099', '993399', 'CC66FF', 'CC33FF', 'CC00FF', \
      '9900CC', '996699', '660066', 'CC99FF', '9933CC', '9933FF', '9900FF', '660099', '663366', '9966CC', '9966FF', \
      '6600CC', '6633CC', '663399', '330033', 'CCCCFF', '9999FF', '6633FF', '6600FF', '330099', '330066', '9999CC', \
      '6666FF', '6666CC', '666699', '333399', '333366', '3333FF', '3300FF', '3300CC', '3333CC', '000099', '000066', \
      '6699FF', '3366FF', '0000FF', '0000CC', '0033CC', '000033', '0066FF', '0066CC', '3366CC', '0033FF', '003399', \
      '003366', '99CCFF', '3399FF', '0099FF', '6699CC', '336699', '006699', '66CCFF', '33CCFF', '00CCFF', '3399CC', \
      '0099CC', '003333', '99CCCC', '66CCCC', '339999', '669999', '006666', '336666', 'CCFFFF', '99FFFF', '66FFFF', \
      '33FFFF', '00FFFF', '00CCCC', '99FFCC', '66FFCC', '33FFCC', '00FFCC', '33CCCC', '009999', '66CC99', '33CC99', \
      '00CC99', '339966', '009966', '006633', '66FF99', '33FF99', '00FF99', '33CC66', '00CC66', '009933', '99FF99', \
      '66FF66', '33FF66', '00FF66', '339933', '006600', 'CCFFCC', '99CC99', '66CC66', '669966', '336633', '003300', \
      '33FF33', '00FF33', '00FF00', '00CC00', '33CC33', '00CC33', '66FF00', '66FF33', '33FF00', '33CC00', '339900', \
      '009900', 'CCFF99', '99FF66', '66CC00', '66CC33', '669933', '336600', '99FF00', '99FF33', '99CC66', '99CC00', \
      '99CC33', '669900', 'CCFF66', 'CCFF00', 'CCFF33', 'CCCC99', '666633', '333300', 'CCCC66', 'CCCC33', '999966', \
      '999933', '999900', '666600', 'FFFFFF', 'CCCCCC', '999999', '666666', '333333', '000000']

      background_color = safe_web_colors[random.randint(0, len(safe_web_colors)-1)]

      # эта строка не в шаблоне, т к фигурные скобки конкурируют со скобками стиля
      o.append(str('  <div id="maze" style="width:' + w_px + '; height:' + h_px + '; background:#' + background_color + '">'))


      for x in range(height):
        for y in range(width):
          if x == 1 and y == 0: #start_invisible_wall
            o.append('   <div id="wall_' + str(x//2+1) + '_' + str(y//2+1) + '", class="line_ver invsbl"></div>')
          elif maze[x][y] == line_ver:
            if x % 2 == 0:
              o.append('   <div class="corner"></div>')
            else:
              o.append('   <div id="wall_' + str(x//2+1) + '_' + str(y//2+1) + '", class="line_ver"></div>')
          elif maze[x][y] == line_hor:
            if x == 2*h and y == 2 * w - 1: #finish_invisible_wall
              o.append('   <div id="ceil_' + str(x//2+1) + '_' + str(y//2+1) + '", class="finish"></div>')
            elif y % 2 == 0:
              o.append('   <div class="corner"></div>')
            else:
              o.append('   <div id="ceil_' + str(x//2+1) + '_' + str(y//2+1) + '", class="line_hor"></div>')
          elif maze[x][y] == space or full:
            if x % 2 == 0:
              o.append('   <div class="space"></div>')
            elif y % 2 == 0:
              o.append('   <div class="high_space"></div>')
            else:
              o.append('   <div id="cell_' + str(x//2+1) + '_' + str(y//2+1) + '", class="runner invsbl"></div>')
      
      o.append('  </div>')

      #картинка-награда
      gif = '<div id="gif" class="secret"><iframe src="' + surprise + '" width="' + surprise_width + '" height="' + surprise_hight + '" frameBorder="0" class="giphy-embed"></iframe></div>'
      
      t = get_template('maze_templ.html')

      html = t.render(Context({'wdth': w_px, 'hght': h_px, 'height': h, 'width': w, 'runner': '\n'.join(o), 'gif': gif}))

      del pure_path[:]
      
      return HttpResponse(html)

def stack(request):

  ask_chain = dict()
  bid_chain = dict()
  firstCurrency = 'USD'
  secondCurrency = 'BTC'
  nice_spread = False
  exchanges_names = []

  # для каждой биржи: словарь с данными (распаршенный до нужной степени api) + ключи
  exchanges = {
    'CEX.io': {
      'name': 'CEX.io',
      'data_chain': requests.get('https://cex.io/api/ticker/' + secondCurrency + '/' + firstCurrency).json(),
      'ask': 'ask',
      'bid': 'bid',
    },
    'cCEX': {
      'name': 'cCEX',
      'data_chain': requests.get('https://c-cex.com/t/' + secondCurrency.lower() + '-' + firstCurrency.lower() + '.json').json()['ticker'],
      'ask': 'sell',
      'bid': 'buy',
    },
    'Poloniex': {
      'name': 'Poloniex',
      'data_chain': requests.get('https://poloniex.com/public?command=returnTicker').json()['USDT_BTC'],
      'ask': 'lowestAsk',
      'bid': 'highestBid',
    },
    'HitBTC': {
      'name': 'HitBTC',
      'data_chain': requests.get('https://api.hitbtc.com/api/1/public/'+ secondCurrency + firstCurrency + '/ticker').json(),
      'ask': 'ask',
      'bid': 'bid',
    },
    'BitFinex': {
      'name': 'BitFinex',
      'data_chain': requests.get('https://api.bitfinex.com/v2/ticker/t' + secondCurrency + firstCurrency).json(),
      'ask': 2,
      'bid': 0,
    },
    'Btc-e': {
      'name': 'Btc-e',
      'data_chain': requests.get('https://btc-e.com/api/3/ticker/' + secondCurrency.lower() + '_' + firstCurrency.lower()).json()[secondCurrency.lower() + '_' + firstCurrency.lower()],
      'ask': 'sell',
      'bid': 'buy',
    },
    'XBTCE': {
      'name': 'XBTCE',
      'data_chain': requests.get('https://cryptottlivewebapi.xbtce.net:8443/api/v1/public/ticker/' + secondCurrency + firstCurrency).json()[0],
      'ask': 'BestAsk',
      'bid': 'BestBid',
    },
    'EXMO': {
      'name': 'EXMO',
      'data_chain': requests.get('https://api.exmo.com/v1/ticker').json()[secondCurrency + '_' + firstCurrency],
      'ask': 'sell_price',
      'bid': 'buy_price',
    },
    'Yobit': {
      'name': 'Yobit',
      'data_chain': requests.get('https://yobit.net/api/3/ticker/' + secondCurrency.lower() + '_' + firstCurrency.lower()).json()[secondCurrency.lower() + '_' + firstCurrency.lower()],
      'ask': 'sell',
      'bid': 'buy',
    },
  }

  for exchange in exchanges:

    data_chain = exchanges[exchange]['data_chain']
    ask_path = exchanges[exchange]['ask']
    bid_path = exchanges[exchange]['bid']

    try:
      ask_chain[exchange] = ask = float(data_chain[ask_path]) #создаем связку значений "биржа-аск", "биржа-бид"
      bid_chain[exchange] = bid = float(data_chain[bid_path])
    except(KeyError, IndexError):
      ask = 0.0
      bid = 0.0

  lowest_ask = sorted(ask_chain.items(), key=lambda q: q[1]) #связки сортируются по значениям от мин. к макс. и наоборот
  highest_bid = sorted(bid_chain.items(), key=lambda q: q[1], reverse=True)

  spread = (highest_bid[0][1] - lowest_ask[0][1])
  pretty_spread = "%0.6f" % spread
  if spread > 0.0:
    nice_spread = True

  print(ask_chain)

  bet = Bet_USD_BTC(
    highest_bid = highest_bid[0][1],
    h_bid_stack = highest_bid[0][0],
    lowest_ask = lowest_ask[0][1],
    l_ask_stack = lowest_ask[0][0],
    spread = pretty_spread,
    time = datetime.now(),
    nice_spread = nice_spread
    )
  print(bet)
  bet.save()
  
  time.sleep(60)
  return stack(request)


def current_exchange_rate(request):

  rates = Bet_USD_BTC.objects.order_by('-time')
  previous_data = []
  bid_data = []
  ask_data = []
  time_data = []
  h_bid_stack = []
  l_ask_stack = []
  spread = []

  for z in range(25):
    highest_bid = "%0.2f" %float(rates[z].highest_bid)
    lowest_ask = "%0.2f" %float(rates[z].lowest_ask)
    date = str(rates[z].time.strftime("%d.%m.%Y"))
    time = str(rates[z].time.strftime("%I:%M %p"))
    h_bid_stack = str(rates[z].h_bid_stack)
    l_ask_stack = str(rates[z].l_ask_stack)
    spread = "%0.2f" %float(rates[z].spread)
    bid_data.insert(0, highest_bid)
    ask_data.insert(0, lowest_ask)
    time_data.insert(0, time)

  previous_data.append(bid_data)
  previous_data.append(ask_data)
  previous_data.append(time_data)
  previous_data.append(h_bid_stack)
  previous_data.append(l_ask_stack)
  previous_data.append(spread)
  
  response = TemplateResponse(request, 'USD-BTC_exchange_rate.html', ({'previous_data': previous_data}))
  return response


def get_best_rate(request):

  rates = Bet_USD_BTC.objects.order_by('-time')

  best_rate = {'date': str(rates[0].time.strftime("%d.%m.%Y")),
    'time': str(rates[0].time.strftime("%I:%M %p")), 
    'highest_bid': "%0.2f" %float(rates[0].highest_bid), 
    'h_bid_stack': str(rates[0].h_bid_stack), 
    'lowest_ask': "%0.2f" %float(rates[0].lowest_ask),
    'l_ask_stack': str(rates[0].l_ask_stack), 
    'spread': float(rates[0].spread)
    }

  return HttpResponse(json.dumps(best_rate))


