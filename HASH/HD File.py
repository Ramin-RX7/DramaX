import rx7 as rx
import hashlib,sys,os

dichash={'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}
try:
    ENGLISH= rx.read('./HASH/HD Dictionary/english.txt').split('\n')
    HaDe= '/HASH'
except:
    ENGLISH= rx.read('./HD Dictionary/english.txt').split('\n')
    HaDe= ''

print('Preparing Databases...')
ENGLISH_MORE= rx.read(f'.{HaDe}/HD Dictionary/english_more.txt').split('\n')
TENKMCP= rx.read(f'.{HaDe}/HD Dictionary/english_more.txt').split('\n')

ALL= ENGLISH+ENGLISH_MORE+TENKMCP

MD5=[hashlib.md5(bytes(word, encoding='utf-8')).hexdigest() for word in ALL]  


sa={'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha224':hashlib.sha224,'sha256':hashlib.sha256,
    'sha384':hashlib.sha384,'sha512':hashlib.sha512,'sha3_224':hashlib.sha3_224,
    'sha3_256':hashlib.sha3_256, 'sha3_384':hashlib.sha3_384,'sha3_512':hashlib.sha3_512}


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

    
    FILE= input('Enter Filename:  ') if len(sys.argv)==1 else sys.argv[1]
    if FILE in ('x','99'):
        hdr=False
        #exit()
    print(f'Analysing {os.path.basename(FILE)}...')
    if rx.files.isfile(FILE):# and rx.files.size(FILE)//10**6<75:
        HASHES= rx.read(FILE).split('\n')
        rx.style.print('Completed.','green')
    else:
        rx.style.print("Operation Failed.",'red')
        os.system('pause')
        return False
    print('============================')

    BL=0
    global FOUND
    FOUND=[]

    for HASH in HASHES:
        print(HASH)
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
            if len(HASH) and HASH != ' ':
                print("Couldn't Recognize Hash Type",end='')
            else:
                pass

        if mi=='1':
            find=False         
            try:
                DEC=ALL[MD5.index(HASH)]
                print('Decrypted String is:  ',end='')
                rx.style.print(DEC,color='green')
                find=True
                FOUND.append('x')                    
            except:
                pass
            rang=10000
            if not find:
                for nom in range(int(rang)):
                    result = hashlib.md5(str(nom).encode()) 
                    rh=result.hexdigest()
                    if rh==HASH:
                        find=True
                        FOUND.append('x')
                        print('Decrypted String is:  ',end='')
                        rx.style.print(nom,color='green')

            if not find:
                if len(HASH) and HASH != ' ':
                    rx.style.print('Not Found','light_red')
                else:
                    rx.style.print('Line Found With No Character','light_red')
                    BL+=1


        if int(mi) in range(2,7):

           try:
                crypt= sa[dichash[mi]]
                WORDS= [crypt(bytes(word, encoding='utf-8')).hexdigest() for word in ALL]
                DEC= ALL[WORDS.index(HASH)]
                print('Decrypted String is:  ',end='')
                rx.style.print(str(DEC),color='green')
                FOUND.append('x')
                find=True                

           except:
                try:
                    crypt= sa['sha3_'+dichash[mi][-3:]]   
                    WORDS= [crypt(bytes(word, encoding='utf-8')).hexdigest() for word in ALL]                    
                    DEC= ALL[WORDS.index(HASH)]
                    print('Decrypted String is:  ',end='')
                    rx.style.print(str(DEC),color='green')
                    FOUND.append('x')
                    find=True
                except:
                    if len(HASH) and HASH != ' ':
                        rx.style.print('Not Found','light_red')
                    else:
                        rx.style.print('Line Found With No Character','light_red')
                        BL+=1

           """def decsha(nom,File):
                if File== 'ENG':
                    if not nom:  
                        WORD=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_{dichash[mi]}.txt')
                    else:
                        if len(mi)==6:
                            WORD=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt')
                        else: return False
                if File== '10K MCP':
                    if not nom:  
                        WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_{dichash[mi]}.txt')
                    else:    
                        WORD=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt')
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
                        break"""
            

        print(40*'―')
    rx.style.switch('dodger_blue_2')
    print(f'Finnished At {round(TIME.lap(),3)}')
    print(f'Decrypted {len(FOUND)} from {len(HASHES)-BL}')
    print(f'Success Rate: {round(len(FOUND)/(len(HASHES)-BL)*100,2)}%')
    rx.style.switch_default()
    rx.p()
    os.system('pause')


hdr=True
while hdr:
    try:
        HASH_DECRYPT()
    except EOFError:          exit()
    except KeyboardInterrupt: hdr=False
    except:                   pass
#HASH_DECRYPT()
