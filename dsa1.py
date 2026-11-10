import requests
import telebot
import time
import datetime
from telebot.types import InlineKeyboardButton as btn
from telebot.types import InlineKeyboardMarkup as mak
now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = mm + '/' + dd + '/' + yyyy + ' ' + hour + ':' + mi + ':' + ss
hours = now.hour
x = datetime.datetime.now()
g = datetime.datetime(2024, 3, 10, 0, 0, 0)
if x.strftime('%x') > g.strftime('%x'):
    print('\n\n')
    print('Time ends to buy contact @aa774578')
    print('\n\n')
    print(x)
    sys.exit(0)
if x.strftime('%x') == g.strftime('%x'):
    print('')
    if x.strftime('%X') > g.strftime('%X'):
        print('\n\n')
        print('Time ends to buy contact @aa774578')
        print('\n\n')
        print(x)
        sys.exit(0)
    else:
        print('')
else:
    print('')
print('')

def star(X):
    url1 = f'''http://instaup.marsapi.com/get_likes/follow/orders?user_id={X}'''
    red = requests.get(url1).text
    if 'instaup.developers@gmail.com' in red:
        return {
            'coins': '0' }
    url = f'''{X}'''
    req = requests.get(url)
    if '{"coins":0}' in req.text:
        return {
            'coins': '50' }
    if None in req.text:
        coin = req.text.split('{"coins":"')[1].split('"}}')[0]
        return {
            'coins': str(coin) }
    return {
        None: '50' }

Y = '\x1b[1;93m'
G = '\x1b[2;32m'
R = '\x1b[2;31m'
B = '\x1b[2;36m'
P = '\x1b[2;35m'
print(f'''{Y}               MADE BY E S C A N O R E AND E S S''')
print('************************************************************')
file = input(f'''{B}[√] Name File Ids : ''')
token = input(f'''{R}[√] Token : ''')
idtl = input(f'''{G}[√] Id Tele : ''')
bot = telebot.TeleBot(token)
bot.send_message(idtl, 'I CHECK IDS FOR YOU👀🔥')
send = 0

def ch():
    global send
    pass
# WARNING: Decompyle incomplete

from threading import Thread


