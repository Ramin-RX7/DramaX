import os
import sys
import argparse

import rx7 as rx

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from LIB import Dictionary
from LIB.Functions import pause



print = rx.style.print


BANNER = '''
    `7MM"""Yb.              .g8"""bgd
     MM    `Yb.           .dP'     `M
     MM     `Mb           dM'       `
     MM      MM           MM
     MM     ,MP           MM.
     MM    ,dP'           `Mb.     ,'
    .JMMmmmdP' ictionary   `"bmmmd' reator

    '''


# if __name__ == "__main__":
rx.cls()
print(BANNER,color='gold_3b')
print('BECAREFULL WHEN USING THIS PROGRAM TO CREATE LARGE DICTIONARIES'
      '(MORE THAN 50M WORDS)!',
      color='red', style='bold')
print('DO NOT TRY THIS FOR LARGE NUMBER OF WORDS (MORE THAN 100M WORDS)!',
      color='red', style='bold')
print()

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
                        help='Path to a file to save dictionary'
                        )
    parser.add_argument('-I','--Ignore-Memory', action='store_true',
                        help='Ignore Memory Warnings and Errors',
                        default=False)
    '''
    parser.add_argument('-s','--save-memory', action='store_true',
                        help='Save memory (Lower Speed)')
    '''
    args = parser.parse_args()

    SS = args.characters
    LENGTH = args.length
    FILE = args.path
    SAVE_MEMORY = not args.ignore_memory

else:
    SS = rx.io.wait_for_input('Enter Characters of Dictionary:  ')
    while True:
        LENGTH = rx.io.wait_for_input('Enter Max Length of Dictionary:  ')
        try:
            LENGTH = int(LENGTH)
            assert LENGTH > 0
            break
        except:
            print('Length Should be an integer and higher than 0')
    FILE = rx.io.wait_for_input("Enter Path To save Dictionary:  ")

    if rx.files.exists(FILE):
        print('[*] File Already Exists.', color='dodger_blue_1')
        replace = rx.io.wait_for_input('Replace File? [Yes/No]  ')
        if not replace.lower() in ('y','yes'):
            print('[-] Operation Cancelled By User.', color='red')
            sys.exit()

    SAVE_MEMORY = rx.io.selective_input('Save Memory? [Yes/No]  ',
                                        {"y":1,"yes":1,"n":0,"no":0},
                                        ignore_case=True)
# lines below are for test cases
# SS = "1234567890q"
# LENGTH = 7
# FILE = "y"
# save_memory = True


TOTAL = 0       # nom of words
ALL_CHARS = 0   # nom of all chars
MEM = 0
    # str:  empty:49    +1 per additional character (49+total length of characters)
    #list:  empty:56    +8 per additional item in a list ( 56 + 8*total length of characters )
for i in range(1, LENGTH+1):
    wwil = len(SS)**i  # words with i length
    TOTAL += wwil
    ALL_CHARS += len(SS)**i * (i+2)

    mem_str = 49 + i
    moil = 8*wwil + mem_str*wwil  # memory of i length
    MEM +=  moil
# print(ALL_CHARS)



#< Checking Memory >#
if MEM*1.5 > int(rx.system.ram_free(False)):
    print('[-] NOT ENOUGH MEMORY TO START OPERATION', color='red')
    print(f'(This dictionary needs "{rx.convert_bytes(ALL_CHARS*10+200000000)}"'
          f' "But you have "{rx.system.ram_free()}")')
    pause()

elif (not SAVE_MEMORY)  and  (MEM*1.5 > int(rx.system.ram_total(False))//2):
    print('[*] This Dictionary Needs More than Half of Your Memory',
          color='red')
    sure = rx.io.wait_for_input('Enter "yes" to Start [Yes/No]  ')
    if not  sure.lower() in ('y','yes'):
        print('[-] Operation Cancelled By User.', color='red')
        sys.exit()

rx.cls()

print(BANNER, color='gold_3b')

print('Characters to use:  ', end='')
print(SS, color='dodger_blue_1')

print('Words Max Length:   ', end='')
print(LENGTH, color='dodger_blue_1')

# if not save_memory:
print('Required Memory:    ', end='')
print(rx.convert_bytes(MEM*1.5),
      color='dodger_blue_1')

print()

START = rx.record()
DICT = []
i = 1
Progress = TOTAL//100#int(str(TOTAL//100)[:2]+'00')



for word in Dictionary.dict_creator_generator(SS, LENGTH):
    DICT.append(word)
    i += 1
    if  i % Progress  ==  0:
        print('\r'+'[*] Generating Words:  '+str(i)+'/'+str(TOTAL),
              color='dodger_blue_1', end='')
    if SAVE_MEMORY:  # will save up 30% memory
        if sys.getsizeof(DICT)*10 *1.15 > 1_000_000_000:
            rx.write(FILE,'\n'.join(DICT),'a','\n')
            # print(rx.convert_bytes(sys.getsizeof(DICT)*10))
            # rx.sleep(2)
            del DICT
            DICT = []

print('\r[*] Number of Generated Words:  '+str(TOTAL),
      color='dodger_blue_1')
print(f'[*] Operation finnished in {START.lap(Round=4)} seconds',
      color='dodger_blue_1')
rx.write(FILE, '\n'.join(DICT))
print('[+] Dictionary File Has Been Created Successfully.',
      color='green')
print(f'[*] (Address:  {rx.files.abspath(FILE)})',
      color='dodger_blue_1')

print()
# print(sys.getsizeof(DICT))
# print(rx.convert_bytes(sys.getsizeof(DICT)*10))
pause()
del DICT

pause()

# 4.5 => 3.0
# 3.5 => 2.5
# 3.2 => 2.4
# 1.9 => 1.4
# 1.8 => 1.2
