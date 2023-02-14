from pprint import pprint
import Ciphers

cipher = Ciphers.ADFGVX
key = "ramin"
# enc = cipher.encrypt('hello',key,)
# print(enc)
# print(cipher.decrypt(enc,key))
# exit()

"""
import time
t = time.time()
for i in range(500000):
    a = Cipher.ADFGX.encrypt("ramin","hello")
t2 = time.time()
print(t2-t)
# print(a)
"""



def encrypt(text, key, alphabet=Ciphers.LOWERS):
    """
    """
    new_alphabet = key
    for character in alphabet:
        if character not in key:
            new_alphabet += character
    encrypted = ""
    for character in text:
        try:
            encrypted += new_alphabet[alphabet.index(character)]
        except ValueError:
            encrypted += character
    return encrypted


def decrypt(text,key,alphabet=Ciphers.LOWERS):
    new_alphabet = key
    for character in alphabet:
        if character not in key:
            new_alphabet += character
    decrypted = ""
    for character in text:
        try:
            decrypted += alphabet[new_alphabet.index(character)]
        except ValueError:
            decrypted += character
    return decrypted


print(decrypt(encrypt("this is","keyword"),'keyword'))















