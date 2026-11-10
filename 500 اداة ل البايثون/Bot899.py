from faker import Faker
import requests
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
devs = [
5012751368
]
bot = telebot.TeleBot("")#توكن
@bot.message_handler(commands = ["start"])
def Start(message):
 me = message.chat.first_name
 Name = message.chat.first_name
 t2 = message.from_user.username
 iD = message.chat.id
 info = bot.get_chat(message.from_user.id)
 bio = info.bio
 A = types.InlineKeyboardMarkup(row_width=1)
 key = InlineKeyboardMarkup()
 key.row_width = 2
 dev = InlineKeyboardButton(text = "~ Dev »",url ="tg://openmessage?user_id=1325689471")
 B = InlineKeyboardButton(text ="۞︎ معلومات انستا »" ,callback_data="Ig")
 C = InlineKeyboardButton(text ="۞︎ معلومات وهميه »" ,callback_data="Fake")
 D = InlineKeyboardButton(text = "۞︎ تحميل Tik Tok »",callback_data="dtek")
 E = InlineKeyboardButton(text ="۞︎ معلومات ip »" ,callback_data="ipinfo")
 key.add(B,C)
 key.add(dev)
 key.add(D,E)
 bot.reply_to(message, """
اهلا في بوت الخدمات
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Name: `{}`
Id: `{}`
User: @{}
Bio: `{}`
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
اختر مايعجبك من الاسفل
    """.format(Name,iD,t2,bio), parse_mode = "markdown" , reply_markup =key)    
 with open("DB.csv","a") as dc:
    dc.write(f"{Name} | @{t2} | {iD} |{bio}\n")
@bot.callback_query_handler(func= lambda call : True)
def callback_data(call):
  if call.message:
     if call.data == "Ig":
           mm = bot.send_message(call.message.chat.id,"user?")
           bot.register_next_step_handler(mm,get_info)
     if call.data == "Fake":
        Fake_info(call.message)
     if call.data == "dtek":
       tek(call.message)
     if call.data == "ipinfo":
       bot.answer_callback_query(call.id,
		"لست في قائمة الادمنية!")
     if call.data == "480":
       mm = bot.send_message(call.message.chat.id,"Send the link")
       bot.register_next_step_handler(mm,t4)
     if call.data == "720":
       mm = bot.send_message(call.message.chat.id,"Send the link")
       bot.register_next_step_handler(mm,t7)
     if call.data == "1080":
       mm = bot.send_message(call.message.chat.id,"Send the link")
       bot.register_next_step_handler(mm,t10)
     if call.data == "withtek":
       mm = bot.send_message(call.message.chat.id,"Send the link")
       bot.register_next_step_handler(mm,witho)
     if call.data == "audo":
       mm = bot.send_message(call.message.chat.id,"Send the link")
       bot.register_next_step_handler(mm,sot)
     if call.data == "back":
        Name = call.message.chat.first_name
        t2 = call.message.from_user.username
        iD = call.message.chat.id
        info = bot.get_chat(call.message.from_user.id)
        bio = info.bio
        key = InlineKeyboardMarkup()
        key.row_width = 2
        dev = InlineKeyboardButton(text = "~ Dev »",url ="tg://openmessage?user_id=1325689471")
        B = InlineKeyboardButton(text ="۞︎ معلومات انستا »" ,callback_data="Ig")
        C = InlineKeyboardButton(text ="۞︎ معلومات وهميه »" ,callback_data="Fake")
        D = InlineKeyboardButton(text = "۞︎ تحميل Tik Tok »",callback_data="dtek")
        E = InlineKeyboardButton(text ="۞︎ معلومات ip »" ,callback_data="ipinfo")
        key.add(B,C)
        key.add(dev)
        key.add(D,E)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""اهلا   بك مجددًا 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
شكرا لأختيارك خدماتنا مرة اخرى ❤️‍🩹""",parse_mode = "markdown" ,reply_markup =key)
def tek(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   B = InlineKeyboardButton(text ="تحميل بجودة 480 🎞️" ,callback_data="480")
   C = InlineKeyboardButton(text ="تحميل بجودة 720 📽️" ,callback_data="720")
   D = InlineKeyboardButton(text = "تحميل بجودة 1080 🎬",callback_data="1080")
   F = InlineKeyboardButton(text = "تحميل بصيغة mp3 🎧",callback_data="audo")
   E = InlineKeyboardButton(text ="تحميل مع علامة تيك توك ©️" ,callback_data="withtek")
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(B)
   key.add(C)
   key.add(D)
   key.add(E,F)
   key.add(BA)
   bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="""*اختر جودة او صيغه التحميل من الاسفل*""",parse_mode = "markdown" , reply_markup =key)        
def t4(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(BA)
   chat_id = message.chat.id
   link = message.text
   headers = {
			'authority': 'lovetik.com',
			'accept': '*/*',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://lovetik.com',
			'referer': 'https://lovetik.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
   data = {
			'query': link}
   result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
   video = result['links'][3]['a']
   desc = result['desc']
   bot.send_video(chat_id, video=video, caption=desc,reply_markup =key)
def t7(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(BA)
   chat_id = message.chat.id
   link = message.text
   headers = {
			'authority': 'lovetik.com',
			'accept': '*/*',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://lovetik.com',
			'referer': 'https://lovetik.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
   data = {
			'query': link}
   result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
   video = result['links'][2]['a']
   desc = result['desc']
   bot.send_video(chat_id, video=video, caption=desc,reply_markup =key)
def t10(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(BA)
   chat_id = message.chat.id
   link = message.text
   headers = {
			'authority': 'lovetik.com',
			'accept': '*/*',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://lovetik.com',
			'referer': 'https://lovetik.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
   data = {
			'query': link}
   result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
   video = result['links'][1]['a']
   desc = result['desc']
   bot.send_video(chat_id, video=video, caption=desc,reply_markup =key)
def witho(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(BA)
   chat_id = message.chat.id
   link = message.text
   headers = {
			'authority': 'lovetik.com',
			'accept': '*/*',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://lovetik.com',
			'referer': 'https://lovetik.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
   data = {
			'query': link}
   result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
   video = result['links'][4]['a']
   desc = result['desc']
   bot.send_video(chat_id, video=video, caption=desc,reply_markup =key)
def sot(message):
   key = InlineKeyboardMarkup()
   key.row_width = 2
   BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
   key.add(BA)
   chat_id = message.chat.id
   link = message.text
   headers = {
			'authority': 'lovetik.com',
			'accept': '*/*',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://lovetik.com',
			'referer': 'https://lovetik.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
   data = {
			'query': link}
   result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
   video = result['links'][1]['a']
   desc = result['desc']
   audio = result['links'][5]['a']
   bot.send_audio(chat_id, audio=audio, caption=desc,reply_markup =key)
def get_info(message): 
    key = InlineKeyboardMarkup()
    key.row_width = 2
    BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
    key.add(BA)
    user = f"{message.text}"
    api = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
    rr=requests.get(api).json()
    nam = str(rr['graphql']['user']['full_name'])
    iddd = str(rr['graphql']['user']['id'])
    fol = str(rr['graphql']['user']['edge_followed_by']['count'])
    fols =str(rr['graphql']['user']['edge_follow']['count'])
    isp = str(rr['graphql']['user']['is_private'])
    post = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
    ree = re.json()
    dat = ree['date']
    tlg =(f"""
---------------------------------------------------
Name » {nam}
User » @{user}
Followedby » {fols}
Follows count » {fol}
Date » {dat}
ID » {iddd}
Posts » {post}
Is privet? » {isp}
Link » https://www.instagram.com/{user}
---------------------------------------------------""")
    bot.reply_to(message,tlg,reply_markup =key)
def Fake_info(message): 
       key = InlineKeyboardMarkup()
       key.row_width = 2
       BA = InlineKeyboardButton(text ="رجوع الى الخلف ↩️" ,callback_data="back")
       key.add(BA)
       F=Faker()
       email=F.free_email() ;ip=F.ipv4()
       date=F.date() ;last=F.last_name_male() 
       first=F.first_name_male() ;job=F.job()
       con=F.country() ;city=F.city()
       str=F.street_name() ;zip=F.zipcode()
       card=F.credit_card_full() ;zone=F.timezone()
       num=F.phone_number()
       bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"""
*First Name:* `{first}`
*Last Name:* `{last}`
*Job:* `{job}`
*Time Zone:* `{zone}`
*Country:* `{con}`
*City:* `{city}`
*Street:* `{str}`
*Zip Code:* `{zip}`
*Email:* `{email}`
*Phone:* `{num}`
*IP:* `{ip}`
*Credit Card:* `{card}`
""",parse_mode="Markdown",reply_markup =key)

bot.polling()