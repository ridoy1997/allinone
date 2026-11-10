# Decoded by marshal-magic
# Follow us on telegram @psh_team
from user_agent import generate_user_agent
import datetime
import threading
import json
import random
import requests
copyright = '@psh_team'
X = '\x1b[4;33m'
F = '\x1b[2;32m'
Z = '\x1b[4;31m'
L = '\x1b[4;35m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
A = '\x1b[4;31m'
url12 = requests.get('https://pastebin.com/raw/aZMdkMzB').text
if '1' in url12:
    I = input(f'''{A}ENTAR ID : {X}''')
    T = input(f'''{A}ENTAR Token : {X}''')

    def fs():
        countr = [
            'KW',
            'SA',
            'IN',
            'EG',
            'IR',
            'YE',
            'IQ']
        country = random.choice(countr)
        country1 = random.choice(countr)
        if country == 'KW':
            num = 30
        elif country == 'IQ':
            num = 10
        elif country == 'SA':
            num = 15
        elif country == 'IN':
            num = 22
        elif country == 'EG':
            num = 32
        elif country == 'IR':
            num = 21
        elif country == 'YE':
            num = 12
        u = f'''https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count={num}&device_id=7166382878086088234&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=2&is_fullscreen=false&is_page_visible=true&language=ar&os=windows&priority_region={country}&referer=&region={country1}&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=V4i0eWl1l4XXNGAUlAfYoNF-N9wq9E8HJ8vL0Vk2d9yR9kE6d8y-NZw7ViWU_jh-ca7dGEQC3DRYLmWvkbkcxagwW8wD20KzqekJ0xn7tF4lHcUfPnsB4rZFTVcHF9gtOZOX2Sgdkm4ITrNp&X-Bogus=DFSzswVYNHvANryXSDbnEcYklTI6&_signature=_02B4Z6wo00001YNx7rgAAIDAXQe2H-Lkar2DceoAAANief'''
        r = requests.get(u).json()
        e = len(str(r['itemList'][0]['author']['secUid']))
    # WARNING: Decompyle incomplete

    prox_list = []
    for i in range(5):
        t = threading.Thread(fs, **('target',))
        t.start()
        prox_list.append(t)
else:

    def hello():
        x = datetime.datetime.now()
        g = datetime.datetime(2023, 2, 28, 0, 0, 0)
        if x > g or x == g:
            print(Z + '\n\n تم ايقاف الاداة.')
            s = '• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n • لتفعيل الادات راسل المطوره .\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •'
            print(F + s)
            print(X + '@J_C_A')
            exit()

    hello()
