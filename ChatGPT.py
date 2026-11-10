import telebot
import requests
#خلي توكن بوتك مكان: توكن بوتك هنا 
bot = telebot.TeleBot('توكن بوتك هنا ')
#من تخلي توكن بوتك شغل الاداه وروح لبوتك راح يشتغل وياك بوت ذكاء اصطناعي 
#تم تطوير البوت من قبل SD 
#معرف المطور lU22U@
#تم تطوير Api البوت من قبل SD 
#ملاحضة البوت بدون تشفير ومجانا اذا شفت البوت مغيرين حقوقه ويبيعون بي راح اوقف ال Api
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_developer = telebot.types.InlineKeyboardButton('مطور', url='https://t.me/lU22U')
    markup.add(btn_developer)
    
    bot.reply_to(message, "اهلآ بك عزيزي \n*مرحبًا بك في بوت الذكاء الاصطناعي!*\n\nيمكنك استخدام هذا البوت لطرح الأسئلة على الذكاء الاصطناعي ارسل سوالك للحصول على الإجابة.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "جاري حصول على الرد...")
    
    response = requests.get(f"https://educatedwindyoctal.66666612.repl.co/By?SD={message.text}").text
    
    bot.send_message(message.chat.id, response)
    
bot.polling()