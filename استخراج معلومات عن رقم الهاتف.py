import requests 
from bs4 import BeautifulSoup
import re , json 
from pyfiglet import Figlet
import colorama


q = '\033[1;30m'
w = '\033[1;31m'
e = '\033[1;32m'
r = '\033[1;33m'
t = '\033[1;34m'
y = '\033[1;35m'
u = '\033[1;36m'
i = '\033[1;37m'

o = '\033[2;30m'
p = '\033[2;31m'
a = '\033[2;32m'
s = '\033[2;33m'
d = '\033[2;34m'
f = '\033[2;35m'
g = '\033[2;36m'
h = '\033[2;37m'

j = '\033[3;30m'
k = '\033[3;31m'
l = '\033[3;32m'
z = '\033[3;33m'
x = '\033[3;34m'
c = '\033[3;35m'
v = '\033[3;36m'
b = '\033[3;37m'

ll = '\033[4;30m'#رصاصي تحتها خط
rr = '\033[4;31m'#احمر جديد تحتها خط
gg = '\033[4;32m'#اخضر جديدة تحتها خط
yy = '\033[4;33m'#اصفر جديدة تحتها خط
bb = '\033[4;34m' #ازرق جديدة تحتها خط
pp = '\033[4;35m' #بنفسجي جديدة تحتها خط
mm = '\033[4;36m' #سمائي جديدة تحتها خط
aa = '\033[4;37m' #ابيض جديدة تحتها خط

lll = '\033[7;100m'#رصاصي جديدة
rrr = '\033[7;101m'#احمر جديد
ggg = '\033[7;102m'#اخضر جديدة
yyy = '\033[7;103m'#اصفر جديدة
bbb = '\033[7;104m' #ازرق جديدة
ppp = '\033[7;105m' #بنفسجي جديدة
mmm = '\033[7;106m' #سمائي جديدة
aaa = '\033[7;107m' #ابيض جديدة

llll = '\033[8;100m'#لون رصاصي تغطية كلمات
rrrr = '\033[8;101m'#احمر جديد تغطية كلمات
gggg = '\033[8;102m'#اخضر جديدة تغطية كيمات
yyyy = '\033[8;103m'#اصفر جديدة تغطية كامات
bbbb = '\033[8;104m' #ازرق جديدة تغطية كلمات
pppp = '\033[8;105m' #بنفسجي جديدة تغطية كلمات
mmmm = '\033[8;106m' #سمائي جديدة تغطية كلمات
aaaa = '\033[8;107m' #ابيض جديدة تغطية كلمات

lllll = '\033[11;100m'#رصاصي جديد للتشفير
rrrrr = '\033[11;101m'#احمر جديد للتشفير
ggggg = '\033[11;102m'#اخضر جديد للتشفير
yyyyy = '\033[11;103m'#اصفر جديد للتشفير
bbbbb = '\033[11;104m' #ازرق جديد للتشفير
ppppp = '\033[11;105m' #بنفسجي جديد للتشفير
mmmmm = '\033[11;106m' #سمائي جديد للتشفير
aaaaa = '\033[11;107m' #ابيض جديد للتشفير

llllll = '\033[30;100m'#رصاصي ورصاصي
rrrrrr = '\033[30;101m'#احمر ورصاصي
gggggg = '\033[30;102m'#اخضر ورصاصي
yyyyyy = '\033[30;103m'#اصفر ورصاصي
bbbbbb = '\033[30;104m' #ازرق ورصاصي
pppppp = '\033[30;105m' #بنفسجي ورصاصي
mmmmmm = '\033[30;106m' #سمائي ورصاصي
aaaaaa = '\033[30;107m' #ابيض ورصاصي

lllllll = '\033[31;100m'#رصاصي واحمر
rrrrrrr = '\033[31;101m'#احمر واحمر
ggggggg = '\033[31;102m'#اخضر واحمر
yyyyyyy = '\033[31;103m'#اصفر واحمر
bbbbbbb = '\033[31;104m' #ازرق واحمر
ppppppp = '\033[31;105m' #بنفسجي واحمر
mmmmmmm= '\033[31;106m' #سمائي واحمر
aaaaaaa = '\033[31;107m' #ابيض واحمر

llllllll = '\033[32;100m'#رصاصي واخضر
rrrrrrrr = '\033[32;101m'#احمر واخضر
gggggggg = '\033[32;102m'#اخضر واخضر
yyyyyyyy = '\033[32;103m'#اصفر واخضر
bbbbbbbb = '\033[32;104m' #ازرق واخضر
pppppppp = '\033[32;105m' #بنفسجي واخضر
mmmmmmmm = '\033[32;106m' #سمائي واخضر
aaaaaaaa = '\033[32;107m' #ابيض واخضر

lllllllll = '\033[33;100m'#رصاصي واصفر
rrrrrrrrr = '\033[33;101m'#احمر واصفر
ggggggggg = '\033[33;102m'#اخضر واصفر
yyyyyyyyy = '\033[33;103m'#اصفر واصفر
bbbbbbbbb = '\033[33;104m' #ازرق واصفر
ppppppppp = '\033[33;105m' #بنفسجي واصفر
mmmmmmmmm = '\033[33;106m' #سمائي واصفر
aaaaaaaaa = '\033[33;107m' #ابيض واصفر

llllllllll = '\033[34;100m'#رصاصي وازرق
rrrrrrrrrr = '\033[34;101m'#احمر وازرق
gggggggggg = '\033[34;102m'#اخضر وازرق
yyyyyyyyyy = '\033[34;103m'#اصفر وازرق
bbbbbbbbbb = '\033[34;104m' #ازرق وازرق
pppppppppp = '\033[34;105m' #بنفسجي وازرق
mmmmmmmmmm = '\033[34;106m' #سمائي وازرق
aaaaaaaaaa = '\033[34;107m' #ابيض وازرق

la = '\033[35;100m'#رصاصي وبنفسجي
ra = '\033[35;101m'#احمر وبنفسجي
ga = '\033[35;102m'#اخضر وبنفسجي
ya = '\033[35;103m'#اصفر وبنفسجي
ba = '\033[35;104m' #ازرق وبنفسجي
pa = '\033[35;105m' #بنفسجي وبنفسجي
ma = '\033[35;106m' #سمائي وبنفسجي
am = '\033[35;107m' #ابيض وبنفسجي

laa = '\033[36;100m'#رصاصي وسمائي
raa = '\033[36;101m'#احمر وسمائي
gaa = '\033[36;102m'#اخضر وسمائي
yaa = '\033[36;103m'#اصفر وسمائي
baa = '\033[36;104m' #ازرق وسمائي
paa = '\033[36;105m' #بنفسجي وسمائي
maa = '\033[36;106m' #سمائي وسمائي
amm = '\033[36;107m' #ابيض وسمائي

laaa = '\033[37;100m'#رصاصي وابيض
raaa = '\033[37;101m'#احمر وابيض
gaaa = '\033[37;102m'#اخضر وابيض
yaaa = '\033[37;103m'#اصفر وابيض
baaa = '\033[37;104m' #ازرق وابيض
paaa = '\033[37;105m' #بنفسجي وابيض
maaa = '\033[37;106m' #سمائي وابيض
ammm = '\033[37;107m' #ابيض وابيض

laaaa = '\033[90;100m'#رصاصي ورصاصي
raaaa = '\033[90;101m'#احمر ورصاصي
gaaaa = '\033[90;102m'#اخضر ورصاصي
yaaaa = '\033[90;103m'#اصفر ورصاصي
baaaa = '\033[90;104m' #ازرق ورصاصي
paaaa = '\033[90;105m' #بنفسجي ورصاصي
maaaa = '\033[90;106m' #سمائي ورصاصي
ammmm = '\033[90;107m' #ابيض ورصاصي

laaaaa = '\033[91;100m'#رصاصي واحمر
raaaaa = '\033[91;101m'#احمر واحمر
gaaaaa = '\033[91;102m'#اخضر واحمر
yaaaaaa = '\033[91;103m'#اصفر واحمر
baaaaa = '\033[91;104m' #ازرق واحمر
paaaaa = '\033[91;105m' #بنفسجي واحمر
maaaaa = '\033[91;106m' #سمائي واحمر
ammmmm = '\033[91;107m' #ابيض واحمر

laaaaaa = '\033[92;100m'#رصاصي واخضر
raaaaaa = '\033[92;101m'#احمر واخضر
gaaaaaa = '\033[92;102m'#اخضر واخضر
yaaaaaa = '\033[92;103m'#اصفر واخضر
baaaaaa = '\033[92;104m' #ازرق واخضر
paaaaaa = '\033[92;105m' #بنفسجي واخضر
maaaaaa = '\033[92;106m' #سمائي واخضر
ammmmmm= '\033[92;107m' #ابيض واخضر

laaaaaaa = '\033[93;100m'#رصاصي واصفر
raaaaaaa = '\033[93;101m'#احمر واصفر
gaaaaaaa = '\033[93;102m'#اخضر واصفر
yaaaaaaa = '\033[93;103m'#اصفر واصفر
baaaaaaa = '\033[93;104m' #ازرق واصفر
paaaaaaa = '\033[93;105m' #بنفسجي واصفر
maaaaaaa = '\033[93;106m' #سمائي واصفر
ammmmmmm = '\033[93;107m' #ابيض واصفر

lu = '\033[94;100m'#رصاصي وازرق
ru = '\033[94;101m'#احمر وازرق
gu = '\033[94;102m'#اخضر وازرق
tu = '\033[94;103m'#اصفر وازرق
bu = '\033[94;104m' #ازرق وازرق
pu = '\033[94;105m' #بنفسجي وازرق
mu = '\033[94;106m' #سمائي وازرق
au = '\033[94;107m' #ابيض وازرق

luu = '\033[95;100m'#رصاصي وبنفسجي
ruu = '\033[95;101m'#احمر وبنفسجي
guu = '\033[95;102m'#اخضر وبنفسجي
yuu = '\033[95;103m'#اصفر وبنفسجي
buu = '\033[95;104m' #ازرق وبنفسجي
puu = '\033[95;105m' #بنفسجي وبنفسجي
muu = '\033[95;106m' #سمائي وبنفسجي
auu = '\033[95;107m' #ابيض وبنفسجي

luuu = '\033[96;100m'#رصاصي وسمائي
ruuu = '\033[96;101m'#احمر وسمائي
guuu = '\033[96;102m'#اخضر وسمائي
yuuu = '\033[96;103m'#اصفر وسمائي
buuu = '\033[96;104m' #ازرق وسمائي
puuu = '\033[96;105m' #بنفسجي وسمائي
muuu = '\033[96;106m' #سمائي وسمائي
auuu = '\033[96;107m' #ابيض وسمائي

luuuu = '\033[97;100m'#رصاصي وابيض
ruuuu = '\033[97;101m'#احمر وابيض
guuuu = '\033[97;102m'#اخضر وابيض
yuuuu = '\033[97;103m'#اصفر وابيض
buuuu = '\033[97;104m' #ازرق وابيض
puuuu = '\033[97;105m' #بنفسجي وابيض
muuuu = '\033[97;106m' #سمائي وابيض
auuuu = '\033[97;107m' #ابيض وابيض


cv = colorama.Fore.WHITE
rd = colorama.Fore.RED
bl = colorama.Fore.BLUE
mag = colorama.Fore.MAGENTA
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
gbl = colorama.Fore.LIGHTBLUE_EX

def get_info_phone(koso , operators):
    with requests.Session() as session:
        phone = requests.utils.quote(koso)
        url =f"https://www.phonenumbertrack.com/phone-number-track-trace-result?country=&phone={phone}&submit=#QueryResult"
        req = session.get(url).text
        soup = BeautifulSoup(req , "html.parser")
        kos = soup.find("tbody").text
        koon = soup.find("div" , class_="row panel panel-default details").text
        if "Operator" in kos:
            return (koon.replace("International Call Prefix" , "International Call Prefix : ").replace("Country Code" , "\nCountry Code : +").replace("(ایران)" , " or Iran ").replace("Area Code" , "\nArea Code : ").replace("Subscriber’s Number" , "\nSubscriber’s Number:") + "\n==========================\n" + kos.replace("Query" , "Query : ").replace("Country " , "\nCountry : ").replace("Phone Type" , "\nPhone Type : ").replace("Area Code" , "\nArea Code ").replace("Advertising & Sponsored links","").replace("Location","\nLocation : ").replace("More Options Check Phone Number" , "").replace("Operator" , "\nOperator : "))
        else:
            return (koon.replace("International Call Prefix" , "International Call Prefix : ").replace("Country Code" , "\nCountry Code : +").replace("(ایران)" , " or Iran ").replace("Area Code" , "\nArea Code : ").replace("Subscriber’s Number" , "\nSubscriber’s Number:") + "\n==========================\n" + kos.replace("Query" , "Query : ").replace("Country " , "\nCountry : ").replace("Phone Type" , "\nPhone Type : ").replace("Area Code" , "\nArea Code ").replace("Advertising & Sponsored links","").replace("Location","\nLocation : ") + "\nKnown Provider : %s" % (operators))
def operator(number):
    site = "https://www.celltrack.eu/site/trace"    
    payload = {"_csrf":"J-sER_hYlIW2sj9tpjqyeYmDECR07hsR58zHHm5ILYNGpmIdnHXmvdrXd1n8d8A__9kiYw2bQUag_otXA2Vdsg==","use-alt.flow":"1","TrackForm[phone]":number}
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" , "Cookie" :'lang=en; currentCountry=IR; PHPSESSID=fd20137eacfb20b8da0da15cbd7e95cc; _csrf=582230097b3f6b91512381fafdc543214e99b0fb2d120410461a1105b7fda7c0a:2:{i:0;s:5:"_csrf";i:1;s:32:"aMfZd-r8leH4ZMrFvZ2GyuZWG2LIm-p1";}; _gid=GA1.2.2128828554.1658496315; _gaexp=GAX1.2.R26ZEKfQQy-7-ZdDfEyqnQ.19257.1; _gcl_au=1.1.562173569.1658496316; _gat_UA-114079383-1=1; _ga_81BBDDRXGL=GS1.1.1658496316.1.0.1658496316.0; _ga=GA1.1.346672535.1658496315'}

    req = requests.post(site , headers=headers , data=payload)
    soup = BeautifulSoup(req.text , "html.parser")
    final =  soup.find_all("tbody")[1].find_all("tr")[1].find_all("td")[1].text

    return final.replace(" " , "").replace("\n" , "")

def logo():
    return Figlet(font="slant").renderText("M A H D I")

print (gbl + "\t" + logo())
number = input(rd + "TELE : @DD_1_1_1\nاكتب رقـﻢ موبايل مـ&ـﻊ رمز الدولة ولاتنسة تكتب +قًبل رمز دولة  مثلا هيجي" + bl + "+96477245345678\n- >  " + gn )


print (yl + get_info_phone(number , operator(number) + cv))
#حقوق المطور مـٰهوُدِي  تخمط اذكر المصدر
#اداه سهلة الغاية منها التعلم وتدريب وليس السرقة

#قناتي @iuron0
#معرف حسابي @DD_1_1_1