lookup= {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
         'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
         'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
         'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
         'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'} 
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if(letter != ' '):
            cipher += lookup[letter] 
        else:
            cipher += ' '
    return cipher 

def decrypt(message): 
    decipher = '' 
    i = 0
    while True :
        if(i < len(message)-4):
            substr = message[i:i + 5]
            if(substr[0] != ' '):
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)] 
                i += 5
            else: 
                decipher += ' '
                i += 1
        else: 
            break
    return decipher 
  

import os
while True:
    os.system('clear')
    print('''

      █▀▀▄ █▀▀█ █▀▀ █▀▀█ █▀▀▄ ▀█▀ █▀▀█ █▀▀▄
      █▀▀▄ █▄▄█ █   █  █ █  █  █  █▄▄█ █  █
      ▀▀▀  ▀  ▀ ▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀ ▀  ▀ ▀  ▀  ''')
    print('''
        {1}--Encrypt to Baconian
        {2}--Decrypt Baconian Cipher
     ''')
    vminp= input(' DramaX:Baconian> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ').upper()
        if Word:
            print(f' Encrypted is:  {encrypt(Word)}\n')
            os.system('pause')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        if Cipher:
            try:
                print(f' Decrypted is:  {decrypt(Cipher)}\n')
            except:
                print(' Incorrect Cipher Text.\n')
            os.system('pause')