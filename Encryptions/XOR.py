'''
Case Insensetive (All Will Be Lowercase)
Key Length Must Be 1 nad Will Automaticly Changed to Uppercase
'''


def ende(inpString,xorKey):
    length = len(inpString)
    for i in range(length): 
        inpString = (inpString[:i] + 
             chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:])
    return inpString

import os
while True:
    os.system('clear')
    print('''
     █ █ █▀▀█ █▀▀█
     ▄▀▄ █  █ █▄▄▀
     ▀ ▀ ▀▀▀▀ ▀ ▀▀    
     ''')
    WORD= input(' Type the Word to  Encrypt/Decrypt:  ')
    if WORD=='99':
        exit()
    KEY= input(' Enter Key (ONLY ONE CHARACTER):      ').upper()
    if WORD and len(KEY)==1:
        print(f' Encrypted/Decrypted is:  {ende(WORD.lower(),KEY)}\n')
        os.system('pause')