'''
Case Insensetive
Key Insensetive
'''


alphabet = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}
 
 
def generate_table(key):
    return [alphabet[char] for char in key.upper()]
 
 
def encrypt(key, words):
    cipher = ""
    count = 0
    table = generate_table(key)
    for char in words.upper():
        cipher += get_opponent(table[count], char)
        count = (count + 1) % len(table)
    return cipher
 
 
def decrypt(key, words):
    return encrypt(key, words)
 
 
def get_position(table, char):
    if char in table[0]:
        row = 0
    else:
        row = 1 if char in table[1] else -1
    return (None, None) if row == -1 else (row, table[row].index(char))
 
 
def get_opponent(table, char):
    row, col = get_position(table, char.upper())
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char
 
 

import os
while True:
    os.system('clear')
    print('''

      █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ 
      █▄▄█ █  █ █▄▄▀   █   █▄▄█ 
      ▀    ▀▀▀▀ ▀ ▀▀   ▀   ▀  ▀ ''')
    print('''
        {1}--Encrypt to Porta
        {2}--Decrypt Porta Cipher
    ''')
    vminp= input(' DramaX:Porta> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ')
        Key=  input(' Enter Key:  ')
        if Word and Key:
            print(encrypt(Key,Word))
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key=    input(' Enter Key:          ')
        if Cipher and Key:
            print(' '+decrypt(Key,Cipher)+'\n')
    os.system('pause')