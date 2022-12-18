import sys
import os

import rx7 as rx

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from LIB.Functions import  get_files, list_lines






if __name__ == "__main__":
    print("THIS FILE IS NOT CONSIDERED AS ANY PART OF THIS PROJECT IN THE REMAKE")
    print("IT WILL BE REMOVED FROM THE REPOSITORY IN THE UPCOMING UPDATES")
    exit()
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
    
    filename= get_files('Enter Hashed File Name:  ',times=1)
    print('Enter word list files path below. Type "end" to finnish adding files')
    dict_files= get_files()
    
    for hash in list_lines(filename):
        pass    
        #HashDecrypter.py argparser
