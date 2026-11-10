import random
import os
import sys
os.system('pass.txt')
G = open('pass.txt', "w")
E = "\033[1;93m"
A = "\033[1;90m" 
Q = input('How many passwords in list : ')
Q = int(Q)
def Genpass():
	K=0
	u = "0123456789qwertyuioplkjhgfdsazxcvbnm@#$"
	while True:
	   K+=1
	   passs =str("".join(random.choice(u)for i in range(8)))
	   print(f'\r {E}Making passwords list :{A}  {K}',end="")
	   G.write(passs+'\n')
	   if K ==Q:
	   	break
Genpass()