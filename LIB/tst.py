from pprint import pprint
import Cipher

cipher = Cipher.ADFGVX
key = "ramin"
enc = cipher.encrypt('hello',key,)
print(enc)
print(cipher.decrypt(enc,key))
exit()

import time
t = time.time()
for i in range(500000):
    a = Cipher.ADFGX.encrypt("ramin","hello")
t2 = time.time()
print(t2-t)
# print(a)







"""
[
 ['r', 'a', 'm', 'i', 'n'],
 ['b', 'c', 'd', 'e', 'f'],
 ['g', 'h', 'k', 'l', 'o'],
 ['p', 'q', 's', 't', 'u'],
 ['v', 'w', 'x', 'y', 'z']
]
"""