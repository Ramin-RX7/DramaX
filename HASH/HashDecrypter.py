import sys
import os
from typing import Literal

import rx7 as rx
from tabulate import tabulate

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
import LIB.Hash as HASHLIB
from LIB.Functions import (get_files,print_banner,cursorPos,tabulate_table)
from LIB.TAP import Tap
from LIB import Dictionary


print= rx.style.print



FIXED_LINES = 0
TABLE = tabulate_table(headers=["OPTION","VALUE"], tablefmt="rounded_grid")

def clear_lines(n=None):
    if not n:
        n = cursorPos()[1] - FIXED_LINES
    output = '\x1B[1A\x1b[2K'*n
    print(end=output)

def update_table(key=None,value=None):
    global TABLE
    if any([key,value]):
        TABLE.add_row([key,value])
    clear_lines()
    print(TABLE)
    print()


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
FIXED_LINES +=  len(banner.splitlines()) + 1


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
    update_table("Hash",Hash)
    print("Choose decrypting method:")
    print("""\
          1. Words list files
          2. Hash  list files
          3. Live Dictionary Creator
    """)
    method = rx.io.selective_input("Decrypting Mathod: ", ["1","2","3"])
    if method in ("1","2"):
        print("Enter your Dictionary files path below.")
        print('  (Press enter with empty input to end)')
        Files = get_files(empty_input_action='end')
        update_table("Dictionaries", Files)
        Threads = int(rx.io.selective_input("Enter Number of threads: ",
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
            return Dictionary.dict_creator_generator(SS,LENGTH)
        Threads = 1
    update_table("Threads",Threads)

    #"""
    if method == "2":
        Type = "None"
    else:
        print("\nEnter Hash Type from list below:")
        opts = {}
        for i,hash in enumerate(list(HASHLIB.HASHES_DICT.keys()),1):
            opts[str(i)] = hash
            print(f"    {i}. {hash}",end="")
        print()
        Type = rx.io.selective_input("Enter Hash Type: ",opts)
    update_table("Hash Type",Type)
    Quiet = False



# rx.io.getpass("Press Enter to Start the operation")
update_table()
rx.style.log_info(f'[*] Operation started at:  "{rx.DateTime.now()}"', add_time=False)

T = rx.record()
if method in ("1","2"):
    if Threads == 1:
        DECRYPTED =  HASHLIB.decrypt(Hash, Type, files=Files, quiet=Quiet)
    else:
        DECRYPTED =  HASHLIB.decrypt_thread(Hash, Type, files=Files, quiet=Quiet, threads_count=Threads)
elif method in ("3"):
    TOTAL = 0
    for i in range(1, LENGTH+1):
        TOTAL += len(SS)**i
    DECRYPTED =  HASHLIB.decrypt(Hash, Type, generator=dictionary_generator, quiet=Quiet, length=TOTAL)

duration = round(T.lap(),3)
min, sec  = divmod(duration, 60)
hour, min = divmod(min, 60)
day, hour = divmod(hour, 24)
formatted_duration = f"{sec} seconds"
if min:
    formatted_duration = f"{min} minutes and "+formatted_duration
if hour:
    formatted_duration = f"{hour} hours and "+formatted_duration
if day:
    formatted_duration = f"{day} days and "+formatted_duration


if DECRYPTED:
    rx.style.log_success('[+] Found', add_time=False)
    print('[+] Decrypted String is:  ', end='')
    print(DECRYPTED, color='green')
    rx.style.log_info(
        f'[*] Operation Finnished Successfully in {formatted_duration}  ({rx.DateTime.now()})',
        add_time=False
    )
else:
    rx.style.log_info(
        f'[*] Operation Finnished in "{formatted_duration}"  ({rx.DateTime.now()})',
        add_time=False
    )
    rx.style.log_error(
        f'[-] Could not find any words from given list that matches to "{Hash}"',
        add_time=False
    )
print()
# pause()
