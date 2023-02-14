from typing import Literal
from collections import OrderedDict
import hashlib


def decrypt(nom:int) -> int:
    for i in range(nom):
        a = hashlib.sha256(bytes(str(nom),"utf-8")).hexdigest()
    a = 0 
    return a
