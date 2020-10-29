'''
Case Sensetive.
Support Numbers and Symbols.
Key Must be an Integer Lower Than Word Length and Higher than 1.
'''


def encryptRailFence(text, key):  
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)):
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down
        rail[row][col] = text[i] 
        col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 


def decryptRailFence(cipher, key): 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False 
        rail[row][col] = '*'
        col += 1 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 
  
import os
while True:
    os.system('clear')
    print('''

       █▀▀█ █▀▀█ ▀█▀ █     █▀▀ █▀▀ █▀▀▄ █▀▀ █▀▀
       █▄▄▀ █▄▄█  █  █     █▀▀ █▀▀ █  █ ▀▀█ █▀▀
       ▀ ▀▀ ▀  ▀ ▀▀▀ ▀▀▀   ▀   ▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀   (Zig-Zag) ''')
    print('''
        {1}--Encrypt to Zig-Zag
        {2}--Decrypt Zig-Zag Cipher
    ''')
    vminp= input(' DramaX:Rail_Fense> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input(' Type Word:  ')
        Key=  input(' Enter Key:  ')
        if Word and Key:
            print(encryptRailFence(Word,int(Key))+'\n')
    if vminp=='2':
        Cipher= input(' Type Cipher Text:   ')
        Key=    input(' Enter Key:          ')
        if Cipher and Key:
            print(decryptRailFence(Cipher,int(Key))+'\n')
    os.system('pause')
