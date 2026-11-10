import requests,time,pyfiglet

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض

lo = pyfiglet.figlet_format(' H S O')
print(Y+lo)
print('\n')
print(Z+' * '*20)

token = input(B+'ENTER TOKEN : ')
print('\n')
ID = input(B+' ENTER ID : ')
print('\n')
user = input(X+ 'user name : ')
print('\n')

print(F+'*'*60)
api = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
rr=requests.get(api).json()

nam = str(rr['graphql']['user']['full_name'])
iddd = str(rr['graphql']['user']['id'])
fol = str(rr['graphql']['user']['edge_followed_by']['count'])
fols =str(rr['graphql']['user']['edge_follow']['count'])
isp = str(rr['graphql']['user']['is_private'])
bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
ree = re.json()
dat = ree['date']
lo = (f'''
{F}

name : » {nam}
user :  » {user}
fols :  » {fols}
folo :  » {fol}
date : » {dat}
post : » {bio}
ID   : » {iddd}
''')
print(lo)
print(' تم جلب معلومات حسابك الانستكرام')
tlg =(f"""
𖤍 تم جلب معلومات حسابك الانستكرام  𖤍
---------------------------------------------------• ➤
اسم الحساب » {nam}
يوزر الحساب » @{user}
اليتابعهم » {fols}
المتابعين » {fol}
تاريخ الحساب » {dat}
الايدي » {iddd}
منشورات الحساب» {bio}
رابط الخاص بالحساب » https://www.instagram.com/{user}
---------------------------------------------------• ➤
@PY_87 @llxxx3""")
print(Y+'='*60)
requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))