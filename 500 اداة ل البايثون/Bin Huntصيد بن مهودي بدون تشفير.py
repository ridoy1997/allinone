import os
import random
import requests
import colorama
from colorama import init, Fore
import time
from time import sleep
# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
l = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =

colorama.init() 

def logo():
    print(f'''{X}« {C}Tech Phantom{F}⸙ {X}»
    {B}┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{B}┓
    {Z}┃ {F}⌯ {C}Developer     {F}›{C} @HHWHHHH  {Z}┃
    {Z}┃ {F}⌯ {C}GitHub  {F}      ›{C} @kaito-bs  {Z}┃
    {Z}┃ {F}⌯ {C}Channel       {F}›{C} @wxww3  {Z}   ┃
    {B}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{B}┛ ''')
def tool():
    g = 0
    b = 0
    all = -1
    logo()
    id =input(f'{X}𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘐𝘋:')
    token =input(f'{C}𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘛𝘖𝘒𝘌𝘕:')
    sleep(1)
    sleep(0.1)
    while True:
        api = 'https://kabospythonanywhere.nhnh7.repl.co/Bin/Checker/'
        all += 1
        req =requests.get(api).json()
        bin = req['Bin']
        Country = req['Country']
        Stat = req['Status']
        if Stat == True:
            #print(f'''New Bin IS HUNTED
#{F}Status:{Stat}\n{C}ʙɪɴ:{bin}\n{l}𝖼𝗈𝗎𝗇𝗍𝗋ʏ:{Country}\n''')
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''\r                 \n{F}Good Bin : {g}
{Z}Bad Bin : {b}
{C}Number : {all}
{C}@HHWHHHH CH : @wxww3''')
            g += 1
            tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= 
ʙɪɴ:{bin}
𝖼𝗈𝗎𝗇𝗍𝗋ʏ:{Country}
BY : @HHWHHHH CH : @wxww3
    ''')
    
            e = requests.post(tlg)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            print(f'''\r                 \n{F}Good Bin : {g}
{Z}Bad Bin : {b}
{C}Number : {all}
{C}@HHWHHHH CH : @wxww3''')
            b += 1
            #print(f'{Z}Wrong Bin\n {C}ʙɪɴ:{bin}\n')


tool()

