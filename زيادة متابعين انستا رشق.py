import requests
import random
R = "\033[1;31m"
G = "\033[1;32m"
import webbrowser
webbrowser.open('https://t.me/jalal3_4')
print(R+'''
           Followers ✅
/---------------🇾🇪------------------\\

STEVEN AL GADAR
٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭
ـــــــــــــــــــــــــــــــــــــــــــــــــــــ
تغيرك للمصدر دليل علي فشلك
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــ

❖❖❖❖❖❖❖❖❖❖❖
STEVEN: https://t.me/stevenalgadar

◈◈◈◈◈◈◈◈◈◈◈
\----------------🇾🇪-----------------/
                                         ''')
def Folowers():
    username = input('[+]Username :')
    print("")
    list = 'qwertyuiopasdfghjklzxcvbnm'
    eml = ''.join(random.choice(list) for i in range(6))
    email = f'{eml}@gmail.com'
    url = 'https://core.poprey.com/api/create_test_order_v2.php'
    headers = {
    'accept': 'application/json, text/plain, */*',
   # 'accept-encoding': 'gzip, deflate,EDISONpy
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-length': '109',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://poprey.com',
    'referer': 'https://poprey.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',#EDISONpy
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'x-auth-token': 'null',
    'x-target-lang': 'en'
    }
    data = {
    'service': 'Followers',
    'email': email,
    'username': username,
    'system': 'Instagram',
    'count': '10',
    'type': 't1',
    'csrf':''
    }
    req = requests.post(url,headers=headers,data=data)
    js = req.json()
    if js["text"] == "Please, open your profile and try again. Thank you.":
    	print("Please, open your profile and try again. Thank you.")
    elif js["text"] == "Please, enter the correct username and try again. Thank you.":
    	print("Please, enter the correct username and try again. Thank you.")
    elif js["result"] == "Error":
        print("[-]Not completed 24 hours, come back later.")
    elif js["result"] == "Ok":
        print(G+"[+]Soon you will get your 10 free Followers, come back tomorrow to get new Followers.")
Folowers()
