try:
    #TeaM_ExEc #@VnVn2 #Warrior
    import requests,random,threading
    from cfonts import render
    from random import choice

except ImportError:
    print("Please install missing libraries: requests, random, threading, cfonts")


W = "\033[0m" ;G = '\033[32;1m';R = '\033[31;1m'
A = "\033[1;91m";B = "\033[1;90m";C = "\033[1;97m"
E = "\033[1;92m";H = "\033[1;93m";K = "\033[1;94m"
L = "\033[1;95m";M = "\033[1;94m"


Fix = '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}'
Fix2 = '"errors": {"username":'
Fix3 = '"code": "username_is_taken"'


def Banner():

    Bannerx = f""" {C}<   {H}TeaM ~ ExEc ~ TheBesT   {C}>"""
    output = render('EXEC',colors=[str(choice(['red'])), str(choice(['white'])), str(choice(['red','green','white']))],align='left',space='0')
    Banner = f"""
  {C}<   {H}CHECK INSTAGRAM USERNAME {C}>  
 {C}---------------------------
 {R}[{C}+{R}] {H}NAME       {C}: {H}EXEC
 {R}[{C}+{R}] {H}GITHUB     {C}: {H}6F8
 {R}[{C}+{R}] {H}INSTAGRAM  {C}: {H}GXP6
 {R}[{C}+{R}] {H}TELEGRAM   {C}: {H}VNVN6
 {R}[{C}+{R}] {H}YOUTUBE    {C}: {H}WARRIOR
 {C}---------------------------"""
    print(output+Bannerx+Banner)
Banner()


iD    = input (f" {R}[{C}+{R}] {C}ENTER YOUR ID TELE {R}: ")
TokeN = input (f" {R}[{C}+{R}] {C}ENTER YOU TOKEN BOT {R}: ")


def Check():
    while True :
        letters = 'A1B2C3D4E5F6G7H8I9J0K_LMNOPQRSTUVWXYZ'
        duplicate_letter = random.choice(letters)
        duplicates_count = random.randint(3, 7)
        duplicates = duplicate_letter * duplicates_count
        Username = list(duplicates)
        different_letter = random.choice(letters.replace(duplicate_letter, ''))
        random_index = random.randint(0, len(Username))
        Username.insert(random_index, different_letter)
        Username = ''.join(Username)
        URL = f"https://www.instagram.com/accounts/web_create_ajax/attempt/"
        headers = {'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type':'application/x-www-form-urlencoded','accept':'/','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL','cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425','cookie':'ig_nrcb=1'}
        data = f'email=aakmnnsjskksmsnsn%40gmail.com&username={Username}&first_name=&opt_into_one_tap=false'
        response = requests.post(url=URL, headers=headers, data=data)

        if Fix in response.text:
            print (f"{R}[{C}Username ~ Error{R}] {C}==> {R}{Username}")
        elif Fix2 in response.text:
            print (f"{R}[{C}Username ~ TaKen{R}] {C}==> {R}{Username}")
        elif Fix3 in response.text:
            print (f"{R}[{C}Username ~ TaKen{R}] {C}==> {R}{Username}")
        else :
            open("Available.txt","a").write(f"{Username}\n")

            requests.post(f'https://api.telegram.org/bot{TokeN}/sendMessage?chat_id={iD}&text=UsernamE ✓ : {Username}')
            print (F"{R}[{C}UsernameGooD{R}] {C}==> {E}{Username}")    

thread = []
for i in range(10):
    thread1 = threading.Thread(target=Check)
    thread1.start()
    thread.append(thread1)
    for thread2 in thread:
        thread2.join    