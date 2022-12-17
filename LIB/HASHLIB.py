from typing import Union,Tuple,Callable,Generator,Iterable
import hashlib
import sys
import os

import rx7 as rx

print = rx.style.print


HASHES_DICT = {
    'md5':hashlib.md5,
    
    'sha1':hashlib.sha1,

    'sha224': hashlib.sha224,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512,

    'sha3_224': hashlib.sha3_224,
    'sha3_256': hashlib.sha3_256,
    'sha3_384': hashlib.sha3_384,
    'sha3_512': hashlib.sha3_512,

    "auto": None
}



def list_lines(filename):
    '''
    return a list that contains every line of file
    '''
    #list_of_words = open(filename).readlines()
    list_of_words= rx.read(filename).splitlines()
    return list_of_words




def decrypt(hash : str,
            type_: str,
            files:Iterable = None,
            generator:Callable = None,
            quiet:bool = False
            ):
    
    if not (files or generator):
        raise ValueError("Either 'files' or 'generator' parameter should be passed to function")
    elif files:
        method = Iterable
    else:
        method = Generator

    print_status = not quiet
    enc_func = HASHES_DICT[type_]
    

    if method == Iterable:
        for File in files:
            i = 0
            lst = list_lines(File)
            ln = len(lst)
            basename = os.path.basename(File)
            for Word in lst:
                if print_status:
                    i += 1
                    if i % 100 == 0:
                        sys.stdout.write(
                            f'\rWorking on words of "{basename}" :  {i}/{ln}'
                        )
                result = enc_func(bytes(Word, 'utf-8')).hexdigest()
                if result == hash:
                    if print_status:
                        sys.stdout.write(
                            f'\rWorking on words of "{basename}" :  {rx.style(i,"green")}/{ln}'
                        )
                        print()
                    return Word
            if print_status:
                sys.stdout.write(
                    f'\rWorking on words of "{basename}" :  {i}/{ln}'
                )
                rx.style.print(f'\n[*] Not Found in "{basename}"\n',
                            'blue')

    elif method == Generator:
        for Word in generator():
            result = enc_func(bytes(Word, 'utf-8')).hexdigest()
            if result == hash:
                return Word


    return None
