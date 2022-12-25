from typing import Literal
from collections import OrderedDict

print("Python One")
LOWERS   = 'abcdefghijklmnopqrstuvwxyz'
class ADFGX:
    '''
    Uses a table with "ADFGX" labels for rows and columns.
    Key is a string (usually with characters in given alphabet) (with no repeat in characters)
      that would be placed in the beginning of the table
    if "table" argument is not "DEFAULT", it should have the structure below:
        list[list[str]]
        if width of table is 5 as an example:
            (the table should be 5x5)
        [
         ['i', 'n', 'r', 'a', 'm'],
         ['b', 'c', 'd', 'e', 'f'],
         ['g', 'h', 'k', 'l', 'o'],
         ['p', 'q', 's', 't', 'u'],
         ['v', 'w', 'x', 'y', 'z']
        ]
        when the table is not default, encrypt/decrypt method would assume you 
          have injected the key.
    For easier use, I have implemented table_creator funtion in "ADFGX.Tools" class so
      you can make tables with custom key and width
    '''
    class Tools:
        @staticmethod
        def table_creator(alphabet,key:str="",width=5):
            """
            alphabet: str|list[str]
            key: key will be added to the beggining of the table
            width
            """

            # remove duplicates of key
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

            return table

    @staticmethod
    def decrypt(text,key="",table="DEFAULT"):
        if table=="DEFAULT":
            alphabets = list(LOWERS)
            alphabets.remove("j")
            table = ADFGX.Tools.table_creator(alphabets,key,5)
        # pprint(table) 

        table_labels = "ADFGX"
        decrypted = ""
        for i in range(int(len(text)/2)):
            row = table_labels.index(text[2*i])
            col = table_labels.index(text[2*i +1])
            decrypted += table[row][col]

        return decrypted
    @staticmethod
    def encrypt(text,key:str="",table="DEFAULT",
                      when_not_found:Literal["ERROR","PASS"]="PASS"):
        if table=="DEFAULT":
            alphabets = list(LOWERS)
            alphabets.remove("j")
            table = ADFGX.Tools.table_creator(alphabets,key,5)
        # pprint((table))

        table_label = "ADFGX"
        encrypted = ""
        table_enumerate = list(enumerate(table))
        for letter in text:
            found = False
            for i,row in table_enumerate:
                for j,item in enumerate(row):
                    if letter == item:
                        encrypted += table_label[i]+table_label[j]#+" "
                        found = True
                        break
                if found:
                    break
            if (not found)  and  when_not_found=="ERROR":
                raise ValueError(f'letter "{letter}" not found in alphabet+keys')
        return encrypted
