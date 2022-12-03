from typing import Union,Tuple,Callable,Generator,Iterable
import hashlib
import sys
import os

import rx7 as rx

print = rx.style.print


sa={'md5':hashlib.md5,
    
    'sha1':hashlib.sha1,

    'sha224': hashlib.sha224,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512,

    'sha3_224': hashlib.sha3_224,
    'sha3_256': hashlib.sha3_256,
    'sha3_384': hashlib.sha3_384,
    'sha3_512': hashlib.sha3_512,

    'GUESS': None}


def list_lines(filename):
    '''
    return a list that contains every line of file
    '''
    #list_of_words = open(filename).readlines()
    list_of_words= rx.read(filename).splitlines()
    return list_of_words


def decrypt(hash : str,
            type_: str,
            Files_or_Generator: Union[Iterable, Callable],
            quiet:bool = False
            ):
    
    print_status = not quiet
    enc_func = sa[type_]

    method = Iterable
    if callable(Files_or_Generator):
        method = Generator
    

    if method == Iterable:
        for File in Files_or_Generator:
            i = 0
            lst = list_lines(File)
            ln = len(lst)
            for Word in lst:
                if print_status:
                    i += 1
                    if i % 100 == 0:
                        sys.stdout.write(
                            f'\rWorking on words of "{os.path.basename(File)}" :  {i}/{ln}'
                        )
                result = enc_func(bytes(Word, 'utf-8')).hexdigest()
                if result == hash:
                    if print_status:
                        sys.stdout.write(
                            f'\rWorking on words of "{os.path.basename(File)}" :  {i}/{ln}'
                        )
                        print()
                    return Word
            if print_status:
                sys.stdout.write(
                    f'\rWorking on words of "{os.path.basename(File)}" :  {i}/{ln}'
                )
                rx.style.print(f'\n[*] Not Found in "{os.path.basename(File)}"\n',
                            'blue')

    elif method == Generator:
        for Word in Files_or_Generator():
            result = enc_func(bytes(Word, 'utf-8')).hexdigest()
            if result == hash:
                return Word


    return None
