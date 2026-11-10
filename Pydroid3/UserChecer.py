import requests as reback
import re as trakos
# Trakos ALways Best 
def check():
    d = 0
    f = 0
    try:
        file = input(f"[?] Enter File Name :")
        trakoss = open(f"{file}","r+").readlines()
        for user in trakoss:
            userr = user.strip()

            r = reback.get(f"https://t.me/{userr}").text
            find = (trakos.findall(f'<meta property="twitter:title" content="(.*?)">',r)[0])
            findd = f"{find}"
            if "Telegram: Contact" in findd:
                d+=1
                with open(f"done.txt","a")as t:
                    t.write(f"{userr}\n")
                t.close()
            else:
                f+=1
                print(f"\r[+] Not Banned | {f} | Banned | {d}",end="")
        print(f"\n\n[%] Done Check All List Results: \n\n- Banned : {d} .\n- Not Banned : {f}\n\n-- @trprogram")
    except FileNotFoundError:
        print("[!!] Error File Name!")
check()