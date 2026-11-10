import pyfiglet
Z = '\x1b[1;31m'
F = '\x1b[2;32m'
B = '\x1b[2;36m'
X = '\x1b[1;33m'
C = '\x1b[2;35m'
logo = pyfiglet.figlet_format('firoun')
print(Z + logo)
loo = pyfiglet.figlet_format('CC Check')
print(F + loo)
k = '----+----+-----+------+-----+'
print(C + k)
lo = ' User : @X_EG_VIP'
print(X + lo)
i = '@X_EG_VIP_X'
print(C + i)
o = '#♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤#'
print(B + o)
import time
import os
import random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print('Code_Zilla love you ◇♧♤♡ ')
ch = '@Flashchkbot'
api_id = '17058698'
api_hash = '088f8d5bf0b4b5c0536b039bb6bdf1d2'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open('COD.txt', 'r').read().split('\n'):
                try:
                    client.send_message(ch, f'''/chg {chg}''')
                    time.sleep(random.randint(30, 30))
                    mssag = client.get_messages(ch, 1, **('limit',))
                    if 'ANTI_SPAM' in str(mssag[0].message):
                        t = str(mssag[0].message).split('again after ')[1]
                    t = t.split('seconds')[0]
                    t = int(t)
                    print(f'''Done Sleep : {t + 2}''')
                    time.sleep(t + 2)
                    print(mssag[0].message)
                    time.sleep(1)
                finally:
                    pass
                    print(False)
                    continue
               

