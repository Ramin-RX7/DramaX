'''
Case Sensetive
Support Numbers and Symbols But Not Work on Them (Under Maintaince)
'''

def rot13(s):
    result = ""
    for v in s:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result


import os
while True:
    os.system('clear')
    print('''

      █▀▀█ █▀▀█ ▀▀█▀▀      ▀█  ▀▀█
      █▄▄▀ █  █   █   ▄▄    █  ▀▀█
      ▀ ▀▀ ▀▀▀▀   ▀        ▀▀▀ ▀▀▀
     ''')

    vminp= input(' Enter Word To Encrypt/Decrypt:  ')
    print()
    if vminp=='99':
        exit()
    if vminp:
        print(f' ROT13 of {vminp} is:  {rot13(vminp)}\n')
    os.system('pause')
