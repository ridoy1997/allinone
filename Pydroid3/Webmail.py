from msilib.schema import Error
import warnings
from colorama import init, Fore
from multiprocessing.dummy import Pool, Lock
import multiprocessing
import requests
import sys
import subprocess
import os
import time
from termcolor import colored, cprint
init(strip=not sys.stdout.isatty())
init()
os.system(
    'title Webmail Valid Domain Checker By X7ROOT - Valid: 0 - Bad: 0 - Error: 0')
if not os.path.exists('Results'):
    os.makedirs('Results')
warnings.filterwarnings("ignore")
print(colored(r"""

                        __          __  _                     _ _    _____ _               _
                        \ \        / / | |                   (_) |  / ____| |             | |
                         \ \  /\  / /__| |__  _ __ ___   __ _ _| | | |    | |__   ___  ___| | _____ _ __
                          \ \/  \/ / _ \ '_ \| '_ ` _ \ / _` | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
                           \  /\  /  __/ |_) | | | | | | (_| | | | | |____| | | |  __/ (__|   <  __/ |
                            \/  \/ \___|_.__/|_| |_| |_|\__,_|_|_|  \_____|_| |_|\___|\___|_|\_\___|_|

                                        [*] Telegram : https://t.me/x7seller
""", 'yellow'))
lock = Lock()
combo_txt = input('[+] Enter Your Combo List : ')
print('  ')
combo_len = len(open(combo_txt, 'r', errors='ignore').read().split('\n'))
thread_num = int(input('[+] Enter Number of Threads: '))
print('  ')
TotalCombo = print('[+] Combo Loaded : {}'.format(combo_len))
print('  ')
Valid = 0
Bad = 0
Error = 0


class Post:

    def login(self, email, password):
        global Valid, Bad, Error
        try:
            session = requests.session()
            domain = email[email.index("@")+1:]
            source = session.get(
                f"https://{domain}:2096", verify=False, timeout=5).text
            Valid += 1
            lock.acquire()
            print("Domian" + Fore.LIGHTGREEN_EX +
                  "[WebMail] " + Fore.LIGHTWHITE_EX + f"Domain : {domain} ")
            print(f"{domain}""", file=open(
                "Results\\Hits_Webmail.txt", "a"))
            os.system(
                "title " + "[+] Webmail Valid Domain Checker Progressing .. [Valid :  {} ] [Bad : {} ] [Error : {} ]".format(
                    Valid, Bad, Error))
            lock.release()
        except:
            try:
                source = session.get(
                    f"http://{domain}:2096", verify=False, timeout=5).text
                if '/login/' in source:
                    Valid += 1
                    lock.acquire()
                    print("Domian" + Fore.LIGHTGREEN_EX +
                          "[WebMail] " + Fore.LIGHTWHITE_EX + f"Domain : {domain} ")
                    print(f"{domain}""", file=open(
                        "Results\\Hits_Webmail.txt", "a"))
                    os.system(
                        "title " + "[+] Webmail Valid Domain Checker Progressing .. [Valid :  {} ] [Bad : {} ] [Error : {} ]".format(
                            Valid, Bad, Error))
                    lock.release()
                else:
                    Bad += 1
                    lock.acquire()
                    print("Domian" + Fore.LIGHTRED_EX +
                          "[Not_WebMail] " + Fore.LIGHTWHITE_EX + f"Domain : {domain} ")
                    os.system(
                        "title " + "[+] Webmail Valid Domain Checker Progressing .. [Valid :  {} ] [Bad : {} ] [Error : {} ]".format(
                            Valid, Bad, Error))
                    lock.release()
            except:
                Error += 1
                print("Domian" + Fore.LIGHTBLUE_EX +
                      "[Error] " + Fore.LIGHTWHITE_EX + f"Domain : {domain} ")
                os.system(
                    "title " + "[+] Webmail Valid Domain Checker Progressing .. [Valid :  {} ] [Bad : {} ] [Error : {} ]".format(
                        Valid, Bad, Error))


class Thread:

    def __init__(self, cmb_txt, threads):
        self.cmb_txt = cmb_txt
        self.threads = threads
        self.accounts = []

    def load(self):
        with open((self.cmb_txt), errors='ignore') as (f):
            lines = f.read().split('\n')
        for line in lines:
            if line.count(':') == 1:
                email, password = line.split(':')
                self.accounts.append({'email': email,
                                      'password': password})

    def brute(self, account):
        email = account['email']
        password = account['password']
        Post().login(email, password)

    def main(self):
        self.load()
        pool = Pool(self.threads)
        for _ in pool.imap_unordered(self.brute, self.accounts):
            pass


if __name__ == '__main__':
    Thread(combo_txt, thread_num).main()
    print('  ')
    input('[+] Completed')
