from pprint import pprint
import Cipher

cipher = Cipher.Affine
key = [7,2]
enc = cipher.encrypt('hello',key,Cipher.LOWERS)
# print(enc)
# print(cipher.decrypt(enc,key,Cipher.LOWERS))


from typing import Literal
def table_creator(alphabet:str|list[str],key:str="",width=5):
    """
    alphabet: str|list[str]
    key: key will be added to the beggining of the table
    width
    """

    # remove duplicates of key
    from collections import OrderedDict
    key = "".join(OrderedDict.fromkeys(key))

    # remove letter of alphabet that are in key
    alphabet = list(alphabet)
    for i,letter in enumerate(alphabet):
        if letter in key:
            alphabet[i] = None
    alphabet = list(filter(None,alphabet))

    # check to see if lengths are equal
    encrypted = list(key)+alphabet
    if len(encrypted) != width**2:
        raise ValueError("Wrong value for alphabet/key/width. \
                (width**2 must be equal to len(alphabet+set(key)) )")

    # creating the table
    table : list[list[str]] = []
    for i in range(width):
        table.append([])
        for j in range(5):
            table[i].append(encrypted[5*i + j])
    # pprint(table)
    return table



def encrypt_adfgx(text,key="",table="DEFAULT",
                  when_not_found:Literal["ERROR","PASS"]="PASS"):
    if table=="DEFAULT":
        alphabets = list(Cipher.LOWERS)
        alphabets.remove("j")
        table = table_creator(alphabets,key,5)
    # pprint((table))

    ADFGX = "ADFGX"
    encrypted = ""
    table_enumerate = list(enumerate(table))
    for letter in text:
        found = False
        for i,row in table_enumerate:
            for j,item in enumerate(row):
                if letter == item:
                    encrypted += ADFGX[i]+ADFGX[j]#+" "
                    found = True
                    break
            if found:
                break
        if (not found)  and  when_not_found=="ERROR":
            raise ValueError(f'letter "{letter}" not found in alphabet+keys')
    return encrypted


def decrypt_adfgx(text,key="",table="DEFAULT"):
    if table=="DEFAULT":
        alphabets = list(Cipher.LOWERS)
        alphabets.remove("j")
        table = table_creator(alphabets,key,5)
    # pprint(table)

    table_labels = "ADFGX"
    decrypted = ""
    for i in range(int(len(text)/2)):
        row = table_labels.index(text[2*i])
        col = table_labels.index(text[2*i +1])
        decrypted += table[row][col]
    
    return decrypted





print(Cipher._ADFGX_Family.encrypt("helloworld", "ramin"))
print(decrypt_adfgx(encrypt_adfgx("helloworld", "ramin"),"ramin"))



"""
[
 ['r', 'a', 'm', 'i', 'n'],
 ['b', 'c', 'd', 'e', 'f'],
 ['g', 'h', 'k', 'l', 'o'],
 ['p', 'q', 's', 't', 'u'],
 ['v', 'w', 'x', 'y', 'z']
]
"""