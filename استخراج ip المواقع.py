#by omar
#Telegram >> @toolsegy
#استخراج ايبي الموقع

import socket

Dmn = input("Type url : ") #رابط الموقع
iip = socket.gethostbyname(Dmn)
print(iip)

