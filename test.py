'''
# TODO:
 #> Functions:
    #> Func for y/n inputs
 #> HashGenerator:  More Hashes

# NOTE:
 #> one space at the beginnig of lines?
'''


import random
from LIB import Cipher

alphabet = [char for char in Cipher.ALL_CHARS]
random.shuffle(alphabet)
alphabet = ''.join(alphabet)

encryption = Cipher.Xor
text= 'Ramin.1383'
key = 'R'#alphabet
#print(Cipher.porta('abc','z'))
print(encryption.encrypt(text,key))
print(encryption.decrypt(encryption.encrypt(text,key),key))
