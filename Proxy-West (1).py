import smtplib
import requests
import threading
import random
import os
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet
os.system("clear")
print(pyfiglet.figlet_format("WestTekno"))
print("""Telegram: @WestTekno
Coder: @proyw

""")
file=input("Combo File: ")
print("Stared...")
def chk(proxy):
    proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
    }
    try:
        requests.get("https://google.com/", proxies=proxies,timeout=3)
        print(f"Hit [=] {proxy}")
        q= open("/sdcard/west-proxy",'a+')
        q.write(proxy+'\n')
    except:
        print("Die: "+proxy)
total=open(file,'r').readlines()
uz=len(total)
def c1():
    for west in range(0,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c2():
    for west in range(1,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c3():
    for west in range(2,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c4():
    for west in range(3,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c5():
    for west in range(4,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c6():
    for west in range(5,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c7():
    for west in range(6,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c8():
    for west in range(7,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c9():
    for west in range(8,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
def c10():
    for west in range(9,uz,10):
        up=total[west].split(' ')[0]
        mp=up.replace("\n","")
        chk(mp)
a1 = threading.Thread(target=c1)
a2 = threading.Thread(target=c2)
a3= threading.Thread(target=c3)
a4= threading.Thread(target=c4)
a5= threading.Thread(target=c5) 
a6= threading.Thread(target=c6) 
a7 = threading.Thread(target=c7)
a8 = threading.Thread(target=c8)
a9= threading.Thread(target=c9)
a10= threading.Thread(target=c10)
a1.start() 
a2.start() 
a3.start() 
a4.start() 
a5.start() 
a6.start()
a7.start() 
a8.start() 
a9.start() 
a10.start() 
