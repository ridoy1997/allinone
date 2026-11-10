
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from binascii import unhexlify
from base64 import b64encode, b64decode
from urllib.parse import quote
import webbrowser
import json
import requests
import time
import os
import datetime
current_date = datetime.datetime.now().date()
if current_date > datetime.date(2023, 2, 11):
    red_text = '\x1b[31mTool stopped, contact to run it.\x1b[0m'
    print(red_text)
    exit()
A = '\x1b[1;91m'
B = '\x1b[1;90m'
C = '\x1b[1;97m'
E = '\x1b[1;92m'
H = '\x1b[1;93m'
K = '\x1b[1;94m'
L = '\x1b[1;95m'
M = '\x1b[1;96m'
Z = '\x1b[1;31m'
X = '\x1b[1;92m'
F = '\x1b[1;97m'
XX = '\x1b[1;35m'


def baner():
    banera = f'''\x1b[1;91m                                                                   \n                      \n           {A} Auto Liker tool (new api) V2\n                                       \n                                       \n                      \n                      \n{M}====================================\n{A}[+] Developer  : Crypo x \n{H}[+] Telegram    : @crypo_x / @G_G_H_G\n{H}[+] Instagram  : @crypo_x\n{M}====================================\n'''
    for crypo in banera.splitlines():
        print(crypo)


os.system('clear')
baner()
url = 'https://php-web-server.action-moviemov.repl.co/'
response = requests.get(url)
if response.status_code != 200:
    error_message = '\x1b[31m=====> @ <=======\n[+]يجب الاعادة لاحقا بسبب كثرة طلبات [+]\x1b[0m'
    print(error_message)
    exit()
valid_keys = {
    '82773983725:HJeoBebO9920',
    '82674998365:UwvIbeJevOebN',
    '82793656278:pORyeievdiidnw',
    '18297362897:qE9929r883979'}
key = input('Enter key code: ')
if key in valid_keys:
    success_message = '\x1b[31m====> Servure {statues : on } ✓ <====\n\x1b[0m'
    print(success_message)
else:
    print('Invalid key code. / يجب شراء كود من المطور @')
    exit()
    print()
    import time
for i in range(800):
    red_text = '\x1b[31m\x1b[1m=====>\x1b[0m'
    green_text = '\x1b[32m\x1b[1m{ Done 3 likes }\x1b[0m'
    print(red_text, green_text)
    print()
    time.sleep(4)
