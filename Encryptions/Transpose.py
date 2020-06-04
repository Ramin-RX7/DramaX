'''
len(word)>len(key)>1
'''

import math,detectEnglish,os

def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)
def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
def hackTransposition(message):
    print(' Hacking...')
    print(' (Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(1, len(message)):
        print(' Trying key #%s...' % (key))
        decryptedText = decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptedText):
            print()
            print(' Possible encryption hack:')
            print(' Key %s: %s' % (key, decryptedText[:100]))
            print()
            print(' Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

'''
hackTransposition('rixan7mr')
'''

while True:
    os.system('clear')
    print('''
 
      ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ 
        █   █▄▄▀ █▄▄█ █  █ ▀▀█ █▀▀▀ █  █ ▀▀█ █▀▀ 
        ▀   ▀ ▀▀ ▀  ▀ ▀  ▀ ▀▀▀ ▀    ▀▀▀▀ ▀▀▀ ▀▀▀   ''')
    print('''
        {1}--Encrypt to Transpose
        {2}--Decrypt Transpose Cipher
        {3}--Transpose Cracker  (Under Maintaince)
    ''')
    vminp= input(' DramaX:Transpose> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ')
        Key=  input(' Enter Key:  ')
        if Word and Key:
            print(f' Encrypted String is:  {encryptMessage(int(Key),Word)}\n')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key=    input(' Enter Key:          ')
        if Cipher:
            print(f' Decrypted Cipher is:  {decryptMessage(int(Key),Cipher)}\n')

    os.system('pause')
