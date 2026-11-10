import tambotapi 
import time
import random
import requests
from user_agent import generate_user_agent

token = "_Zu_g2OnrVVwOwaG-ZbLMhrJq-rYpZ2M_b919Hhricw"

bot = tambotapi.TamBot(token)


def main():
    chat_id = bot.get_chat_id()  
    bot.send_message("Hello My Friend\nSend /check To Start Check", chat_id)
    while True:
        last_update = bot.get_updates() 
        if last_update: 
            chat_id = bot.get_chat_id(last_update) 
            type = bot.get_update_type(last_update)
            callback_id = bot.get_callback_id(last_update)
            if bot.get_text(last_update) == '/check':
                bot.send_message("Done Start Check\nBy : @ItsCoder | @tambotapi", chat_id)
                while True:
                    v1 = str(''.join((random.choice("qwertyuioplkjhgfdsazxcvbnm") for i in range(1))))
                    v2 = str(''.join((random.choice("qwertyuioplkjhgfdsazxcvb-nm-")for i in range(1))))
                    v3 = str(''.join((random.choice("qwertyuioplkjh-gfdsazxcvbnmhd") for i in range(1))))
                    user1 = (v1+v3+v2+v2)
                    user2 = (v1+v3+v3+v1)
                    nova = (user1, user2)
                    user = random.choice(nova)
                    headers={
                	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                'User-Agent': str(generate_user_agent())
                }
                    resp = requests.get(f'https://tt.me/{user}',headers=headers)
                    if resp.ok:
                        if '<meta property="og:url" content="https://tamtam.chat/">' in resp.text:
                            bot.send_message(f"Available User ✅: @{user}", chat_id)
                    else:
                        pass
            else:
            	pass
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
