'''
Case Sensetive
Support Numbers and Symbols
Key Is Case Sensetive
'''

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789</>!"@£$%^&*()-=_+?~,.'
def generateKey(string, key):
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def new_alph(ch):
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph

def encrypt(text, big_key):
    res = ''
    i = 1
    big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t) == 1:
                res += new[alph.index(t)]
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res

def decrypt(text, big_key):
    res = ''
    i = 1
    big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t) == 1:
                res += alph[new.index(t)]
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res


import os
while True:
    os.system('clear')
    print('''

      ▀█ █▀ ▀█▀ █▀▀▀ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀
       █▄█   █  █ ▀█ █▀▀ █  █ █▀▀ █▄▄▀ █▀▀
        ▀   ▀▀▀ ▀▀▀▀ ▀▀▀ ▀  ▀ ▀▀▀ ▀ ▀▀ ▀▀▀  ''')
    print('''
        {1}--Encrypt to Vigenere
        {2}--Decrypt Vigenere Cipher
        {3}--Vigenere Cracker  (Comming Soon...)
    ''')
    vminp= input(' DramaX:Vigenere> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ')
        Key=  input(' Enter Key:  ')
        if Word and Key:
            print(f' Encrypted String is:  {encrypt(Word,Key)}\n')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key=    input(' Enter Key:          ')
        if Cipher and Key:
            print(f' Decrypted Cipher is:  {decrypt(Cipher,Key)}\n')
    os.system('pause')
