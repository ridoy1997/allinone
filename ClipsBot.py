import telebot, os
import moviepy.editor as mp

bot = telebot.TeleBot(token=str(input("TOKEN : ")), parse_mode="markdown")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, f'*Send Audio...*')

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
  try:
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    open('file1.ogg', 'wb').write(downloaded_file)
    sent = bot.reply_to(message,f"*- أرسل ملف صوتي أخر للدمج*")
    def OpenVoice(message):
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        open('file2.ogg', 'wb').write(downloaded_file)
        sentWait = bot.reply_to(message,f"*- جاري الدمج...*")
        audioC1 = mp.AudioFileClip('file1.ogg')
        audioC2 = mp.AudioFileClip('file2.ogg')
        ClipsAudio = [audioC1, audioC2]
        final_audio = mp.concatenate_audioclips(ClipsAudio)
        final_audio.write_audiofile('CompileAudio.ogg')
        try:
            bot.send_audio(chat_id=message.chat.id, audio=open('CompileAudio.ogg', 'rb'), caption='*- تم الدمج☑️*', timeout=1000, reply_to_message_id=sentWait.message_id)
            os.remove('file1.ogg') 
            os.remove('file2.ogg') 
            os.remove('CompileAudio.ogg') 
        except:
            os.remove('file1.ogg') 
            os.remove('file2.ogg') 
            bot.reply_to(sentWait,f"*- تم الحفظ في ملف CompileAudio.ogg*")
    bot.register_next_step_handler(sent, OpenVoice)
  except Exception as err:
    bot.send_message(message.chat.id, text=f'حدث خطأ:\n{err}', parse_mode=None)
@bot.message_handler(content_types=['audio'])
def audio_processing(message):
  try:
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    open('file1.mp3', 'wb').write(downloaded_file)
    sent = bot.reply_to(message,f"*- أرسل ملف صوتي أخر للدمج*")
    def OpenAudio(message):
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        open('file2.mp3', 'wb').write(downloaded_file)
        sentWait = bot.reply_to(message,f"*- جاري الدمج...*")
        audioC1 = mp.AudioFileClip('file1.mp3')
        audioC2 = mp.AudioFileClip('file2.mp3')
        ClipsAudio = [audioC1, audioC2]
        final_audio = mp.concatenate_audioclips(ClipsAudio)
        final_audio.write_audiofile('CompileAudio.mp3')
        try:
            bot.send_audio(chat_id=message.chat.id, audio=open('CompileAudio.mp3', 'rb'), caption='*- تم الدمج☑️*', timeout=1000, reply_to_message_id=sentWait.message_id)
            os.remove('file1.mp3') 
            os.remove('file2.mp3') 
            os.remove('CompileAudio.mp3') 
        except:
            os.remove('file1.mp3') 
            os.remove('file2.mp3') 
            bot.reply_to(sentWait,f"*- تم الحفظ في ملف CompileAudio.mp3*")
    bot.register_next_step_handler(sent, OpenAudio)
  except Exception as err:
    bot.send_message(message.chat.id, text=f'حدث خطأ:\n{err}', parse_mode=None)
bot.infinity_polling()