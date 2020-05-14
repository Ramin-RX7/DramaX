"""try:
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
         os.system(f'python ".{HaDe}/HC full.py" ".{HaDe}/HD Dictionary/10k mcp.txt" "10kmcp" ".{HaDe}/HD Dictionary/10kmcp/"')
         rx.style.print("ENGLISH DICTIONARY  files have been successfully created",'green')
         print('Done.')
         hdex= True
     elif HDSI=='3':
        try:
            rx.files.remove(f'.{HaDe}/HD Dictionary/ENG')   
            os.mkdir(f'.{HaDe}/HD Dictionary/ENG') 
            os.mkdir(f'.{HaDe}/HD Dictionary/ENG/MORE') 
        except FileNotFoundError: pass
        try:
            rx.files.remove(f'.{HaDe}/HD Dictionary/10kmcp') 
            os.mkdir(f'.{HaDe}/HD Dictionary/10kmcp')     
        except FileNotFoundError: pass
        rx.style.print('Done','green')
     #os.system('pause')"""