# import pyximport
# pyximport.install()


import time

t = time.time()
import mycython
# from x import mycython
t2 = time.time()
print(t2-t)
t = time.time()
a=mycython.decrypt(1000000)
print(a)
for i in range(500000):
    break
    a = mycython.ADFGX.encrypt("ramin","hello")
t2 = time.time()
print(t2-t)
