import telebot 
from telebot import types
from Nova_Tools import Tools
import names
import requests

call2 = types.InlineKeyboardButton(text = "Programmer", url="t.me/VZX_TEAM")

bot = input("[+] Enter Token : ") 

@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	bot.send_message(message.chat.id, text=f"Welcome my dear : {name} 👀\nBot Download Python Libs 🤯\nSend Lib Name 🤔\nProgrammer : @C0_28 | @VZX_TEAM 🙋‍♂")
	
@bot.message_handler()
def download(message):
	lib = message.text
	if lib == "Nova-Tools" or lib == "FakerMail":
		bot.send_message(message.chat.id, text="You are not allowed to download the library")
	else:
		try:
			di = requests.get(f"https://pypi.org/project/{lib}/").status_code
			if di == 404:
				bot.send_message(message.chat.id, text="Library not found")
			if di == 200:
				do = requests.get(f"https://pypi.org/project/{lib}/").text.split('<div class="card file__card">')[1].split(">")[0].split('<a href="')[1].split('"')[0]
				call = types.InlineKeyboardButton(text = "Download Lib", url = do)
				Keyy = types.InlineKeyboardMarkup()
				Keyy.row_width = 1
				Keyy.add(call,call2)
				name = message.from_user.first_name
				bot.send_message(message.chat.id, text=f"Welcome my dear : {name}  👀\nDone Download Python Lib 🤯",reply_markup=Keyy)
		except:
			bot.send_message(message.chat.id, text="Library not found")
			
bot.infinity_polling()