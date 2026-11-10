import tkinter as tk
import requests
import random

def check_username():
    telegram_id = telegram_id_entry.get()
    token_bot = token_bot_entry.get()

    while True:
        tx1 = '1234567890qwertyuiopasdfghjklzxcvbnm'
        tx2 = '_._._._._.'
        tx3 = '_._._._._.1234567890'

        sr1 = str(''.join(random.choice(tx1)for i in range(1)))
        sr2 = str(''.join(random.choice(tx1)for i in range(1)))
        sr3 = str(''.join(random.choice(tx1)for i in range(1)))
        sr4 = str(''.join(random.choice(tx2)for i in range(1)))
        sr5 = str(''.join(random.choice(tx3)for i in range(1)))
        sr6 = str(''.join(random.choice(tx1)for i in range(1)))

        rm  = sr5+sr1+sr6+sr3+sr5
        rm2 = sr1+sr5+sr6+sr5+sr4
        rm3 = sr1+sr6+sr5+sr3+sr5
        rm4 = sr5+sr6+sr3+sr5+sr4
        rm5 = sr5+sr2+sr2+sr4+sr1
        rm6 = sr3+sr5+sr3+sr5+sr3
        rm7 = sr3+sr5+sr5+sr5+sr5
        nm_ = (rm,rm2,rm3,rm4,rm5,rm6,rm7)

        user = random.choice(nm_)
        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        headers ={'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type':'application/x-www-form-urlencoded','accept':'/','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL','cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425','cookie':'ig_nrcb=1'}
        data = f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false'
        response = requests.post(url,headers=headers,data=data)
        if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in response.text:
            result_label.config(text=f"Username~ErroR : {user}")
        elif '"errors": {"username":' in response.text or '"code": "username_is_taken"' in response.text:
            result_label.config(text=f"Username~TaKeN : {user}")
        else:
            open("Available.txt","a").write(f"{user}\n")
            message = f"Username~Aailable \n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n- UsernamE ✓ : {user}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n- Canecl > @YSYSD By > @VNVN6"
            requests.post(f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={telegram_id}&text={message}')

            result_label.config(text=f"Username~Available : {user} ✓")


window = tk.Tk()
window.title("Instagram Username Checker")

telegram_id_label = tk.Label(window, text="Enter your Telegram ID:")
telegram_id_label.pack()
telegram_id_entry = tk.Entry(window)
telegram_id_entry.pack()

token_bot_label = tk.Label(window, text="Enter your Token Bot:")
token_bot_label.pack()
token_bot_entry = tk.Entry(window)
token_bot_entry.pack()

check_button = tk.Button(window, text="Check Username", command=check_username)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

footer = tk.Frame(window)
footer.pack(side="bottom", fill="x")

copyright = tk.Label(footer, text="Team ExEc")
copyright.pack()

window.geometry("350x150")
window.mainloop()
