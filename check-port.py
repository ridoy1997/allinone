import socket
from socket import *
import telebot

bot = telebot.TeleBot("5588418954:AAE2XfYSFdFvr3TNd5gNHw6SnJIPLL8iVcQ")

@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	bot.send_message(message.chat.id, text=f"اهلا بك يا عزيزي {name}\nبوت فحص البورتات المفتوحة في الايبي\nفقط قم بارسال الايبي:البورت\nالمبرمج : @C0_28 | @VZX_TEAM")

@bot.message_handler(func=lambda m: True)
def checkPort(message,timeout=0.1):
       host = message.text
       hostname = host.split(':')[0]
       port = host.split(':')[1]
       sock = socket(
       family=AF_INET,
       type=SOCK_STREAM,
       proto=0,
       fileno=None
       )
       sock.settimeout(timeout)
       try:
            portOpen = sock.connect((hostname, port))
            sock.close()
            bot.send_message(message.chat.id, text=f"Ip : {hostname}\nport : {port}\nStatus : True")
       except:
            bot.send_message(message.chat.id, text=f"Ip : {hostname}\nport : {port}\nStatus : False")
        
bot.infinity_polling()