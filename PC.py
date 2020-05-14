import hashlib,getpass,os
import rx7 as rx

"""print('''
                        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   
                    ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶                
                  ¶¶¶¶                       ¶¶¶¶              
                 ¶¶¶                           ¶¶¶            
                ¶¶                               ¶¶           
               ¶¶                                 ¶¶          
              ¶¶                                   ¶¶          
              ¶¶ ¶¶                             ¶¶ ¶¶          
              ¶¶ ¶¶                             ¶¶ ¶¶          
              ¶¶ ¶¶                             ¶¶ ¶¶          
              ¶¶  ¶¶                           ¶¶  ¶¶          
              ¶¶  ¶¶                           ¶¶  ¶¶          
               ¶¶ ¶¶   ¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶   ¶¶ ¶¶           
               ¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶           
                 ¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶             
       ¶¶¶¶      ¶¶   ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶  ¶¶      ¶¶¶¶   
      ¶¶¶¶¶¶     ¶¶   ¶¶¶¶¶¶¶   ¶¶¶   ¶¶¶¶¶¶¶   ¶¶     ¶¶¶¶¶¶  
      ¶¶   ¶¶    ¶¶     ¶¶¶    ¶¶¶¶¶    ¶¶¶     ¶¶    ¶¶   ¶¶  
     ¶¶¶    ¶¶¶¶  ¶¶          ¶¶¶¶¶¶¶          ¶¶  ¶¶¶¶    ¶¶¶ 
    ¶¶         ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶        ¶¶
    ¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶
      ¶¶¶¶ ¶¶¶¶¶      ¶¶¶¶¶              ¶¶¶¶¶     ¶¶¶¶¶¶ ¶¶¶ 
             ¶¶¶¶¶¶  ¶¶¶  ¶¶            ¶¶  ¶¶¶  ¶¶¶¶¶¶        
                  ¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶              
                      ¶¶ ¶¶ ¶ ¶ ¶  ¶ ¶ ¶ ¶¶ ¶¶                 
                    ¶¶¶¶  ¶ ¶ ¶ ¶  ¶ ¶ ¶    ¶¶¶¶¶              
                ¶¶¶¶¶ ¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶ ¶¶¶¶¶            
        ¶¶¶¶¶¶¶¶¶¶     ¶¶                 ¶¶      ¶¶¶¶¶¶¶¶¶    
       ¶¶           ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶¶          ¶¶   
        ¶¶¶     ¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶     ¶¶¶    
          ¶¶   ¶¶¶           ¶¶¶¶¶¶¶¶¶           ¶¶¶   ¶¶      
          ¶¶  ¶¶                                   ¶¶  ¶¶      
           ¶¶¶¶                                     ¶¶¶¶   
''')"""

PC_LOGO='''
         8888888b.    .d8888b. 
         888   Y88b  d88P  Y88b
         888    888  888    888
         888   d88P  888       
         8888888P"   888       
         888         888    888
         888         Y88b  d88P
         888          "Y8888P" 
'''

dichash={'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}
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
    COLOR= COLORS[rx.rand.choice(COLORS_NESBAT)] #list(COLORS.keys())
    rx.style.print(PC_LOGO,COLOR[0])
    rx.style.print('''
       {1}--Hash Decryptor
       {2}--Hash Generator
       {3}--Create Dictionary

       {3}--Password Attacks
       {4}--Wireless Testing
       {5}--Exploitation Tools
       {6}--Sniffing & Spoofing
       {7}--Web Hacking
       {8}--Private Web Hacking
       {0}--Post Exploitation
      {11}--INSTALL & UPDATE
      {12}--CONTRIBUTORS
      {99}--EXIT\n''',COLOR[1])
    
    MAIN_INP= input('$ ')
    if   MAIN_INP== '1':
        HASH_DECRYPT()
    elif MAIN_INP=='2':
        HASH_GENERATE()
    elif MAIN_INP=='3':
        CREATE_DIC()
    elif MAIN_INP in ('99','x'):
        exit()
    else:
        MAIN()


def HASH_DECRYPT():
    os.system('python ".\\HASH\\HD.py"')


def CREATE_DIC():
    os.system('python ".\\HASH\\DC.py"')


def HASH_GENERATE():
    inp= input('Enter String to Create Hashes:  ')
    if not inp or inp=='99':
        return False
    else:
        os.system('python ".\\HASH\\HG.py" '+inp)




while True:
    MAIN()
