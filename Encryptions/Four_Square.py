import re

table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 

def generate_table(key = ''):
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '')
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table

def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L  = generate_table(keys[0]), generate_table(keys[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += mangle(R, L, digraphs)
    return ciphertext


def mangle(R, L, digraphs):
    a = position(table, digraphs[0])
    b = position(table, digraphs[1])
    return R[a[0]][b[1]] + L[b[0]][a[1]]

def decrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L = generate_table(keys[0]), generate_table(keys[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += unmangle(R, L, digraphs)
    return ciphertext.lower()

def unmangle(R, L, digraphs):
    a = position(R, digraphs[0])
    b = position(L, digraphs[1])
    return table[a[0]][b[1]] + table[b[0]][a[1]]

def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return (row, col)
    return (None, None)





import os
while True:
    os.system('clear')
    print('''
       ▄
     ▄▀█        █▀▀ █▀▀█ █  █ █▀▀█ █▀▀█ █▀▀
     ▀▀█▀       ▀▀█ █ ▄█ █  █ █▄▄█ █▄▄▀ █▀▀
       ▀   ▀▀▀  ▀▀▀ ▀▀▀█  ▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀     ''')
    print('''
        {1}--Encrypt to 4-Square
        {2}--Decrypt 4-Square Cipher  (Under Maintaince and May Not Work Correctly.)
    ''')
    vminp= input(' DramaX:4_Square> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word=  input(' Type Word :  ')
        Key=  [input(' Enter Key1:  '),input(' Enter Key2:  ')]
        #if Word and Key[0] and Key[1]:
        print(encrypt(Key,Word))
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key=   [input(' Enter Key1:         '),input(' Enter Key2:         ')]
        if Cipher and Key:
            print(decrypt(Cipher,Key)+'\n')
    os.system('pause')
