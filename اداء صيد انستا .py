# encoding: utf-8
# Decoded by HackerMode tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @GG4RT )
import requests
import telebot
from time import sleep
token = input(' 🌼Token :')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*هلا  طريقه التشغيل فقط ارسل اليوزر و سيتم اجيد جميع حقوقه         ــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــ       {first} اتشرفت بيك حب \n                              ALI𖢕 - @GG4RT*",parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, text="ويت حب @GG4RT")
        sleep(2)
        url = f'https://google7x.ml/API/kashif.php?text={msg}'
        ref = requests.get(url)
        res = ref.json()
        gen = res['Name']
        User = res['Username']
        id = res['Id']
        bot.send_message(message.chat.id,text=f' \nالاسم : {gen}\nاليوزر  : {User}\nايدي : {id}\n ـ @o_j_y  @GG4RT')
    except:
        pass
bot.polling(True)