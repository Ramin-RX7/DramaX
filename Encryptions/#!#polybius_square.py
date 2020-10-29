def polybiusCipher(s):   
    # convert each character to its encrypted code 
    ret=''
    for char in s: 
        row = int((ord(char) - ord('a')) / 5) + 1
        col = ((ord(char) - ord('a')) % 5) + 1
        # if character is 'k' 
        if char == 'k': 
                row = row - 1
                col = 5 - col + 1                          
        # if character is greater than 'j' 
        elif ord(char) >= ord('j'): 
                if col == 1 : 
                    col = 6
                    row = row - 1
                      
                col = col - 1

        ret+=str(row)+str(col)
    return ret
  
def Decrypt(cipher):
    if not len(cipher)%2:
        out = [(cipher[i:i+2]) for i in range(0, len(cipher), 2)] 
    else:
        return 'Wrong Cipher Text Was Given.'
        
    #4211322433
    for rc in out:
        row,col= rc[0],rc[1]
        



import os
while True:
    os.system('clear')
    print('''
     █▀▀█ █▀▀█ █   █  █ █▀▀▄ ▀█▀ █  █ █▀▀    █▀▀ █▀▀█ █  █ █▀▀█ █▀▀█ █▀▀
     █  █ █  █ █   █▄▄█ █▀▀▄  █  █  █ ▀▀█    ▀▀█ █ ▄█ █  █ █▄▄█ █▄▄▀ █▀▀
     █▀▀▀ ▀▀▀▀ ▀▀▀ ▄▄▄█ ▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀    ▀▀▀ ▀▀▀█  ▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀
     ''')
    print('''
        {1}--Encrypt to  Polybius Square
        {2}--Decrypt  Polybius Square  Cipher  (Under Maintaince)
    ''')
    vminp= input('DramaX:Polybius_Square> ')
    print()
    if vminp=='99':
        exit()
    if vminp=='1':
        Word= input('Type Word:  ')
        if Word:
            print(polybiusCipher(Word)+'\n')
    if vminp=='2':
        print('Under Maintaince\n')
        Cipher= input('Type Cipher Text:   ')
        if Cipher:
            print(str(Decrypt(Cipher))+'\n')

    os.system('pause')

