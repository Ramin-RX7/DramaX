import hashlib,getpass,os
import rx7 as rx

print('''
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
''')

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

dichash={'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}
COLORS= {'Yellow':['yellow','gold_1'], 'Blue':['blue','dodger_blue_2'],
         'Red':['red','red_1'],        'Green':['green','green_3a'],
         'Classic':['grey_46','default']}
COLORS_NESBAT= ['Yellow', 'Yellow', 'Blue', 'Red','Red', 'Classic','Classic']


def ce(msg='Wrong Command',color='default'):
    if msg:
     rx.style.print(msg,color)
     print('Press Enter to Continue...')
     import getpass
     getpass.getpass('')
     os.system('clear')
    #getpass.getpass('Press Enter to Continue')
    #rx.cls()
    #MAIN()

def MAIN():
    #rx.cls()
    os.system('clear')
    COLOR= COLORS[rx.rand.choice(COLORS_NESBAT)] #list(COLORS.keys())
    rx.style.print(PC_LOGO,COLOR[0])
    rx.style.print('''
       {1}--Hash Actions
       {2}--Create Dictionary (Not Selectable in Termux)

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
        print('''
       {1}--Hash Decryptor
       {2}--File Hash Decryptor
       {3}--Hash Generator        
        ''')
        hinp= input('HASH>  ')
        if   hinp == '1':
            os.system('python "HD.py"')
        elif hinp == '2':
            ce("File Hash Decryptor isn't supported in Termux",'light_red')
            os.system('clear')            
        elif hinp=='3':
            inp= input('Enter String to Create Hashes:  ')
            if not inp or inp=='99':
                return False
            else:
                os.system('python "HG.py" '+inp)
    elif MAIN_INP=='3':
        #os.system('python "DC.py"')
        ce("Dictionary Creator isn't supported in Termux",'light_red')
        os.system('clear')
    elif MAIN_INP in ('99','x'):
        exit()
    else:
        MAIN()


while True:
    MAIN()
