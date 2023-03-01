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

    "auto":  "auto",
    "None":  None
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
            quiet:bool = False,
            **kwargs):

    if not (files or generator):
        raise ValueError("Either 'files' or 'generator' parameter should be passed to function")
    elif files:
        method = Iterable
    else:
        method = Generator

    print_status = not quiet

    if type_ not in HASHES_DICT.keys():
        raise ValueError("Could not find given hash type in the list.")
    enc_func = HASHES_DICT[type_]
    if enc_func == "auto":
        print("Auto hash detection is not implemented yet",color="red")
        print('You can use "DramaX::Hash::Detect Hash Type" to see possible result')
        return None



    if method == Generator:
        files = [Generator]

    for File in files:
        i = 0
        if method == Iterable:
            dict_ = list_lines(File)
            def f():
                return dict_
            length = len(dict_)
            basename = os.path.basename(File)
        elif method == Generator:
            f = generator
            length = kwargs["length"]
            basename = "given dictionary"
        for Word in f():
            if print_status:
                i += 1
                if i % 100 == 0:
                    sys.stdout.write(
                        f'\rWorking on words of "{basename}" :  {i}/{length}'
                    )
            if enc_func:
                result = enc_func(bytes(Word, 'utf-8')).hexdigest()
            else:
                result = Word
            if result == hash:
                break
        else:
            Word = None

        if print_status:
            sys.stdout.write(
                f'\rWorking on words of "{basename}" :  {i}/{length}'
            )
            print()
        return Word
    return None



import more_itertools, threading
def decrypt_thread(hash : str,
            type_: str,
            files:Iterable = None,
            generator:Callable = None,
            quiet:bool = False,
            threads_count:int = 5
            ):

    if not (files or generator):
        raise ValueError("Either 'files' or 'generator' parameter should be passed to function")
    elif files:
        method = Iterable
    else:
        method = Generator

    print_status = not quiet

    if type_ not in HASHES_DICT.keys():
        raise ValueError("Could not find given hash type in the list.")
    enc_func = HASHES_DICT[type_]
    if enc_func == "auto":
        print("Auto hash detection is not implemented yet",color="red")
        print('You can use "DramaX::Hash::Detect Hash Type" to see possible result')
        return None


    def thread_dec(words_list):
        for Word in words_list:
            if enc_func:
                result = enc_func(bytes(Word, 'utf-8')).hexdigest()
            else:
                result = Word
            if result == hash:
                return Word

    class ThreadWithReturnValue(threading.Thread):
        def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
            threading.Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None
        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        def join(self, *args):
            threading.Thread.join(self, *args)
            return self._return


    if method == Iterable:
        for File in files:
            i = 0
            distributeds = more_itertools.distribute(threads_count,list_lines(File))

            THREADS = []
            for word_list in distributeds:
                thread = ThreadWithReturnValue(target=thread_dec,args=(word_list,))
                thread.daemon = True
                thread.start()
                THREADS.append(thread)
                threading.Lock

            while True:
                not_alives = []
                for thread in THREADS:
                    is_alive = thread.is_alive()
                    if not is_alive:
                        not_alives.append((not is_alive))
                        if thread._return:
                            return thread._return
                if all(not_alives) and len(not_alives)==threads_count:
                    return

    elif method == Generator:
        for Word in generator():
            result = enc_func(bytes(Word, 'utf-8')).hexdigest()
            if result == hash:
                return Word


    return None
