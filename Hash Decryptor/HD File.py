import rx7 as rx
import hashlib

dichash={'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}
# Reading Word Files
ENGLISH= rx.read('english.txt')
ENGLISH= ENGLISH.split('\n')
###
TenK_MCP= rx.read('10k mcp.txt')
TenK_MCP= TenK_MCP.split('\n')
###


def HASH_DECRYPT():
    global TIME
    TIME= rx.record()
    rx.cls()
    rx.style.print('''
           88  88    db    .dP"Y8 88  88    888888 88 88     888888
           88  88   dPYb   `Ybo." 88  88    88__   88 88     88__  
           888888  dP__Yb  o.`Y8b 888888    88""   88 88  .o 88""  
           88  88 dP""""Yb 8bodP' 88  88    88     88 88ood8 888888

     8888b.  888888  dP""b8 88""Yb d88   88b 88""Yb 888888  dP"Yb  88""Yb
      8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   dP   Yb 88__dP
      8I  dY 88""   Yb      88"Yb     l8l    88"""    88   Yb   dP 88"Yb 
     8888Y"  888888  YboodP 88  Yb    d8b    88       88    YbodP  88  Yb
     ''','gold_3b')

    global HASHES
    FILE= input('Enter Filename:  ')
    if FILE in ('x','99'):
        exit()
    if rx.files.isfile(FILE):
        HASHES= rx.read(FILE).split('\n')
    #CHECK=0
    global FOUND
    FOUND=[]
    for HASH in HASHES:
        #if CHECK<len(HASHES): CHECK+=1
        #else: raise ValueError
        if len(HASH) in (40,56,64,96,128,32):
            if len(HASH) == 32:
                mi='1'
            elif len(HASH) == 40:
                mi='2'
            elif len(HASH) == 56:
                mi='3'
            elif len(HASH) == 64:
                mi='4'
            elif len(HASH) == 96:
                mi='5'
            elif len(HASH) == 128:
                mi='6'
            print('Hash Type Has Been Recognized.  (',end='')
            rx.style.print(str(dichash[mi]),'green',end='')
            print(')')
        else:
            print("Couldn't Recognize Hash Type",end='')

        '''def CSS(*ss):
            print('Choose Sample Space:')
            lst=[]
            for item in ss:
                lst.append(bool(input(item+': ')))
            return lst
        SS= CSS('ENGLISH DICTIONARY','10K MOST COMMON PASSWORDS','NUMBERS')'''
        SS=[True,True,True]
        rang=10000


        if mi=='1':
            find=False
            if SS[0]:
                WORD=rx.read(f'./ENG/eh_md5.txt')
                WORDS= WORD.split('\n')
                try:
                    word=ENGLISH[WORDS.index(HASH)]
                    print('Decrypted String is:  ',end='')
                    rx.style.print(word,color='green')
                    find=True
                    FOUND.append('x')
                except:
                    pass

            if SS[1] and not find:
                WORD=rx.read(f'./10kmcp/10kmcp_md5.txt')
                WORDS= WORD.split('\n')
                try:
                    word=TenK_MCP[WORDS.index(HASH)]
                    print('Decrypted String is:  ',end='')
                    rx.style.print(word,color='green')
                    find=True
                    FOUND.append('x')
                except:
                    print()


            if SS[2] and not find:
                for word in range(int(rang)):
                    result = hashlib.md5(str(word).encode()) 
                    rh=result.hexdigest()
                    if rh==HASH:
                        find=True
                        FOUND.append('x')
                        print('Decrypted String is:  ',end='')
                        rx.style.print(word,color='green')

            if not find:
                rx.style.print('Not Found','light_red')

        if int(mi) in range(2,7):
            def decsha(nom,File):
                if File== 'ENG':
                    if not nom:  
                        WORD=rx.read(f'./ENG/eh_{dichash[mi]}.txt')
                    else:
                        if len(mi)==6:
                            WORD=rx.read(f'./ENG/eh_sha3-{dichash[mi][-3:]}.txt')
                        else: return False
                if File== '10K MCP':
                    if not nom:  
                        WORD=rx.read(f'./10kmcp/10kmcp_{dichash[mi]}.txt')
                    else:    
                        WORD=rx.read(f'./10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt')
                WORDS= WORD.split('\n')
                try:
                    word=ENGLISH[WORDS.index(HASH)] if File=='ENG' else TenK_MCP[WORDS.index(HASH)]
                    print('Decrypted String is:  ',end='')
                    rx.style.print(str(word),color='green')
                    FOUND.append('x')
                    return True
                except:
                    return False
            x=False  
            if SS[0]:
                x= decsha(0,'ENG')
                if not x and len(dichash[mi])==6:
                    x= decsha(1,'ENG')
            if SS[1] and not x:
                x= decsha(0,'10K MCP')
                if not x and len(dichash[mi])==6:
                    x= decsha(1,'10K MCP')
            if SS[2] and not x:
                if mi=='2':
                    enc=hashlib.sha1
                if mi=='3':
                    enc= hashlib.sha224
                    enc2=hashlib.sha3_224
                if mi=='4':
                    enc=hashlib.sha256
                    enc2=hashlib.sha3_256
                if mi=='5':
                    enc=hashlib.sha384
                    enc2=hashlib.sha3_384
                if mi=='6':
                    enc=hashlib.sha512
                    enc2=hashlib.sha3_512
                for word in range(int(rang)):
                    result= enc(str(word).encode()) 
                    result2=enc2(str(word).encode())
                    rh= result.hexdigest()
                    rh2=result2.hexdigest()
                    #print(rh)
                    if rh==HASH or rh2==HASH:
                        print('Decrypted String is:  ',end='')
                        rx.style.print(word,color='green')
                        x=True
                        FOUND.append('x')
                        break
            if not x:
                rx.style.print('Not Found','light_red')
        print(40*'―')
    rx.style.switch('dodger_blue_2')
    print(f'Finnished At {round(TIME.lap(),3)}')
    print(f'Decrypted {len(FOUND)} from {len(HASHES)}')
    print(f'Success Rate: {round(len(FOUND)/len(HASHES)*100,2)}%')
    rx.style.switch_default()
    rx.p()
    os.system('pause')

import os
while True:
    try:
        HASH_DECRYPT()
    except EOFError:          exit()
    except KeyboardInterrupt: exit()
    except:                   pass
