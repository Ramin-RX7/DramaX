'''
- Case Sensetive
- Supports Numbers and Symbols
- KEY1 should be chosen to be relatively prime to 94 (i.e. a should have no factors in common with 26)
  List of All Acceptable Key1:
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
- KEY2 Can be any Number Higher than 9
'''


# UM
"""
 def egcd(a, b): 
     x,y, u,v = 0,1, 1,0
     while a != 0: 
         q, r = b//a, b%a 
         m, n = x-u*q, y-v*q 
         b,a, x,y, u,v = a,r, u,v, m,n 
     gcd = b 
     return gcd, x, y 
 def modinv(a, m): 
     gcd, x, y = egcd(a, m) 
     if gcd != 1: 
         return None 
     else: 
         return x % m 
 
 def affine_encrypt(text, key):
     return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)+ ord('A')) for t in text.upper().replace(' ', '')]) 
 def affine_decrypt(cipher, key):
     return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 
"""


import sys, pyperclip, cryptomath, random, detectEnglish

SYMBOLS = """ !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

def main(myMessage,myKey,myMode):
    #myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    #myKey = 2023
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    '''print('Key: %s' % (myKey))
     print('%sed text:' % (myMode.title()))
     print(translated)
     pyperclip.copy(translated)
     print('Full %sed text copied to clipboard.' % (myMode))'''
    return f'{myMode}ed String is:  {translated}'

def hackAffine(message):
    print()
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    # brute-force by looping through every possible key
    for key in range(len(SYMBOLS) ** 2):
        keyA = getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
            continue
        decryptedText = decryptMessage(key, message)
        #if not SILENT_MODE:
        #    print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
        if detectEnglish.isEnglish(decryptedText):
            print()
            print(' Possible encryption hack:')
            print(' Key1: %s  |  Key2: %s' % (str(key)[:2],str(key)[2:]))
            print(f' Decrypted Message:  {rx7.style(decryptedText[:200],BG="dark_green")}')

            print()
            print(' Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper() in ('DONE','D'):
                return decryptedText
    return None

def HACK(myMessage):
    hackedMessage = hackAffine(myMessage)
    if hackedMessage != None:
        print(f' Copying hacked message to clipboard:  {hackedMessage}')
        pyperclip.copy(hackedMessage)
    else:
        print(' Failed to hack encryption.')

def getKeyParts(key):
    key=int(key)
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit(' The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit(' The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit(' Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit(' Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
    key= int(key)
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext

def decryptMessage(key, message):
    key= int(key)
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB



import os,rx7
while True:
    os.system('clear')
    print('''

      █▀▀█ █▀▀ █▀▀ ▀█▀ █▀▀▄ █▀▀
      █▄▄█ █▀▀ █▀▀  █  █  █ █▀▀
      ▀  ▀ ▀   ▀   ▀▀▀ ▀  ▀ ▀▀▀  ''')
    print('''
        {1}--Encrypt to Affine
        {2}--Decrypt Affine Cipher
        {3}--Affine Hacker
     ''')
    vminp= input(' DramaX:Affine> ')
    print()
    if rx7.files.exists('Affine/affinecipher.py'): pade= ''
    else: pade='Encryptions/'
    pass
    if vminp=='99':
        exit()
    if vminp.lower() in ('-h','-help'):
        print(__doc__)

    if vminp=='1':
        Word=      input(' Type Word :  ')
        Key1= int(input(  ' Enter Key1:  '))
        Key2= int(input(  ' Enter Key2:  '))
        print(f' Decrypted Cipher is:  {main(Word,str(Key1)+str(Key2),"encrypt")}\n')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key1= input(  ' Enter Key1:  ')
        Key2= input(  ' Enter Key2:  ')
        print(f' Decrypted Cipher is:  {main(Cipher,str(Key1)+str(Key2),"decrypt")}\n')
    if vminp=='3':
        Cipher= input(' Type Cipher Text:   ')
        HACK(Cipher)
        #os.system(f'python {pade}Affine/affinehacker.py "{Cipher}"')

    os.system('pause')
# 1nNx[1 !
