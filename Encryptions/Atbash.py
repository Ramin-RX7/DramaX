'''

'''


alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def atbash(message):
    cipher = ''
    for letter in message:
        if letter in alp:
            cipher +=  alp[25-alp.index(letter)]
        else:
            cipher += letter
    return cipher 

import os
while True:
    os.system('clear')
    print('''

      █▀▀█ ▀▀█▀▀ █▀▀▄ █▀▀█ █▀▀ █  █
      █▄▄█   █   █▀▀▄ █▄▄█ ▀▀█ █▀▀█
      ▀  ▀   ▀   ▀▀▀  ▀  ▀ ▀▀▀ ▀  ▀ 
      ''')
    vminp= input(' Type Word To Encrypt/Decrypt:   ')
    print()
    if vminp=='99':
        exit()
    else:
        print(f' Encrypted/Decrypted is:  {atbash(vminp.upper())}\n')
    os.system('pause')
