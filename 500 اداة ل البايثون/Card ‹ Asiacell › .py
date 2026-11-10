from random import *
from telebot import *
bot = TeleBot("——")
@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,f'''*⌁ 𝗛𝗶 𝗕𝗿𝗼𝘁𝗵𝗲𝗿,𝗕𝗼𝘁 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗖𝗔𝗥𝗗 𝗔𝘀𝗶𝗮𝗰𝗲𝗹𝗹 𝗜𝗤 ⚙️ 
𝗦𝗲𝗻𝗱 ‹ /guess › .*''',parse_mode="markdown")
@bot.message_handler(func=lambda m: True)

@bot.message_handler(commands=['guess'])
def g_ks(message):
	num = "0123456789"
	cards = str(''.join(random.choice(num) for i in range(14)))
	card = "*133*"+cards
	bot.send_message(message.chat.id,f'''*⌁ — 𝗗𝗼𝗻𝗲 𝗴𝘂𝗲𝘀𝘀 𝗖𝗮𝗿𝗱𝘀 𝗔𝘀𝗶𝗮𝗰𝗲𝗹𝗹 👾 .
⌁ ================ ⌁*
⌁ `{card}#`
*⌁ ================ ⌁*
*⌁ — 𝗗𝗼𝗻𝗲 𝗦𝗲𝗻𝗱 𝗢𝗻𝗰𝗲 𝗔𝗴𝗮𝗶𝗻 📫 .*''',parse_mode="markdown")

bot.polling(True)