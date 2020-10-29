import hashlib
import sys
import getpass
import argparse
from LIB.Functions import pause, cls
from LIB.Hash import sa
import rx7 as rx



sa={'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha224':hashlib.sha224,'sha256':hashlib.sha256,
    'sha384':hashlib.sha384,'sha512':hashlib.sha512,'sha3_224':hashlib.sha3_224,
    'sha3_256':hashlib.sha3_256, 'sha3_384':hashlib.sha3_384,'sha3_512':hashlib.sha3_512,
    'all':'all'}


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




if __name__ == "__main__":
    cls()
    rx.style.print('''
                     88  88    db    .dP"Y8 88  88
                     88  88   dPYb   `Ybo." 88  88
                     888888  dP__Yb  o.`Y8b 888888
                     88  88 dP""""Yb 8bodP' 88  88

     dP""b8 888888 88b 88 888888 88""Yb    db   888888 dP"Yb  88""Yb
    dP   `" 88__   88Yb88 88__   88__dP   dPYb    88  dP   Yb 88__dP
    Yb  "88 88""   88 Y88 88""   88"Yb   dP__Yb   88  Yb   dP 88"Yb 
     YboodP 888888 88  Y8 888888 88  Yb dP""""Yb  88   YbodP  88  Yb
    ''', 'gold_3b')

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

        print_hashes(word, hashed_file_name, quiet)


    else:
        while True:
            print('Use:  "HASH||FILE"  to save output to FILE')
            inp= input('Enter String to Create Hashes:  ')
            if inp=='exit':
                break
            elif inp:
                if '||' in inp:
                    inp = inp.split('||')
                    print_hashes(inp[0],inp[1])
                else:
                    print_hashes(inp)
                pause()
