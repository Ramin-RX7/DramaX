import argparse
import datetime
import hashlib
import os
import sys

import rx7.lite as rx

from LIB.Functions import *
from LIB.Hash import Hash_Decrypt, Recognize_Hash



print= rx.style.print


if __name__ == "__main__":
    rx.cls()
    banner= '''
                        88  88    db    .dP"Y8 88  88
                        88  88   dPYb   `Ybo." 88  88
                        888888  dP__Yb  o.`Y8b 888888
                        88  88 dP""""Yb 8bodP' 88  88

     8888b.  888888  dP""b8 88""Yb d88   88b 88""Yb 888888 888888 88""Yb
      8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   88__   88__dP
      8I  dY 88""   Yb      88"Yb     l8l    88"""    88   88""   88"Yb 
     8888Y"  888888  YboodP 88  Yb    d8b    88       88   888888 88  Yb
     '''
    print(banner,'gold_3b')


    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            'Dictionary Creator',
            description='Use this app to create dictionaries',
            allow_abbrev=False,
            )

        parser.add_argument('-w','--hashed-word',
                            required=True, metavar='HASHED',
                            help='Hashed Word to Decrypt'
                            )
        parser.add_argument('path',metavar='FILES', nargs='+',
                            help='Path to files for searching words')
        parser.add_argument('-q','--quiet',
                            action='store_false'
                            )
        args = parser.parse_args()

        Hash = args.hashed_word
        Type = Recognize_Hash(Hash)
        files = args.path
        quiet = args.quiet


    else:
        Hash= wait_for_input('Enter Hashed String:  ')
        Type= Recognize_Hash(Hash)
        
        if not Type:
            print('[-] Could Not Recognize The Hash Type.', 'red')
            sys.exit()

        print('Enter word list files path below. (Type "end" to finnish adding files)')
        files = get_files()
        quiet = True



    rx.cls()
    print(banner,'gold_3b')
    print()
    print(f'Hash: ', end='') ; print(Hash,'green')
    print(f'Type: ', end='') ; print(Type,'green')
    print()
    print(f'Operation started at:  "{datetime.datetime.now()}"')
    print()

    T= rx.record()

    DECRYPTED= Hash_Decrypt(Hash, files, quiet)
    if DECRYPTED:
        print('[+] Found','green')
        print('Decrypted String is:  ', end='')
        print(DECRYPTED, 'green')
        #print(DECRYPTED[1])
        print(f'[*] Operation Finnished in {round(T.lap(),3)} seconds  ({datetime.datetime.now()})', 'dodger_blue_1')
    else:
        print(f'[-] Could not find any words from given list that matches to "{Hash}"','red')
