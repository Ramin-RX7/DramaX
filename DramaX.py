import hashlib
import os

try:
    import rx7 as rx
    import xxhash
    import pymmh3
except ModuleNotFoundError:
    rx.style.print('Module Not Found Error','red',style='bold')
    print('Install the requirements modules first: ')
    print('rx7\nxxhash\npymmh3')

from LIB.Cipher import CIPHERS_LIST,CIPHERS_DICT
from LIB.Functions import pause

print = rx.style.print

PC_LOGO='''
        8888888b.                                         Y88b   d88P
        888  "Y88b                                         Y88b d88P 
        888    888                                          Y88o88P  
        888    888 888d888 8888b.  88888b.d88b.   8888b.     Y888P   
        888    888 888P"      "88b 888 "888 "88b     "88b    d888b   
        888    888 888    .d888888 888  888  888 .d888888   d88888b  
        888  .d88P 888    888  888 888  888  888 888  888  d88P Y88b 
        8888888P"  888    "Y888888 888  888  888 "Y888888 d88P   Y88b
'''
COLORS= {'Yellow':['yellow','gold_1'], 'Blue':['blue','dodger_blue_2'],
         'Red':['red','red_1'],        'Green':['green','green_3a'],
         'Classic':['grey_46','default']}
COLORS_NESBAT= ['Yellow', 'Yellow', 'Blue', 'Red','Red', 'Classic','Classic']


def ce(msg='Wrong Command',color='default'):
    if msg:
     rx.style.print(msg,color)
    import os
    os.system('pause')     
    #getpass.getpass('Press Enter to Continue')
    #rx.cls()
    #MAIN()
 
def MAIN():
    rx.cls()
    COLOR= COLORS[rx.random.choose(COLORS_NESBAT)] #list(COLORS.keys())
    rx.style.print(PC_LOGO,COLOR[0])
    rx.style.print('''
       {1}--Hash Actions
       {2}--Create Dictionary
       {3}--Ciphers
       {6}--Web Hacking (Comming Soon)

      {99}--EXIT\n''',COLOR[1])
    
    '''
       {3}--Password Attacks
       {4}--Wireless Testing
       {5}--Exploitation Tools
       {6}--Sniffing & Spoofing
       {7}--Web Hacking
       {8}--Private Web Hacking
       {0}--Post Exploitation
      {11}--INSTALL & UPDATE
      {12}--CONTRIBUTORS    
    '''

    MAIN_INP= input(' DramaX> ')
    if   MAIN_INP== '1':
        #rx.cls()
        HASH_EX=False
        while not HASH_EX:
            rx.cls()
            print('''
             dMP dMP .aMMMb  .dMMMb  dMP dMP 
            dMP dMP dMP"dMP dMP" VP dMP dMP  
           dMMMMMP dMMMMMP  VMMMb  dMMMMMP   
          dMP dMP dMP dMP dP .dMP dMP dMP    
         dMP dMP dMP dMP  VMMMP" dMP dMP         

           {1}--Hash Decrypter
           {2}--File Hash Decrypter
           {3}--Hash Generator
           {3}--Hash Dictionary Creator
           ''')

            hinp= input('HASH>  ')
            if   hinp == '99':
                HASH_EX=True
            elif hinp == '1':
                os.system('python ".\\HashDecrypter.py"')
            elif hinp == '2':
                os.system('python ".\\HashDecrypterFile.py"')
            elif hinp == '3':
                os.system('python ".\\HashGenerator.py"')

    elif MAIN_INP=='2':
        os.system('python ".\\DictionaryCreator.py"')
    
    elif MAIN_INP=='3':
        CIPHER_EX=False
        while not CIPHER_EX:
            CIPHER_EX=CIPHERS()

    elif MAIN_INP=='6':
        rx.cls()
        print('Under Maintaince...')
        print('Comming Soon...')
        ce('')
        #os.system('python ".\\Web-Attack\\WPHF.py"')

    elif MAIN_INP in ('99','x'):
        exit()
    else:
        MAIN()


def CIPHERS():
    rx.cls()
    print('''
      ██████╗ ██╗ ██████╗  ██╗  ██╗ ███████╗ ██████╗  ███████╗
     ██╔════╝ ██║ ██╔══██╗ ██║  ██║ ██╔════╝ ██╔══██╗ ██╔════╝
     ██║      ██║ ██████╔╝ ███████║ █████╗   ██████╔╝ ███████╗
     ██║      ██║ ██╔═══╝  ██╔══██║ ██╔══╝   ██╔══██╗ ╚════██║
     ╚██████╗ ██║ ██║      ██║  ██║ ███████╗ ██║  ██║ ███████║
      ╚═════╝ ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚══════╝ 
     ''')
    print('UNDER MAINTAINCE...','red')
    pause()
    return True
    cipher_options = ""
    i = 1
    for cipher in CIPHERS_LIST:
        option = f"{i}-{cipher}"
        white_space = (30-len(option))*' '
        cipher_options += option+white_space
        i += 1
        if i%3==1:
            cipher_options += '\n'
    print(cipher_options)
    cinp= rx.io.selective_input(' DramaX:Ciphers> ',list(str(i) for i in range(1,len(CIPHERS_LIST)+1))+['99'],error=True)
    if cinp=='99':
        return True
    elif cinp:
        edt = rx.io.selective_input('Type [ENCRYPT/decrypt]:  ',['encrypt','decrypt','e','n','1','2'],error=True)
        word = 'Encrypted String'  if edt in ('d','2','decrypt')  else 'Word to Encrypt'
        inp = rx.io.wait_for_input(f'Enter {word}:')
        pause()
    else:
        CIPHERS()
 

while True:
    MAIN()
