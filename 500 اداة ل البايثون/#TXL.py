logo = """

 ---------------  -----      -----   ---
|               | \    \    /    /  /   \ 
 ---------------   \    \  /    /   /   \
      /    \        \    \/    /    /   \
      /    \         \   /\   /     /   \
      /    \          \ /  \ /      /   \
      /    \           /    \       /   \
      /    \          / \  / \      /   \
      /    \         /   \/   \     /   \
      /    \        /    /\    \    /   \
      /    \       /    /  \    \   /___________\
      /~~~~\      /~~~~/    \~~~~\  /~~~~~~~~~~~\
                                                            
        @BBB2B           
        
   goin now @GGGRG                                                                                                                                                                               
                                                                                                         
                                """
print(logo)


import random
num = 0
oo = 'ieisjqwertyuiopasdfghjzxcvbnm'
gg = 'qwertyuiopasdfghjklzxcvbnm1234567890'

while True:
	user = random.choice(gg)+random.choice(gg)+random.choice(gg)+random.choice(oo)+random.choice(gg)+random.choice(gg)
	email = user+("@gmail.com")
	num +=1
	with open('list.yahoo.txt','a') as xx:
		xx.write(f'{email}\n')
		print(f'\r[+] - number : {num,email}', end=' ')

