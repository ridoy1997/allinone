import random
import requests
from telethon import TelegramClient, events, sync
import time

#الالوان
s = '\033[1;36m'
a = '\033[1;33m'
z = '\033[1;31m'

print(s+"""اذا اردت ان تولد فيزات وارسالها للبوت اكتب {1}
      واذا اردت ان تفحص فيزاتك اكتب {2}
""")
choice = input("Enter Number : ")

if choice == "1":
	token = input("Enter the token : ")
	chat_id = input("Enter the id : ")
	digits_1 = input("Enter the first set of digits (6 digits only) : ")
	
	# Check if the input is a 6-digit number
	while len(digits_1) != 6 or not digits_1.isdigit():
	    print("Invalid input. Please enter a 6-digit number.")
	    digits_1 = input("Enter the first set of digits (6 digits only) : ")
	
	# Create a list to store the generated numbers
	numbers = []
	
	# Generate 100 random numbers and add them to the list
	for i in range(100):
	    # Create the first group of 16 digits
	    digits_1_rest = ''.join(str(random.randint(0, 9)) for _ in range(10))
	    digits_1_full = digits_1 + digits_1_rest if len(digits_1) < 16 else digits_1[:16]
	
	    # Create the second group of 2 digits
	    digits_2 = str(random.choice(range(1, 13))).zfill(2)
	
	    # Create the third group of 4 digits
	    digits_3 = "202" + str(random.randint(3, 9))
	
	    # Create the fourth group of 3 digits
	    digits_4 = ''.join(str(random.randint(0, 9)) for _ in range(3))
	
	    # Combine the groups separated by vertical bars
	    result = digits_1_full + "|" + digits_2 + "|" + digits_3 + "|" + digits_4
	
	    # Add the number to the list
	    numbers.append(result)
	
	    # Send the result to the Telegram account
	    url = "https://api.telegram.org/bot" + token + "/sendMessage"
	    params = {"chat_id": chat_id, "text": result}
	    req = requests.get(url, params=params)
	
	    if req.status_code == 200:
	        print("Message", i+1, "sent successfully!")
	    else:
	        print("Error sending message", i+1)
	
	# Write the numbers to a file
	path = input("Enter file path : ")
	
	with open(path, 'w') as f:
	    f.write('\n'.join(numbers))
	
	print("Numbers saved to", path)
elif choice == "2":
	print(s+"-"*50)
	print(s+"تم الصنع الاداة بواسطة المطور دارك (Youssef)")
	print("-"*50)
	print('\033[1;31m' + 'اداة فحص ايديات انستا اب وفيزات على أي بوت' + '\033[0m')
	print("•"*24)
	#معلومات تسجيل الدخول للحساب
	
	api_id = 10935817
	api_hash = '0cc337dc972b6323a9421daa3d6cd3e2'
	phone_number = '+9647503976745'
	
	client = TelegramClient('session_name', api_id, api_hash)
	
	async def login():
	    await client.connect()
	    if not await client.is_user_authorized():
	        await client.send_code_request(phone_number)
	        try:
	            await client.sign_in(phone_number, input('Enter the code: '))
	        except SessionPasswordNeededError:
	            password = input('Two-Step Verification enabled. Please enter your password: ')
	            await client.sign_in(password=password)
	
	    # انتظار 5 ثواني بعد تسجيل الدخول
	    time.sleep(5)
	
	    # إرسال رسالة "/start" إلى البوت المحدد
	    televisa = input(s+"Enter user name the bot : ")
	    print("•"*35)
	    bot_username = (televisa)
	    await client.send_message(bot_username, "/start")
	
	    # انتظار 5 ثواني قبل إرسال الرسائل من الملف
	    time.sleep(5)
	
	    # إرسال الرسائل من الملف إلى البوت المحدد
	    infile = input(s+"Enter The File : ")
	    print(z+"•*35")
	    with open("/storage/emulated/0/"+infile, 'r') as f:
	        lines = f.readlines()
	        bot_entity = await client.get_entity(bot_username)
	        for line in lines[1:]:
	            await client.send_message(bot_entity, ".vbv "+line.strip())
	            print("بدء الفحص")
	            time.sleep(3.1)
	
	    await client.disconnect()
	
	client.start()
	client.loop.run_until_complete(login())