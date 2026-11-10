from telebot import *
from time import sleep
import requests

bot = TeleBot("")
userBot = ("")
# -- user bot dont [@] --
ad = (f'https://t.me/{userBot}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members')
@bot.message_handler(commands=['start'])
def start(message):
	key = types.InlineKeyboardMarkup()
	str = types.InlineKeyboardButton('اضفني لـ مجموعتك 🧚🏼‍♂️' ,url =f'{ad}')	
	key.add(str)
	bot.reply_to(message,f'''*اهلين انا ايفو 🧚

↞اختصاصي زخرفه اسم بلغه ‹ en ; ar › .
↞ فريند البـوت تيست ...
 *''',parse_mode="Markdown",reply_markup=key)
@bot.message_handler(func=lambda m : True )
def main(message):
  	ivo = message.text
  	url = f'https://dedo.cf/api-zkrfa.php?text={ivo}'
  	ivos = requests.get(url).json()
  	p = ivos['results']
  	bot.reply_to(message,f'''↞ انتظرنـي *
 *''',parse_mode="Markdown")
  	time.sleep(2)
  	bot.send_message(message.chat.id,f'''*↞ تـم الانتهاء 🧚🏼🔃 ...
• الـيـك الـزخارف  : 
↞ الاسـم : {ivo}  .
↞الـزخرفة : {p} .*''',parse_mode="Markdown",reply_to_message_id=message.message_id)
bot.polling()