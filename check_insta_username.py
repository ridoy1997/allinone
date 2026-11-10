#-----------المكاتب-------------#
from user_agent import generate_user_agent
import requests
import random
import colorama
import time
from time import sleep
import os
#---------------------------------#

#------الالوان----------------------#
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
#----------------------------------------#

#--------------ربـــاعــي---------------#
def rb():
    e = ['_','.']
    kw = "x0oc"
    al = "zxcvbnmlkjhgfdsaqwertyuiop"
    se = "1234567890"
    while True:
        xo = str("".join(random.choice(kw)for i in range(4)))
        ox = str("".join(random.choice(al)for i in range(4)))
        xox = str("".join(random.choice(kw)for i in range(2)))
        oxo = str("".join(random.choice(kw)for i in range(2)))
        use = str("".join(random.choice(al)for i in range(1)))
        usez = str("".join(random.choice(e)for i in range(1))) 
        gs = str("".join(random.choice(se)for i in range(1))) 
        ano = str("".join(random.choice(kw)for i in range(1)))
        o = xox+oxo
        v = oxo+xox
        j = use+usez+gs+ano
        l = ano+gs+usez+ano
        q = use+ano+usez+gs
        r = oxo+usez+ano
        s = oxo+gs+ano
        x = ano+gs+oxo
        w = gs+use+oxo
        kn = [o,v,j,l,q,xo,ox,r,s,x,w]
        user = random.choice(kn)
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        req =requests.get(f'https://www.instagram.com/{user}', headers=headers).status_code
        if req == 404:
                print(BGreen+user)
                tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={iD}&text=
𝐇𝐈 𝐍𝐄𝐖 𝐔𝐒𝐄𝐑 

𝐔𝐒𝐄𝐑 : {user}

𝐁𝐘 : @IlIlI_x
𝐂𝐇 : @kHaTaRch ''')
                i = requests.post(tlg)
        else:
            print(BRed+user)
            
#----------شبه رباعي-----------#

def rb_b():
    e = ['_','.']
    kw = "x0oc"
    al = "zxcvbnmlkjhgfdsaqwertyuiop"
    se = "1234567890"
    while True:
        xo = str("".join(random.choice(kw)for i in range(3)))
        ox = str("".join(random.choice(al)for i in range(3)))
        xox = str("".join(random.choice(kw)for i in range(2)))
        oxo = str("".join(random.choice(kw)for i in range(2)))
        use = str("".join(random.choice(al)for i in range(1)))
        usez = str("".join(random.choice(e)for i in range(1))) 
        gs = str("".join(random.choice(se)for i in range(1))) 
        ano = str("".join(random.choice(kw)for i in range(1)))
        a = xox+usez+xox
        b = oxo+usez+xox
        c = xox+gs+use
        d =oxo+gs+use
        e = xo+usez+ano
        f = ox+usez+ano
        g = ano+usez+xo
        h = ano+usez+ox
        i = ano+gs+usez+xo
        j = ano+gs+usez+ox
        k= xo+usez+gs+ano
        l= ox+usez+gs+ano
        
        
        kn = [a,b,c,d,e,f,g,h,i,j,k,l]
        user = random.choice(kn)
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        req =requests.get(f'https://www.instagram.com/{user}', headers=headers).status_code
        if req == 404:
                print(BGreen+user)
                tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={iD}&text=
𝐇𝐈 𝐍𝐄𝐖 𝐔𝐒𝐄𝐑 

𝐔𝐒𝐄𝐑 : {user}

𝐁𝐘 : @IlIlI_x
𝐂𝐇 : @kHaTaRch ''')
                i = requests.post(tlg)
        else:
            print(BRed+user)
            
#----------خماسي----------#

def rb_bb():
    e = ['_','.']
    kw = "x0oc"
    al = "zxcvbnmlkjhgfdsaqwertyuiop"
    se = "1234567890"
    while True:
        xo = str("".join(random.choice(kw)for i in range(3)))
        ox = str("".join(random.choice(al)for i in range(3)))
        xox = str("".join(random.choice(kw)for i in range(2)))
        oxo = str("".join(random.choice(kw)for i in range(2)))
        use = str("".join(random.choice(al)for i in range(1)))
        usez = str("".join(random.choice(e)for i in range(1))) 
        gs = str("".join(random.choice(se)for i in range(1))) 
        ano = str("".join(random.choice(kw)for i in range(1)))
        a = xox+usez+xox
        b = oxo+usez+xox
        c = xox+gs+use+use
        d =oxo+gs+use+ano7
        e = xo+usez+ano
        f = ox+usez+ano
        g = ano+usez+xo
        h = ano+usez+ox+use
        i = ano+xo+ano
        j = ano+gs+ox
        k= xo+ano+ano
        l= ox+ano+use
        
        
        kn = [a,b,c,d,e,f,g,h,i,j,k,l]
        user = random.choice(kn)
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        req =requests.get(f'https://www.instagram.com/{user}', headers=headers).status_code
        if req == 404:
                print(BGreen+user)
                tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={iD}&text=
𝐇𝐈 𝐍𝐄𝐖 𝐔𝐒𝐄𝐑 

𝐔𝐒𝐄𝐑 : {user}

𝐁𝐘 : @IlIlI_x
𝐂𝐇 : @kHaTaRch ''')
                i = requests.post(tlg)
        else:
            print(BRed+user)
print('- ENTER TOKEN : ')
token = input(' ')
print('-ENTER iD : ')
iD = input('')
sleep(1.5)
os.system('clear')
print('''
ربـــــــاعــــي[1]
 شـبــه رباعـي[2]
 خــمـــاســـي[3]
''')
n = input(' ')
if n == '1':
    rb()
elif n == '2':
    rb_b()
elif n == '3':
    rb_bb()
else:
    print(BRed+'اخـتـيار خـطـأ')                                            