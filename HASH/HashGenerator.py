import hashlib
import sys
import getpass
import argparse
import os

import rx7 as rx

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from LIB.Functions import pause,print_banner
from LIB.HASHLIB import HASHES_DICT
from LIB.TAP import Tap



print = rx.style.print


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




def print_hashes(word,file=None, Print=True):
    word = bytes(word, encoding='utf-8')
    LIST = []
    for name,func in HASHES_DICT.items():
        try:
            result = func(word).hexdigest()
            LIST.append(result)
            if Print:
                print(f' {name.upper()}:{" "*(10-len(name))}{result}')
        except TypeError:
            pass
    if file:
        rx.write(str(file),'\n'.join(LIST))
    return LIST




if len(sys.argv) > 1:
    class SimpleArgumentParser(Tap):
        text : str                 # string which you want to get its hashes
        output_file:str = None     # The file to save hashes of "word" to it
        quiet: bool     = False    # Run app in quiet mode (Do not print the hashes)
        def configure(self) -> None:
            self.add_argument('text')
    Args = SimpleArgumentParser(epilog=str(rx.Style(
                                            'Generate Hash of a word in all supported hash types',
                                            style='underlined')),
                                conflict_handler='resolve').parse_args()
    Text,File,Quiet = (Args.text,Args.output_file,Args.quiet)

    if not Quiet:
        rx.cls()
        print_banner(BANNER)
        print(f'''\nHere is list of hashes for "{rx._fg('dodger_blue_1')}{Text}{rx._attr(0)}:"''')
        print_hashes(Text,File, not Quiet)


else:
    rx.cls()
    print_banner(BANNER)
    inp= input('Enter String to Create Hashes:  ')
    if inp=='exit':
        exit()
    elif inp:
        print_hashes(inp)
