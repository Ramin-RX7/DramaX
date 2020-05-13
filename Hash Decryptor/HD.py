import hashlib,os
import rx7 as rx


def HD_SETTING():
    try:
        rx.read('./HD Dictionary/english.txt').split('\n')
        HaDe=''
    except:
        HaDe='/Hash Decryptor'    
    hdex=False
    def get_size(start_path = '.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size    
    while not hdex:
     rx.cls()
     print('''
      █  █    █▀▀▄          █▀▀ █▀▀ ▀▀█▀▀ ▀▀█▀▀ ▀█▀ █▀▀▄ █▀▀▀
      █▀▀█ash █  █ecryptor  ▀▀█ █▀▀   █     █    █  █  █ █ ▀█
      ▀  ▀    ▀▀▀           ▀▀▀ ▀▀▀   ▀     ▀   ▀▀▀ ▀  ▀ ▀▀▀▀
     ''')
     print('''
     {1} Create All "ENGLISH DICTIONARY" Files
     {2} Create All "10K Most Common Passwords" Files
     {3} REMOVE ALL  HASH DICTIONARIES (Freeup +%sMB)
      ''' % str((get_size(f'.{HaDe}/HD Dictionary/ENG')+get_size(f'.{HaDe}/HD Dictionary/10kmcp'))//10**6))
     HDSI= input('HD:SETTING> ')
     if HDSI=='1':
         MYN= input('INCLUDE "ENGLISH DICTIONARY 2" (y/n)? ')
         os.system(f'python ".{HaDe}/HC full.py" ".{HaDe}/HD Dictionary/english.txt" "eh" ".{HaDe}/HD Dictionary/ENG/"')
         rx.style.print("ENGLISH DICTIONARY  files have been successfully created",'green')
         if MYN.lower()=='y':
             os.system(f'python ".{HaDe}/HC full.py" ".{HaDe}/HD Dictionary/english_more.txt" "ehm" ".{HaDe}/HD Dictionary/ENG/MORE/"')
             rx.style.print("ENGLISH DICTIONARY 2  files have been successfully created",'green')
         print('Done.')
         hdex= True
     elif HDSI=='2':
         try:
             rx.read('./HD Dictionary/english.txt').split('\n')
             HaDe=''
         except:
             HaDe='/Hash Decryptor'
         os.system(f'python ".{HaDe}/HC full.py" ".{HaDe}/HD Dictionary/10k mcp.txt" "10kmcp" ".{HaDe}/HD Dictionary/10kmcp/"')
         rx.style.print("ENGLISH DICTIONARY  files have been successfully created",'green')
         print('Done.')
         hdex= True  
         import math
         math.inf
     elif HDSI=='3':
        rx.files.remove(f'.{HaDe}/HD Dictionary/ENG')   
        os.mkdir(f'.{HaDe}/HD Dictionary/ENG') 
        os.mkdir(f'.{HaDe}/HD Dictionary/ENG/MORE') 
        rx.files.remove(f'.{HaDe}/HD Dictionary/10kmcp') 
        os.mkdir(f'.{HaDe}/HD Dictionary/10kmcp')     
     #os.system('pause')

def ce(msg='',color='light_red'):
    rx.style.print(msg,color)

dichash={'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}
def HASH_DECRYPT():
    # Reading Word Files
    try:
        ENGLISH= rx.read('./HD Dictionary/english.txt').split('\n')
        ENGLISH_MORE= rx.read(f'./HD Dictionary/english_more.txt').split('\n')
        HaDe=''
    except:
        ENGLISH= rx.read('./Hash Decryptor/HD Dictionary/english.txt').split('\n')
        ENGLISH_MORE= rx.read(f'./Hash Decryptor/HD Dictionary/english_more.txt').split('\n')  
        HaDe='/Hash Decryptor'

    TenK_MCP= rx.read(f'.{HaDe}/HD Dictionary/10k mcp.txt').split('\n')

    ###########


    rx.cls()
    rx.style.print('''
                        88  88    db    .dP"Y8 88  88
                        88  88   dPYb   `Ybo." 88  88
                        888888  dP__Yb  o.`Y8b 888888
                        88  88 dP""""Yb 8bodP' 88  88

     8888b.  888888  dP""b8 88""Yb d88   88b 88""Yb 888888  dP"Yb  88""Yb
      8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   dP   Yb 88__dP
      8I  dY 88""   Yb      88"Yb     l8l    88"""    88   Yb   dP 88"Yb 
     8888Y"  888888  YboodP 88  Yb    d8b    88       88    YbodP  88  Yb
     ''','gold_3b')
    # cfa5301358b9fcbe7aa45b1ceea088c6
    # a1b7f6c7d739aa48d5dfaacf54df3994
    # 9fba371af0e963d79e5d5580da47c8c0c310a707

    HASH= input('Enter Hashed String:  ')
    
    if HASH in ('99','x'):
        #MAIN()
        global EX
        EX= False
        return True
    if HASH.lower() in ('setting','set'):
        HD_SETTING()
        return True
    print('\nRecognizing Hash Type...')
    if len(HASH) in (40,56,64,96,128,32):
        if len(HASH) == 32:
            mi='1'
        if len(HASH) == 40:
            mi='2'
        if len(HASH) == 56:
            mi='3'
        if len(HASH) == 64:
            mi='4'
        if len(HASH) == 96:
            mi='5'
        if len(HASH) == 128:
           mi='6'
        print('Found.  (',end='')
        rx.style.print(str(dichash[mi]),'green',end='')
        print(')\n')
    else:
       ce('Couldnt Recognize the Hash Type.\n','light_red')
       return True

    #SS= input('Choose Sample Space: \n1- ENGLISH DICTIONARY\n2- NUMBERS\n>')
    def CSS(*ss):

        import win32console
        _stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
        def input_def(prompt, default='T'):
            keys = []
            for c in default:
                evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
                evt.Char = c
                evt.RepeatCount = 1
                evt.KeyDown = True
                keys.append(evt)

            _stdin.WriteConsoleInput(keys)
            return input(prompt)

        print('Choose Sample Space:')
        lst=[]
        for item in ss:
            #lst.append(bool(input_def(item+': ')))
            lst.append(input_def(item+': '))
            if lst[-1] in ('99','x'):
                return False
        return lst
    SS= CSS('ENGLISH DICTIONARY','More on ENG DICT','10K MOST COMMON PASSWORDS','NUMBERS')
    if not SS or 'x' in SS or '99' in SS:
        return False
    WORDS=[]
    if SS[3]:
        try:     
            rang= int(input('Type Last Number: '))
        except:  
            ce('Number Should be Integer')
            return True
            
    #find=False
    if mi=='1':
        find=False
        if SS[0].lower() in ('t','true'):
            try:
                WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_md5.txt').split('\n')
            except:
                print('Loading "ENGLISH DICTIONARY" Database...')
                os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english.txt" ".{HaDe}/HD Dictionary/ENG/eh_md5.txt" md5')
                WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_md5.txt').split('\n')
                rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/eh_md5.txt')

            ENGLISH_LST= ENGLISH
            if SS[1].lower() in ('t','true'):
                try:
                    WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_md5.txt').split('\n')
                except:
                    print('Loading "ENGLISH DICTIONARY 2" Database...')
                    os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english_more.txt" ".{HaDe}/HD Dictionary/ENG/MORE/ehm_md5.txt" md5')
                    WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_md5.txt').split('\n')
                    rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_md5.txt')
                ENGLISH_LST+= ENGLISH_MORE
            try:
                word=ENGLISH_LST[WORDS.index(HASH)]
                rx.style.print('Found',color='green')
                print('Decrypted String is:  ',end='')
                rx.style.print(word,color='green',end='\n\n')
                find=True
                ce('')
                return True
            except:
                rx.style.print('Word Not Found in English Dictionary!',color='light_red')

        if SS[2].lower() in ('t','true') and not find:
            try:
                WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_md5.txt').split('\n')   
            except:
                rx.style.print('Loading "10K Most Common Password" Database...','light_blue')
                os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/10k mcp.txt" ".{HaDe}/HD Dictionary/10kmcp/10kmcp_md5.txt" md5')
                WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_md5.txt').split('\n')
                rx.files.remove(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_md5.txt')
   
            try:
                word=TenK_MCP[WORDS.index(HASH)]
                rx.style.print('Found',color='green')
                print('Decrypted String is:  ',end='')
                rx.style.print(word,color='green',end='\n\n')
                find=True
                #ce('')
                return False
            except:
                #raise
                rx.style.print('Word Not Found in 10K MOST COMMON PASSWORDS!',color='light_red')

        if SS[3].lower() in ('t','true') and not find:
            for word in range(int(rang)):
                result = hashlib.md5(str(word).encode()) 
                rh=result.hexdigest()
                if rh==HASH:
                    find=True
                    rx.style.print('Done.',color='green')
                    print('Decrypted String is:  ',end='')
                    rx.style.print(word,color='green',end='\n\n')
                    ce('')
                    return True

        if not find:
            ce('Not Found',color='red')
            return False
            

    if int(mi) in range(2,7):
        WORDS=[]
        def decsha(nom,File):
            if File== 'ENG':
                ENGLISH_LST= ENGLISH
                if not nom:
                    try:
                        WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_{dichash[mi]}.txt').split('\n')
                    except:
                        rx.style.print('Loading "ENGLISH DICTIONARY" Database...','blue')
                        os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english.txt" ".{HaDe}/HD Dictionary/ENG/eh_{dichash[mi]}.txt" {dichash[mi]}')
                        WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_{dichash[mi]}.txt').split('\n')
                        rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/eh_{dichash[mi]}.txt')

                    if SS[1]:
                        try:
                            WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_{dichash[mi]}.txt').split('\n')
                        except:
                            rx.style.print('Loading "ENGLISH DICTIONARY 2" Database...','blue')
                            os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english_more.txt" ".{HaDe}/HD Dictionary/ENG/MORE/ehm_{dichash[mi]}.txt" {dichash[mi]}')
                            WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_{dichash[mi]}.txt').split('\n') 
                            rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_{dichash[mi]}.txt')
                        ENGLISH_LST+=ENGLISH_MORE                   
                else:
                    try:
                        try:
                            WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt').split('\n')
                        except:
                            #print('Loading "ENGLISH DICTIONARY" Database...')
                            os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english.txt" ".{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt" sha3_{dichash[mi][-3:]}')
                            WORDS=rx.read(f'.{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt').split('\n')
                            rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt')
                    except:
                        return False
                    if SS[1]: 
                        try:
                           WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_sha3-{dichash[mi][-3:]}.txt').split('\n')
                        except:
                            #print('Loading "ENGLISH DICTIONARY" Database...')
                            os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/english.txt" ".{HaDe}/HD Dictionary/ENG/MORE/ehm_sha3-{dichash[mi][-3:]}.txt" sha3_{dichash[mi][-3:]}')
                            WORDS+=rx.read(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_sha3-{dichash[mi][-3:]}.txt').split('\n')
                            rx.files.remove(f'.{HaDe}/HD Dictionary/ENG/MORE/ehm_sha3-{dichash[mi][-3:]}.txt')
                        ENGLISH_LST+=ENGLISH_MORE                
            if File== '10K MCP':
                if not nom:
                    try:
                        WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_{dichash[mi]}.txt').split('\n') 
                    except:
                        rx.style.print('Loading "10K Most Common Passwords" Database...','light_blue')
                        os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/10k mcp.txt" ".{HaDe}/HD Dictionary/10kmcp/10kmcp_{dichash[mi]}.txt" {dichash[mi]}')
                        WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_{dichash[mi]}.txt').split('\n') 
                        rx.files.remove(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_{dichash[mi]}.txt')
                else:    
                    try:
                        try:
                            WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt').split('\n') 
                        except:
                            #print('Loading "ENGLISH DICTIONARY" Database...')
                            os.system(f'python ".{HaDe}/createHash.py" ".{HaDe}/HD Dictionary/10k mcp.txt" ".{HaDe}/HD Dictionary/ENG/eh_sha3-{dichash[mi][-3:]}.txt" sha3_{dichash[mi][-3:]}')
                            WORDS=rx.read(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt').split('\n') 
                            rx.files.remove(f'.{HaDe}/HD Dictionary/10kmcp/10kmcp_sha3-{dichash[mi][-3:]}.txt')
                    except:
                        return False

            try:
                word=ENGLISH_LST[WORDS.index(HASH)] if File=='ENG' else TenK_MCP[WORDS.index(HASH)]
                rx.style.print('Found','green')
                print('Decrypted String is:  ',end='')
                rx.style.print(str(word),color='green',end='')
                if len(dichash[mi])==6:
                    typee= f'sha2-{dichash[mi][-3:]}' if not nom else f'sha3-{dichash[mi][-3:]}'
                    rx.style.print(f'  ({typee})','dodger_blue_2',end='\n\n')
                ce('')
                return True
            except:
                return False
        x=False  
        if SS[0]:
            x= decsha(0,'ENG')
            if not x:
                rx.style.print('Word Not Found in 1st Try in English Dictionary','light_red')
                x= decsha(1,'ENG')
            if not x:
                rx.style.print('Word Not Found in 2nd Try in English Dictionary','light_red')
        if SS[2] and not x:
            x= decsha(0,'10K MCP')
            if not x:
                rx.style.print('Word Not Found in 1st Try in 10K MCP','light_red')
                x= decsha(1,'10K MCP')
            if not x:
                rx.style.print('Word Not Found in 2nd Try in 10K MCP','light_red')
        if SS[3] and not x:
            if mi=='2':
                enc=hashlib.sha1
                #enc2=''
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
                rh= result.hexdigest()
                try:
                    result2=enc2(str(word).encode())
                    rh2=result2.hexdigest()
                except: rh2=''
                #print(rh)
                if rh==HASH or rh2==HASH:
                    rx.style.print('Found','green')
                    print('Decrypted String is:  ',end='')
                    rx.style.print(word,color='green',end='')
                    if len(dichash[mi])==6:
                        typee= f'sha2-{dichash[mi][-3:]}' if rh==HASH else f'sha3-{dichash[mi][-3:]}'
                        rx.style.print(f'  ({typee})','dodger_blue_2',end='\n\n')
                    x=True
                    ce('')
            if not x:
                rx.style.print('Word Not Found in Numbers')
        if not x:
            ce('Not Found',color='red')
    #ce('')


EX= True
while EX:
    HASH_DECRYPT()
    if EX:
        os.system('pause')
