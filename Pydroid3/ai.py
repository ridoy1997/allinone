import telebot
import requests
from telebot import types

token = "Token"
bot = telebot.TeleBot(token)
channel = types.InlineKeyboardButton(text="قناتي",url="https://t.me/SuPeRx1")
@bot.message_handler(commands=["start"])
def welcome(message):
	brok = types.InlineKeyboardMarkup()
	brok.add(channel )
	first_name = message.from_user.first_name
	bot.reply_to(message, f"- اهلن [{first_name}](tg://settings)\n& بوت يصنع اكواد بلغة بايثون\nفقط ارسل ما تريد لصنع كود\ndev @BRoK8",parse_mode='Markdown',reply_markup=brok)
	
@bot.message_handler(func=lambda brok:True)
def cod(message):
	try:
		co = message.text
		url = requests.get(f"https://dev-broksuper.pantheonsite.io/api/sm/ai/aii.php?code={co}").json()
		codee = url['result']
		bot.send_message(message.chat.id,codee)
	except:
		bot.reply_to(message,'error')
print('run')
bot.infinity_polling()