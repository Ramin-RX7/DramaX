import sys
import os
import hashlib
from typing import Union, Tuple, Callable, Generator, Iterable

import rx7 as rx

from .Functions import list_lines

# import xxhash
from .NEW_HASHES import pymmh3   # Because of some errors in installing pymmh3
from .NEW_HASHES import siphash  # and siphash from pip, I copy them in ./encryptions/


HashType = str
Function = Callable
dichash = {'1':'md5','2':'sha1','3':'sha224','4':'sha256','5':'sha384','6':'sha512'}

sa={'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha224':hashlib.sha224,'sha256':hashlib.sha256,
    'sha384':hashlib.sha384,'sha512':hashlib.sha512,'sha3_224':hashlib.sha3_224,
    'sha3_256':hashlib.sha3_256, 'sha3_384':hashlib.sha3_384,'sha3_512':hashlib.sha3_512,
    'all':'all'}

def hash_dict_creator(input_list: Iterable, output_file_name: str,
                      encryption_type: str) -> None:
    '''
    Create Hash file of a specifiec Hash Type
    '''
    hashesToExport = []
    encryption_type = sa[encryption_type]
    for word in input_list:
        crypt = encryption_type()
        crypt.update(bytes(word, encoding='utf-8'))
        hashOfWord = crypt.hexdigest()
        hashesToExport.append(hashOfWord)

    # Creating the output file
    rx.write(output_file_name, '\n'.join(hashesToExport))

def hash_dict_creator_all(input_list: Iterable, output_file_name: str) -> None:
    '''
    Create All Types of Hashes
    '''

    try:
        output_file_name = output_file_name.split('.')[0]
        ext = output_file_name.split('.')[1]
    except IndexError:
        ext = 'txt'

    for word in input_list:
        word = bytes(word, encoding='utf-8')
        # To save memory I did not save the hashes in seprate lists.
        # Instead, I directly add them to their files
        # But you can add them to specifiec list ( like hash_file_creator() )
        # and then write them to files
        rx.write(output_file_name + '_md5.'+ext,
                 str(hashlib.md5(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha1.'+ext,
                 str(hashlib.sha1(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha224.'+ext,
                 str(hashlib.sha224(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha256.'+ext,
                 str(hashlib.sha256(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha384.'+ext,
                 str(hashlib.sha384(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha512.'+ext,
                 str(hashlib.sha512(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha3-224.'+ext,
                 str(hashlib.sha3_224(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha3-256.'+ext,
                 str(hashlib.sha3_256(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha3-384.'+ext,
                 str(hashlib.sha3_384(word).hexdigest()) + '\n', 'continue')
        rx.write(output_file_name + '_sha3-512.'+ext,
                 str(hashlib.sha3_512(word).hexdigest()) + '\n', 'continue')

def Recognize_Hash(HASH:str) -> Union[HashType, None]:
    lngth= len(HASH)
    if lngth in (40, 56, 64, 96, 128, 32):
        if lngth == 32:
            Type = '1'
        if lngth == 40:
            Type = '2'
        if lngth == 56:
            Type = '3'
        if lngth == 64:
            Type = '4'
        if lngth == 96:
            Type = '5'
        if lngth == 128:
            Type = '6'
        return str(dichash[Type])
    else:
        return None

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

nothing = hashlib.md5(b'')
do_nothing = lambda x: nothing

def get_hash_func(Type: str) -> Tuple[Function, Function]:
    '''
    Return hashlib function of specifiec Types
    e.g: 
    >>> get_hash_func('sha224')
    (hashlib.sha224, hashlib.sha3_224)
    '''
    # the reason I Did This is if the hash is sha type, we need 2
    # encryption types (sha2 & sha3) but md5 need one (only md5)
    # so I use 'do_nothing' for second md5 function to decrease
    # number of codes and don't repeat the same code for md5 and sha
    if Type == 'md5':
        enc = hashlib.md5
        enc2 = do_nothing  
    elif Type == 'sha1':
        enc = hashlib.sha1
        enc2 = do_nothing  
    elif Type == 'sha224':
        enc = hashlib.sha224
        enc2 = hashlib.sha3_224
    elif Type == 'sha256':
        enc = hashlib.sha256
        enc2 = hashlib.sha3_256
    elif Type == 'sha384':
        enc = hashlib.sha384
        enc2 = hashlib.sha3_384
    elif Type == 'sha512':
        enc = hashlib.sha512
        enc2 = hashlib.sha3_512
    else:
        raise ValidationError('Invalid Hash Type')
    return enc, enc2



class Encrypt:
    #convert = True
    
    #< SCRYPT & SIPHASH & md5 >#
    @staticmethod
    def scrypt(password, salt, n, r, p, maxmem=0, dklen=64):
        return hashlib.scrypt(
            bytes(password),
            salt=bytes(salt),
            n=n, r=r, p=p,
            maxmem=maxmem,
            dklen=dklen).hex()
    @staticmethod
    def sipHash_2_4(password):
        return siphash.SipHash_2_4(bytes(password)).hexdigest()
    @staticmethod
    def md5(password):
        return hashlib.md5(password).hexdigest()

    #< BLAKE >#
    @staticmethod
    def blake2b(password, **kwargs):
        '''
        password: bytes,
        digest_size: int,
        key: ,
        salt: bytes,
        person: ,
        fanout: int,
        depth: int,
        leaf_size: int,
        node_offset: int,
        node_depth: int,
        inner_size: int,
        last_node: bool
        '''
        return hashlib.blake2b(password, **kwargs,).hexdigest()
    @staticmethod
    def blake2s(password, **kwargs):
        '''
        password: bytes,
        digest_size: int,
        key: ,
        salt: bytes,
        person: ,
        fanout: int,
        depth: int,
        leaf_size: int,
        node_offset: int,
        node_depth: int,
        inner_size: int,
        last_node: bool
        '''
        return hashlib.blake2s(password, **kwargs,).hexdigest()

    #< XHH3 >#
    @staticmethod
    def xxh3_128(password):
        return xxhash.xxh3_128(password).hexdigest()
    @staticmethod
    def xxh3_64(password):
        return xxhash.xxh3_64(password).hexdigest()
    @staticmethod
    def xxh2_32(password):
        return xxhash.xxh32(password).hexdigest()
    @staticmethod
    def xxh2_64(password):
        return xxhash.xxh64(password).hexdigest()

    #< mmh3 >#
    @staticmethod
    def pymmh3_32(password):
        return pymmh3.hash(password)
    @staticmethod
    def pymmh3_64(password):
        return pymmh3.hash64(password)
    @staticmethod
    def pymmh3_128(password):
        return pymmh3.hash128(password)

    #< Sha2 >#


    #< Sha3 >#











def Hash_Decrypt(Hash: str,
                 Files_or_Generator: Union[Iterable, Callable],
                 print_status=True) -> Union[Tuple[str, str], None]:
    '''
    - Hash: Hashed String\n
    - Files_or_Generator: A Function that returns list of words.  
    (Better a generator instead of Normal Function for Faster Performance)
    - print_status: if true it will print searching status
    '''

    if type(Files_or_Generator) not in (
            list, set, tuple) and not callable(Files_or_Generator):
        raise TypeError(
            'Files_or_Generator Must Be a Function(Generator) or List of Files'
        )
    else:  # Removable line
        if type(Files_or_Generator) in (list, set, tuple):
            FoG = 'Iterable'
        else:
            FoG = 'Function'

    Type = Recognize_Hash(Hash)
    if not Type:
        raise ValidationError('Couldnt Recognize the Hash Type')

    enc1, enc2 = get_hash_func(Type)

    if FoG == 'Iterable':
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
                result1 = enc1(bytes(Word, 'utf-8')).hexdigest()
                result2 = enc2(bytes(Word, 'utf-8')).hexdigest()
                if result1 == Hash or result2 == Hash:
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
    else:
        for Word in Files_or_Generator():
            result1 = enc1(bytes(Word, 'utf-8')).hexdigest()
            result2 = enc2(bytes(Word, 'utf-8')).hexdigest()
            if result1 == Hash or result2 == Hash:
                '''if result1 == Hash:
                    typee= enc1
                elif result2 in Hash:                   
                    typee= enc2
                return (Word, typee.__name__)'''
                return Word

    return None

def hash_decrypt_file(file_of_hashes, Files_or_Generator) -> Generator:
    '''
    UNDER MAINTAINCE
    '''
    '''
    returns a dictionary that contains hash:word (if found)\n
    PARAMETERS:\n
    file: path to the file that contains hashes
          NOTE: ALL HASHES MUST HAVE SAME LENGTH\n
    Files_or_Generator: Function rr Files that returns/contain words list.
      Files_or_Generator can be:
        - An Iterable that contains files path.
        - A Function that returns list of words.  
          (Better a generator instead of Normal Function for Faster Performance)

    '''
    if type(Files_or_Generator) not in (list,set,tuple) and not callable(Files_or_Generator):
        raise TypeError('Files_or_Generator Must Be a Function(Generator) or List of Files')
    else:  # removable line
        if type(Files_or_Generator) in (list,set,tuple):
            FoG_Type= 'Iterable'
        else:
            FoG_Type= 'Function'

    hashes= list_lines(file_of_hashes)
    Type= Recognize_Hash(hashes[1])
    enc1, enc2= get_hash_func(Type)

    FOUND= {}

    if FoG_Type == 'Iterable':
        for File in Files_or_Generator:
            for Word in list_lines(File):
                Word= bytes(Word[:-1],'utf-8')
                result1 = enc1(Word).hexdigest()
                result2 = enc2(Word).hexdigest()
                if result1 in hashes:
                    FOUND[result1]=Word
                    yield (result1, Word)
                elif result2 in hashes:
                    FOUND[result2]=Word
                    yield (result2, Word)

    else:
        for Word in Files_or_Generator():
            Word= bytes(Word[:-1],'utf-8')
            result1 = enc1(Word).hexdigest()
            result2 = enc2(Word).hexdigest()
            if result1 in hashes:
                FOUND[result1]=Word
                yield (result1, Word)
            elif result2 in hashes:
                FOUND[result2]=Word
                yield (result2, Word)
    
    if not len(FOUND):
        rx.style.print('We Could Not Find Any Words From Files','red')
        yield None
