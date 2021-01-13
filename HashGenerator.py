import hashlib
import sys
import getpass
import argparse

import rx7 as rx

from LIB.Functions import pause, cls
from LIB.Hash import sa


def print_hashes(word, file=None, Print=True):
    word=bytes(word, encoding='utf-8')

    LIST = []
    for name,func in sa.items():
        try:
            result = func(word).hexdigest()
            LIST.append(result)
            if Print:
                print(f' {name.upper()}:{" "*(10-len(name))}{result}')
        except TypeError:
            pass

    if file:
        rx.write(str(file),'\n'.join(result))


BANNER = '''
                     88  88    db    .dP"Y8 88  88
                     88  88   dPYb   `Ybo." 88  88
                     888888  dP__Yb  o.`Y8b 888888
                     88  88 dP""""Yb 8bodP' 88  88                  

     dP""b8 888888 88b 88 888888 88""Yb    db   888888 dP"Yb  88""Yb
    dP   `" 88__   88Yb88 88__   88__dP   dPYb    88  dP   Yb 88__dP
    Yb  "88 88""   88 Y88 88""   88"Yb   dP__Yb   88  Yb   dP 88"Yb 
     YboodP 888888 88  Y8 888888 88  Yb dP""""Yb  88   YbodP  88  Yb
    '''


if __name__ == "__main__":

    if len(sys.argv) > 1:

        parser = argparse.ArgumentParser(
            'Hash Generator',
            description='Generate Hash of a word in all hash types',
            allow_abbrev=False,
            )

        parser.add_argument('HASH',
                            help="Word which you want to get its hashes"
                            )
        parser.add_argument('-f','--output-file',
                            metavar='FILE',
                            help='The file to save hashes of HASH to it'
                            )
        parser.add_argument('-q','--quiet', action='store_false',
                            help='Run app in quiet mode (Do not print the hashes)'
                            )

        args = parser.parse_args()
        
        hashed_file_name = args.output_file
        word = args.HASH
        quiet = args.quiet


        cls()
        rx.style.print(BANNER, 'gold_3b')

        print(f'''Here is list of hashes for "{rx.fg('dodger_blue_1')}{word}{rx.attr(0)}:"''')

        print_hashes(word, hashed_file_name, quiet)


    else:
        while True:
            cls()
            rx.style.print(BANNER, 'gold_3b')
            print('Use:  "HASH||FILE"  to save output to FILE \n')
            inp= input('Enter String to Create Hashes:  ')
            if inp=='exit':
                break
            elif inp:
                if '||' in inp:
                    inp = inp.split('||')
                    print(f'''Here is list of hashes for "{rx.fg('dodger_blue_1')}{inp[0]}{rx.attr(0)}":''')
                    print_hashes(inp[0],inp[1])
                else:
                    print(f'''Here is list of hashes for "{rx.fg('dodger_blue_1')}{inp}{rx.attr(0)}":''')
                    print_hashes(inp)
                pause()
