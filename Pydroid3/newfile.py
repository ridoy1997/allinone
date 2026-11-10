import telebot

bot = telebot.TeleBot("#توكنه")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أدخل المعلومات:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_input = message.text
    t = user_input.splitlines()

    result = ""

    for b in t:
        if ": " in b:
            splitfile = b.strip().split(": ")
            if len(splitfile) >= 2:
                basha = splitfile[0]
                bash = splitfile[1]
                f = ":"
                jhe= f"'{jjenm}'" + f + f"'{jh}',"
                result += jhe + "\n"

    bot.reply_to(message, result)
#يبن المتناكه لاتخمط السورس
#@WVKWV
bot.polling()