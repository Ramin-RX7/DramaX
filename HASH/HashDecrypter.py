import argparse
import hashlib
import sys
import os

import rx7 as rx


sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from LIB.Functions import get_files,pause
from LIB.TAP import Tap
from LIB import HASHLIB




print= rx.style.print



banner= '''
                          88  88    db    .dP"Y8 88  88
                          88  88   dPYb   `Ybo." 88  88
                          888888  dP__Yb  o.`Y8b 888888
                          88  88 dP""""Yb 8bodP' 88  88                   

        8888b. 888888  dP""b8 88""Yb d88   88b 88""Yb 888888 888888 88""Yb
        8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   88__   88__dP
        8I  dY 88""   Yb      88"Yb     l8l    88"""    88   88""   88"Yb 
        8888Y" 888888  YboodP 88  Yb    d8b    88       88   888888 88  Yb
        '''







if len(sys.argv) > 1:
    rx.cls()
    print(banner,color='gold_3b')
    class SimpleArgumentParser(Tap):
        hash: str              # Hashed Text
        type: str = 'auto'     # Hash Type (see all hash types in LIB/HASHLIB.py::HASHES_DICT)
        files: list[str]       # Dictionary Files
        quiet: bool = False    # Quiet Mode
    Args = SimpleArgumentParser(epilog=str(rx.Style('Decrypt hashed text from dictionary files',style='underlined')),
                                conflict_handler='resolve').parse_args()
    Hash,Type,Files,Quiet = (Args.hash,Args.type,Args.files,Args.quiet)
    # rx.cls()
    # print(banner,color='gold_3b')

else:
    rx.cls()
    print(banner,color='gold_3b')
    Hash = rx.io.wait_for_input("Enter Hashed String:  ")
    # print()
    print("Enter Hash Type from list below:")
    options = {}
    i = 1
    for hash in HASHLIB.HASHES_DICT.keys():
        options[str(i)] = hash
        print(f"    {i}) {hash}",end="")
        i += 1
    print()
    Type = rx.io.selective_input("Enter Hash Type: ",options)
    print("Enter your Dictionary files path below.")
    print('  (enter "end" to finish)')
    Files = get_files()
    Quiet = False



print()
print(f'Hash: ', end='') ; print(Hash,color='green')
print(f'Type: ', end='') ; print(Type,color='green')
print()
print(f'[*] Operation started at:  "{rx.DateTime.now()}"', color='dodger_blue_1')
print()

T= rx.record()
DECRYPTED= HASHLIB.decrypt(Hash,Type, files=Files, quiet=Quiet)
if DECRYPTED:
    print('[+] Found',color='green')
    print('Decrypted String is:  ', end='')
    print(DECRYPTED, color='green')
    #print(DECRYPTED[1])
    print(f'\n[*] Operation Finnished Successfully in {round(T.lap(),3)} seconds  ({rx.DateTime.now()})', color='dodger_blue_1')
else:
    print(f'[-] Could not find any words from given list that matches to "{Hash}"',color='red')
print()
pause()
