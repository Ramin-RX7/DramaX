import rx7 as rx
from LIB.Functions import wait_for_input, get_files, list_lines
from LIB.Hash import hash_decrypt_file, Recognize_Hash






if __name__ == "__main__":
    TIME= rx.record()
    rx.cls()
    rx.style.print('''
           88  88    db    .dP"Y8 88  88    888888 88 88     888888
           88  88   dPYb   `Ybo." 88  88    88__   88 88     88__  
           888888  dP__Yb  o.`Y8b 888888    88""   88 88  .o 88""  
           88  88 dP""""Yb 8bodP' 88  88    88     88 88ood8 888888     

     8888b.  888888  dP""b8 88""Yb d88   88b 88""Yb 888888 888888 88""Yb
      8I  Yb 88__   dP   `" 88__dP   Y888Y   88__dP   88   88__   88__dP
      8I  dY 88""   Yb      88"Yb     l8l    88"""    88   88""   88"Yb 
     8888Y"  888888  YboodP 88  Yb    d8b    88       88   888888 88  Yb
     ''','gold_3b')
    print('This will run after implementation of "HashDecrypter.py" argument parser')
    exit()
    filename= wait_for_input('Enter Hashed File Name:  ')
    print('Enter word list files path below. Type "end" to finnish adding files')
    hashed_file= get_files(times=1)

    hashes= list_lines(filename)

    for hash in hashes:
        pass
        #HashDecrypter.py argparser
