import telebot

bot = telebot.TeleBot("5588418954:AAH3XXHb3lxorzTChy_lz1qQ2j3PpVr_Mrk")

@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	bot.send_message(message.chat.id, text=f"َاهلا بك يا عزيزي : {name}\nبوت تقليد اي كلمة ترسلها\nالمبرمج : @C0_28 | @VZX_TEAM")
	
@bot.message_handler()
def answer(message):
	text = message.text
	bot.send_message(message.chat.id, text=text)

bot.infinity_polling()