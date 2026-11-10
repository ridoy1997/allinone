import requests,os,telebot
from bs4 import BeautifulSoup

bo = telebot.TeleBot(input(" Enter token:  ")) 

@bo.message_handler(commands=["start"])
def srt(message):
	id = message.chat.id
	bo.send_message(id,"Welcome To Bot Create Logo\n\nPlease Send Name")
@bo.message_handler()
def found(message):
		text = str(message.text)
		try:
		    url = f"https://www.brandcrowd.com/maker/logos?text={text}"
		    r = requests.get(url)
		    soup = BeautifulSoup(r.content)
		    links = soup.find_all("img")
		    os.system('clear')
		    for link in links:
		        v = link.get("src")
		        if text in str(v):
		            #print(v)				        
		            bo.send_photo(message.chat.id,v)    
		except:
			bo.send_message(message.chat.id,"Please brother, try again in 10 seconds")
bo.infinity_polling()
