import sys
import argparse

import rx7.lite as rx

from LIB import Dictionary
from LIB.Functions import wait_for_input, get_files, pause


# TODO: add write to file directly

print = rx.style.print

BANNER = '''
    `7MM"""Yb.     .g8"""bgd  
     MM    `Yb.  .dP'     `M  
     MM     `Mb  dM'       `  
     MM      MM  MM           
     MM     ,MP  MM.          
     MM    ,dP'  `Mb.      ,' 
    .JMMmmmdP'     `"bmmmd'      

    '''



while True:
    
    rx.cls()

    print(BANNER,'gold_3b')
    exit()
    print('BECAREFULL WHEN USING THIS PROGRAM TO CREATE LARGE DICTIONARIES (MORE THAN 50M WORDS)!', 'red', style='bold')
    print('DO NOT TRY THIS FOR LARGE NUMBER OF WORDS (MORE THAN 100M WORDS)!\n', 'red', style='bold')


    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            'Dictionary Creator',
            description='Use this app to create dictionaries',
            allow_abbrev=False,
            )

        parser.add_argument('-c','--characters',
                            required=True, 
                            help='List of characters to use in Dictionary'
                            )
        parser.add_argument('-l','--length',
                            metavar='LENGTH', required=True, type=int, 
                            help='Max Words Length of Dictionary'
                            )
        parser.add_argument('path',metavar='PATH',
                            help='Path to a file to save dictionary')

        parser.add_argument('-I','--Ignore-Memory', action='store_true',
                            help='Ignore Memory Warnings and Errors',default=False)

        '''
        parser.add_argument('-s','--save-memory', action='store_true',
                            help='Save memory (Lower Speed)')
        '''

        args = parser.parse_args()


        SS = args.characters
        LENGTH = args.length
        FILE = args.path
        ignore_memory = args.Ignore_Memory
        #save_memory = args.save_memory


    
    else:
        SS = wait_for_input('Enter Characters to Start operation:  ')
        while True:
            LENGTH = wait_for_input('Enter Max Length of Dictionary:  ')
            try:
                LENGTH = int(LENGTH)
                assert LENGTH > 0
                break
            except:
                print('Length Should be an integer and higher than 0')
        FILE = get_files('Enter Path To save Dictionary:  ',
                        check_if_exists=False, times=1)[0]

        #< Check if file exists >#
        if rx.files.exists(FILE):
            print('[*] File Already Exists.', 'dodger_blue_1')
            replace = wait_for_input('Replace File? [Yes/No]  ')
            if not replace.lower() in ('y','yes'):
                print('[-] Operation Cancelled By User.', 'red')
                sys.exit()
        
        ignore_memory = False

        #save_memory = wait_for_input('Save Memory? [Yes/No]  ')

    TOTAL = 0
    ALL_CHARS = 0
    for i in range(1, LENGTH+1):
        TOTAL += len(SS)**i
        ALL_CHARS += len(SS)**i * (i+2)
    
    #< Checking Memory >#
    if ALL_CHARS*10+200000000 > int(rx.system.ram_free(False)):
        print('[-] NOT ENOUGH MEMORY TO START OPERATION', 'red')
        print(f'(This dictionary needs "{rx.convert_bytes(ALL_CHARS*10+200000000)}" But you have "{rx.system.ram_free()}")')
        pause()
        sys.exit()
    if ignore_memory  and  ALL_CHARS*10+1500000000 > int(rx.system.ram_total(False))//2:
        print('[*] This Dictionary Needs More than Half of Your Memory', 'red')
        sure = wait_for_input('Enter "yes" to Start [Yes/No]  ')
        if not sure.lower() in ('y','yes'):
            print('[-] Operation Cancelled By User.', 'red')
            sys.exit()

    rx.cls()

    print(BANNER,'gold_3b')

    print('Characters to use:  ', end='')
    print(SS, 'dodger_blue_1')

    print('Words Max Length:   ', end='')
    print(LENGTH, 'dodger_blue_1')

    #if not save_memory:
    print('Required Memory:    ', end='')
    print(rx.convert_bytes(ALL_CHARS*10+(ALL_CHARS*10)/2.5), 'dodger_blue_1')

    print()

    START = rx.record()
    DICT = []
    i = 1
    Progress = TOTAL//100#int(str(TOTAL//100)[:2]+'00')
    for word in Dictionary.dict_creator_generator(SS, LENGTH):
        DICT.append(word)
        i += 1
        if  i % Progress  ==  0:
            print('\r'+'[*] Generating Words:  '+str(i)+'/'+str(TOTAL),'dodger_blue_1', end='')
            '''
            if save_memory:
                rx.write(FILE,'\n'.join(DICT),'a','\n')
                DICT = []
            '''
    print('\r[*] Number of Generated Words:  '+str(TOTAL), 'dodger_blue_1')
    print(f'[*] Operation finnished in {START.lap(Round=4)} seconds', 'dodger_blue_1')
    rx.write(FILE, '\n'.join(DICT))
    print('[+] Dictionary File Has Been Created Successfully.', 'green')
    print(f'[*] (Address:  {rx.files.abspath(FILE)})', 'dodger_blue_1')
    del DICT

    print()

    pause('Press Enter To Exit ...')
    sys.exit()
