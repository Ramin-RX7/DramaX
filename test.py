#import LIB.Hash as hashlib
#enc_func = hashlib.HASHES_DICT["sha256"]
import hashlib
enc_func = hashlib.sha256

import Ciphers.Rail_Fence as rf
# enc_func = rf.encryptRailFence

import time
t=time.time()

for i in range(100,1_000_000):
    enc_func(bytes(str(i), 'utf-8')).hexdigest()
    # x = enc_func(str(i),3)
    # print(x)
    i += 1
    # break

t2 = time.time()
print(t2-t)


