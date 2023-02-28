import sys
import os

import rx7 as rx
from typing import Literal

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from LIB.Functions import get_files,print_banner
from LIB.TAP import Tap
import LIB.Hash as HASHLIB
from LIB import Dictionary


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

rx.cls()
print_banner(banner)



if len(sys.argv) > 1:
    class SimpleArgumentParser(Tap):
        hash: str              # Hashed Text
        type: str = 'auto'     # Hash Type (see all hash types in LIB/HASHLIB.py::HASHES_DICT)
        files: list[str]       # Dictionary Files
        quiet: bool = False    # Quiet Mode
        threads:int = 4        # Number of threads to use
        method: Literal["wordlist","hashlist"] # Defines whether given files are already hashed or not
    Args = SimpleArgumentParser(
                epilog=str(rx.Style('Decrypt hashed text from dictionary files',
                                    style='underlined')),
                conflict_handler='resolve').parse_args()
    Hash,Type,Files,Quiet = (Args.hash,Args.type,Args.files,Args.quiet)
    # rx.cls()
    # print(banner,color='gold_3b')
else:
    r"""
    Hash = "4fd1ba2a277b611f1edef10ed6ffac3c"
    Type = "md5"
    Files = [r"C:\Users\rawmi\Desktop\openwall.net-all.txt"]
    Threads = 1
    # """
    Hash = rx.io.wait_for_input("Enter Hashed String:  ")
    print()
    print("Choose decrypting method:")
    print("""
          1. Words list files
          2. Hash  list files
          3. Live Dictionary Creator
    """)
    method = rx.io.selective_input("Decrypting Mathod: ", ["1","2","3"])
    if method in ("1","2"):
        print("Enter your Dictionary files path below.")
        print('  (enter "end" to finish)')
        Files = get_files(empty_input_action='end')
        Threads = int(rx.io.selective_input("Enter Nunber of threads: ",
                                            [str(i) for i in range(8)]))
    elif method in ("3"):
        SS = rx.io.wait_for_input('Enter Characters of Dictionary:  ')
        while True:
            LENGTH = rx.io.wait_for_input('Enter Max Length of Dictionary:  ')
            try:
                LENGTH = int(LENGTH)
                assert LENGTH > 0
                break
            except:
                print('Length Should be an integer and higher than 0')
        def dictionary_generator():
            yield Dictionary.dict_creator_generator(SS,LENGTH)
        Threads = 1
    #"""
    if method == "2":
        Type = "None"
    else:
        print("Enter Hash Type from list below:")
        options = {}
        for i,hash in enumerate(list(HASHLIB.HASHES_DICT.keys()),1):
            options[str(i)] = hash
            print(f"    {i}) {hash}",end="")
        print()
        Type = rx.io.selective_input("Enter Hash Type: ",options)
    Quiet = False




rx.cls()
print_banner(banner)
# print(banner,color='gold_3b')
print()
print(f'Hash: ', end='') ; print(Hash,color='green')
print(f'Type: ', end='') ; print(Type,color='green')
print()
print(f'[*] Operation started at:  "{rx.DateTime.now()}"', color='dodger_blue_1')
print()

T= rx.record()
if method in ("1","2"):
    if Threads == 1:
        DECRYPTED= HASHLIB.decrypt(Hash, Type, files=Files, quiet=Quiet)
    else:
        DECRYPTED= HASHLIB.decrypt_thread(Hash, Type, files=Files, quiet=Quiet, threads_count=Threads)
elif method in ("3"):
    TOTAL = 0
    for i in range(1, LENGTH+1):
        TOTAL += len(SS)**i
    DECRYPTED= HASHLIB.decrypt(Hash, Type, generator=dictionary_generator, quiet=Quiet, length=TOTAL)


if DECRYPTED:
    print('[+] Found',color='green')
    print('Decrypted String is:  ', end='')
    print(DECRYPTED, color='green')
    #print(DECRYPTED[1])
    print(f'\n[*] Operation Finnished Successfully in {round(T.lap(),3)} seconds  ({rx.DateTime.now()})', color='dodger_blue_1')
else:
    print(f'\n[-] Could not find any words from given list that matches to "{Hash}"',color='red')
print()
# pause()
