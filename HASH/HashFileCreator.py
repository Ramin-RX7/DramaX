import sys
import argparse

import rx7 as rx

from LIB.Functions import  wait_for_input, list_lines, get_files, pause
from LIB.Hash.Hash_Old import  hash_dict_creator, hash_dict_creator_all, sa


if __name__ == "__main__":
    while True:
        rx.cls()
        rx.style.print('''
        88  88    db    .dP"Y8 88  88    888888 88 88     888888
        88  88   dPYb   `Ybo." 88  88    88__   88 88     88__
        888888  dP__Yb  o.`Y8b 888888    88""   88 88  .o 88""
        88  88 dP""""Yb 8bodP' 88  88    88     88 88ood8 888888

            dP""b8 88""Yb 888888    db   888888 dP"Yb  88""Yb
           dP   `" 88__dP 88__     dPYb    88  dP   Yb 88__dP
           Yb      88"Yb  88""    dP__Yb   88  Yb   dP 88"Yb
            YboodP 88  Yb 888888 dP""""Yb  88   YbodP  88  Yb
        ''', 'gold_3b')


        if len(sys.argv) > 1:
            parser = argparse.ArgumentParser(
                'Dictionary Creator',
                description='Use this app to create dictionaries',
                allow_abbrev=False,
                )

            parser.add_argument('-i','--input-file',
                                required=True,
                                help='The file that contains list of words you want to hash'
                                )
            parser.add_argument('-o','--output-file',
                                metavar='LENGTH', required=True,
                                help='The file to save hashed words to it'
                                )
            parser.add_argument('-t','--type',
                                metavar='HASH_TYPE', required=True,
                                help='Type of Hash to hash the words',
                                choices=list(sa.keys()))
            #parser.add_argument('-I','--Ignore', action='store_true')

            args = parser.parse_args()

            hashed_file_name = args.output_file
            encryption_type = args.type
            words_file_name = args.input_file
            #ignore_memory = args.Ignore

        else:
            words_file_name  = get_files('Words  File Name:  ', times=1)[0]
            hashed_file_name = wait_for_input('Output File Name:  ')
            #encryption_type  = wait_for_input('Encryption Type:   ')
            encryption_type  = rx.io.selective_input('Encryption Type:   ',list(sa.keys()),error=True)

        # get words from file
        words_list = list_lines(words_file_name)
        # create the hash
        if encryption_type != 'all':
            hash_dict_creator(words_list, hashed_file_name,encryption_type)
        else:
            hash_dict_creator_all(words_list, hashed_file_name)

        rx.style.print(f'[+] Hash File{"s" if not encryption_type else ""} are Created Successfully', 'dodger_blue_1')
        pause()
