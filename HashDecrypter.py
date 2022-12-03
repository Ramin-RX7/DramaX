import argparse
import hashlib
import sys

import rx7 as rx

from LIB.Functions import get_files,pause


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




def parse_args():
    pass




from LIB import HASHLIB

if __name__ == "__main__":
    print("No ArgeParse Parser Created","red")
    exit()
    Hash,Type,Files,Quiet = parse_args()
else:
    Hash = rx.io.wait_for_input("Enter Hashed String:  ")
    print()

    print("Enter Hash Type from list below")
    options = {}
    i = 1
    for hash in HASHLIB.sa.keys():
        options[str(i)] = hash
        print(f"    {i}) {hash}")
        i += 1        
    Type = rx.io.selective_input("Enter Hash Type: ",options)
    
    print("Enter your Dictionary files path below.")
    print('  (enter "end" to finish)\n')
    Files = get_files()
    Quiet = False



rx.cls()
print(banner,'gold_3b')
print()
print(f'Hash: ', end='') ; print(Hash,'green')
print(f'Type: ', end='') ; print(Type,'green')
print()
print(f'[*] Operation started at:  "{rx.DateTime.now()}"', 'dodger_blue_1')
print()

T= rx.record()
DECRYPTED= HASHLIB.decrypt(Hash,Type, Files, Quiet)
if DECRYPTED:
    print('[+] Found','green')
    print('Decrypted String is:  ', end='')
    print(DECRYPTED, 'green')
    #print(DECRYPTED[1])
    print(f'[*] Operation Finnished Successfully in {round(T.lap(),3)} seconds  ({rx.DateTime.now()})', 'dodger_blue_1')
else:
    print(f'[-] Could not find any words from given list that matches to "{Hash}"','red')
print()
pause()