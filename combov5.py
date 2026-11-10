import os
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import sys
except:
    os.system('pip install sys')

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
    pass
try :
    import telebot
except :
    os.system('pip install telebot')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        import pyfiglet, os,sys
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
import telebot
import requests
import random
from requests import get
from time import sleep
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
from gdolib import *
def id_fromflw():
	os.system("clear")
	logo()
	session = input ('\t'+C+'['+R+'+'+C+']'+Y+' Your SessionID :'+W)
	user = input ('\t'+C+'['+R+'+'+C+']'+Y+' User Target To Get Ids :'+W)
	id = input ('\t'+C+'['+R+'+'+C+']'+Y+' ID Target To Get IDs  :'+W)
	get = gdo_drow.get_ids_followers(session,user,id)
	if get['status']=='Success':
	   for id in get['id']:
	      print(id)
	      open("id.txt", "a").write(str(id) + "\n")
	else:
	   print(R+'• BaD Login or Not Found UserName .')
def logo():
    print(f'{G}-{R}-'*29)	
    print(P+"""_________               ___.           
\_   ___ \  ____   _____\_ |__   ____  
/    \  \/ /  _ \ /     \| __ \ /  _ \ 
\     \___(  <_> )  Y Y  \ \_\ (  <_> )
 \______  /\____/|__|_|  /___  /\____/ 
        \/             \/    \/        """)
    print(f'{G}-{R}-'*29)
    print ('\t'+Y+'['+P+'*'+Y+']'+C+'Code By :'+W+' Bʅαƈƙ Bιɾԃ 🇩🇿ᵁᴬᴾ™')
    print ('\t'+Y+'['+P+'*'+Y+']'+C+'Channel :'+W+' @XM0XX')
    print(f'{G}-{R}-'*29)
def combonum(cod,net,ID,token):
    d=0
    while True :
        num='1234567890'
        d+=1
        h = str("".join(random.choice(num)for numy in range(8)))
        user = (cod+h)
        password=('0'+net+h)
        open("numnum.txt", "a").write(str(user+':'+password) + "\n")
        p=(9999)
        print (G+f'[{d}]~done')
        if p == d:
            break
    requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption= • Done Save Combo\n\n• Tel :@XM1XX\n• Channel :@XM0XX",
            files={"document": open("numnum.txt", "rb")},
        )
def combomailpass(domin,ID,token ):
	d=0
	while True :
	       name_dead1=['Ada','Adriano','Afro','Agata' ,'Alberto','Alessandra','Alessandro','Alessia' ,'Alessio', 'Alfredo' ,'Alice', 'Allegra', 'Alma' ,'Amabel','Gabriel','Lucas','Matheus','Guilherme','Bruno','Rafael','Felipe','Thiago','Pedro','Carlos','rex','fred','jon','rosa','rimi','toni','niko','salah','jamal','lxml','James','Robert','John','Michael','David','William','Richard','Joseph','Thomas','Charles','Christopher','Daniel','Matthew','Anthony','Anthony','Mark','Donald','Steven','Paul','Andrew','Joshua','Kenneth','Kevin','Brian','George','Timothy','Ronald','Edward','Jason','Jeffrey','Ryan','Jacob','Gary','ahmed','naser','yousef','reda','mohamed','salah']
	       num_dead='1234567890'
	       email1=str("".join(random.choice(name_dead1)for i in range(1)))
	       email0=str("".join(random.choice(num_dead)for i in range(3)))
	       pass1=str("".join(random.choice(name_dead1)for i in range(1)))
	       pass2=str("".join(random.choice(num_dead)for i in range(3)))
	       passe=pass1+pass2
	       ran=email1+email0
	       ran = ran+'@'+domin
	       d+=1
	       open("email.txt", "a").write(str(ran+':'+passe) + "\n")
	       p=(9999)
	       print (G+f'[{d}]~done')
	       if p == d:
	           break
	           requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption= • Done Save Combo\n\n• Tel :@XM1XX\n• Channel :@XM0XX",
	           files={"document": open("email.txt", "rb")},
        )	
def comboemail(domin,ID,token):
    d=0
    while True :
        name_dead=['Ada','Adriano','Afro','Agata' ,'Alberto','Alessandra','Alessandro','Alessia' ,'Alessio', 'Alfredo' ,'Alice', 'Allegra', 'Alma' ,'Amabel','Gabriel','Lucas','Matheus','Guilherme','Bruno','Rafael','Felipe','Thiago','Pedro','Carlos','rex','fred','jon','rosa','rimi','toni','niko','salah','jamal','lxml','James','Robert','John','Michael','David','William','Richard','Joseph','Thomas','Charles','Christopher','Daniel','Matthew','Anthony','Anthony','Mark','Donald','Steven','Paul','Andrew','Joshua','Kenneth','Kevin','Brian','George','Timothy','Ronald','Edward','Jason','Jeffrey','Ryan','Jacob','Gary','ahmed','naser','yousef','reda','mohamed','salah']
        num_dead='1234567890'
        email1=str("".join(random.choice(name_dead)for i in range(1)))
        email0=str("".join(random.choice(num_dead)for i in range(3)))
        ran=email1+email0
        ran = ran+'@'+domin
        d+=1
        open("email.txt", "a").write(str(ran) + "\n")
        p=(9999)
        print (G+f'[{d}]~done')
        if p == d:
            break
            requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption= • Done Save Combo\n\n• Tel :@XM1XX\n• Channel :@XM0XX",
            files={"document": open("email.txt", "rb")},
        )
def id():
    import random
    de='1234567890'
    d=0
    while True :
        id=str("".join(random.choice(de)for i in range(10)))
        open("id.txt", "a").write(str(id) + "\n")
        d+=1
        p=(9999)
        print (G+f'[{d}]~done')
        if p == d:
            break
            requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption= • Done Save Combo\n\n• Tel :@XM1XX\n• Channel :@XM0XX",
                files={"document": open("id.txt", "rb")},
            )
logo()
ID=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet Id :'+ W)
token=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet Token :'+W)
os.system('clear')
logo()
print ('\t'+P+'['+Y+'1'+P+']'+Bl+'make num combo ')
print ('\t'+P+'['+Y+'2'+P+']'+Bl+'make email combo ' )
print ('\t'+P+'['+Y+'3'+P+']'+Bl+'make instgram id combo  ' )
print ('\t'+P+'['+Y+'4'+P+']'+Bl+'make email:pass combo ')
print ('\t'+P+'['+Y+'5'+P+']'+Bl+'make combo Ids  From Followers ')
choo=input ('\t'+P+'['+Y+'?'+P+']'+Bl+'Enter Your choise : ')
if choo=='5':
	id_fromflw()
if choo=='4':
	domin=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet Domin :'+W)
	combomailpass(domin,ID,token )
if choo=='3':
    id()
if choo=='1':
    cod=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet Contury Code :'+W)
    net=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet net :'+W)
    combonum(cod,net,ID,token)
if choo=='2':
    domin=input ('\t'+C+'['+R+'+'+C+']'+Y+' Entet Domin :'+W)
    comboemail(domin,ID,token)    