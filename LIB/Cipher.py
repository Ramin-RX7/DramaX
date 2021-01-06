import sys
import math
import random
from abc import ABC, abstractmethod#, abstractstaticmethod
from typing import Union
from collections import OrderedDict


ALL_CHARS = r""" 0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@$%^&*()-=_+[]{};'\:"|,./<>?`~#"""   # note the space at the front
LOWERS   = 'abcdefghijklmnopqrstuvwxyz'
UPPERS   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS   = '0123456789'
SYMBOLS  = r"""!@$%^&*()-=_+[]{};'\:"|,./<>?`~"""
SPACE    = ' '

TEXT_LENGTH = 0

CIPHERS_LIST = ('Polybius','ADFGX','ADFGVX','Atbash','ColumnarTransposition'
                'Bazeries','Beaufort','Bifid','Caesar','Chao','Autokey','Baconian',
                'FourSquare','Gronsfeld','Keyword','Myszkowski','Nihilist',
                'Playfair','RailFence','rot13','Porta','Transpose','ThreeSquare',
                'SimpleSubstitution','XOR','Vigenere','TwoSquare','Trifid',)


class CryptoMath:

    @staticmethod
    def gcd(a, b):
        # Return the GCD of a and b using Euclid's Algorithm
        while a != 0:
            a, b = b % a, a
        return b

    @staticmethod
    def findModInverse(a, m):
        # Returns the modular inverse of a % m, which is
        # the number x such that a*x % m = 1

        if CryptoMath.gcd(a, m) != 1:
            return None # no mod inverse if a & m aren't relatively prime

        # Calculate using the Extended Euclidean Algorithm:
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3 # // is the integer division operator
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m


class Present:
    pass


class _Cipher(ABC):
    
    class Tools:
        pass

    @abstractmethod
    def encrypt(self):
        '''Help Not Provided or Cipher is Under MainTaince'''
        pass

    @abstractmethod
    def decrypt(self):
        '''Help Not Provided or Cipher is Under MainTaince'''
        pass


class _PolybiusSquare:
    """
    PolybiusSquare. It's used by many classical ciphers
    """
    __alphabet = None
    __side = 0

    def __init__(self, alphabet, key=""):
        keyi = []
        if key:
            for char in key:
                index = self.__find_index_in_alphabet(char, alphabet)
                keyi.append(index)
            # remove duplicates
            keyi = OrderedDict.fromkeys(keyi)

        alph_out = []
        for i in keyi:
            alph_out.append(alphabet[i])

        for i in range(len(alphabet)):
            if i not in keyi:
                alph_out.append(alphabet[i])

        self.__alphabet = alph_out
        self.__side = int(math.ceil(math.sqrt(len(alphabet))))

    def __find_index_in_alphabet(self, char, alphabet):
        for j in range(len(alphabet)):
            try:
                alphabet[j].index(char)
                break
            except ValueError:
                pass
        return j

    def get_coordinates(self, char):
        for j in range(len(self.__alphabet)):
            try:
                self.__alphabet[j].index(char)
                break
            except ValueError:
                pass

        row = int(j / self.__side)
        column = j % self.__side
        return (row, column)

    def get_char(self, row, column):
        return self.__alphabet[row * self.__side + column][0]

    def get_columns(self):
        return self.__side

    def get_rows(self):
        return int(len(self.__alphabet) / self.__side)



class Polybius:
    """
    The Polybius Cipher
    """
    class Tools:
        @staticmethod
        def __encDec(self, alphabet, text, key, isEncrypt=True):
            square = _PolybiusSquare(alphabet, key)
            res = ""
            header = range(1, square.get_columns() + 1)
            header = "".join(map(str, header))
            if isEncrypt:
                for char in text:
                    coords = square.get_coordinates(char)
                    row = coords[0]
                    column = coords[1]
                    res += header[row] + header[column]
            else:
                for i in range(0, len(text), 2):
                    try:
                        row = header.index(text[i])
                    except ValueError:
                        wrchar = text[i].encode('utf-8')
                        raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                    try:
                        column = header.index(text[i+1])
                    except ValueError:
                        wrchar = text[i+1].encode('utf-8')
                        raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                    res += square.get_char(row, column)
            return res

    @staticmethod
    def encrypt(text, alphabet, key=""):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Polybius.Tools.__encDec(alphabet, text, key, True)

    @staticmethod
    def decrypt(text, alphabet, key=""):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Polybius.Tools.__encDec(alphabet, text, key, False)

class _ADFGX:
    @staticmethod
    def decrypt(text, key, alphabet, header):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        keysize = len(key)
        size = len(text)
        rows = int(math.ceil(size/keysize))
        reminder = size % keysize
        keyword = list(key)
        indices = sorted(range(len(keyword)), key=lambda k: keyword[k])

        myarr = list(indices)
        lefti = 0
        righti = 0
        for key, value in enumerate(indices):
            righti = lefti
            righti += rows
            if reminder > 0 and value > reminder-1:
                righti -= 1
            myarr[value] = text[lefti:righti]
            lefti = righti

        column = 0
        row = 0
        res = ''
        for _ in range(size):
            res += (myarr[column][row])
            column += 1
            if column == keysize:
                column = 0
                row += 1
            
        try:
            code = []
            for char in res:
                code.append(str(header.index(char)+1))
        except ValueError:
            wrchar = bytes(char,'utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in the alphabet!")

        code = "".join(code)
        return Polybius.decrypt(code, alphabet=alphabet)
    @staticmethod
    def encrypt(text, key, alphabet, header):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        ans0 = Polybius.encrypt(text, alphabet=alphabet)
        ans = [header[int(char)-1] for char in ans0]

        keyword = list(key)
        keysize = len(key)
        size = len(ans)
        indices = sorted(range(len(keyword)), key=lambda k: keyword[k])
        row = int(math.ceil(size/keysize))
        for i in range(row):
            p = ""
            for j in range(keysize):
                myi = i*keysize+j
                if myi < len(ans):
                    eee = ans[myi]
                    p += "".join(eee)

        ans2 = ""
        for s in indices:
            ind = s
            while ind < size:
                p = ans[ind]
                ans2 += p
                ind += keysize

        return ans2
class ADFGX(_Cipher):
    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return _ADFGX.decrypt(text, key, alphabet, 'ADFGX')
    @staticmethod
    def encrypt(text, key, alphabet, header):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return _ADFGX.encrypt(text, key, alphabet, 'ADFGX')
class ADFGVX(_Cipher):
    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return _ADFGX.decrypt(text, key, alphabet, 'ADFGVX')
    @staticmethod
    def encrypt(text, key, alphabet, header):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return _ADFGX.encrypt(text, key, alphabet, 'ADFGVX')

class Affine(_Cipher):
    """
    - Case Sensetive
    - Supports Numbers and Symbols
    - Both keys should be integer 
    - key1 should be relatively prime to len(alphabet)
    - key1 will be converted to  range(1,len(alphabet))
    - key2 will be converted to  range(0,len(alphabet))

    """

    '''
    def hackAffine(message):
        print()
        print('Hacking...')
        print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
        # brute-force by looping through every possible key
        for key in range(len(SYMBOLS) ** 2):
            keyA = getKeyParts(key)[0]
            if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
                continue
            decryptedText = decryptMessage(key, message)
            #if not SILENT_MODE:
            #    print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
            if detectEnglish.isEnglish(decryptedText):
                print()
                print(' Possible encryption hack:')
                print(' Key1: %s  |  Key2: %s' % (str(key)[:2],str(key)[2:]))
                print(f' Decrypted Message:  {rx7.style(decryptedText[:200],BG="dark_green")}')

                print()
                print(' Enter D for done, or just press Enter to continue hacking:')
                response = input('> ')
                if response.strip().upper() in ('DONE','D'):
                    return decryptedText
        return None

    def HACK(myMessage):
        hackedMessage = hackAffine(myMessage)
        if hackedMessage != None:
            print(f' Copying hacked message to clipboard:  {hackedMessage}')
            pyperclip.copy(hackedMessage)
        else:
            print(' Failed to hack encryption.')
    '''


    class Tools:
        @staticmethod
        def getInverse(key1, alphabet):
            for i in range(1, len(alphabet)):
                if ((int(key1)*int(i)) % int(len(alphabet))) == 1:
                    return i
            return 0

        @staticmethod
        def _EncDec(text, keys, alphabet, Enc):
            '''
            enc:
            for symbol in message:
                if symbol in SYMBOLS:
                    symIndex = SYMBOLS.find(symbol)
                    ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
                else:
                    ciphertext += symbol
            return ciphertext

            dec:
            modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
            for symbol in message:
                if symbol in SYMBOLS:
                    symIndex = SYMBOLS.find(symbol)
                    plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
                else:
                    plaintext += symbol
            return plaintext            
            '''
            key1 = keys[0]
            key2 = keys[1]
            ans = ""
            try:
                for char in text:
                    if Enc:
                        alphI = (alphabet.index(char) * key1 + key2) % len(alphabet)
                    else:
                        aInverse = Affine.Tools.getInverse(key1, alphabet)
                        alphI = (aInverse * (alphabet.index(char) - key2)) % len(alphabet)
                    enc = alphabet[alphI]
                    ans += enc
            except ValueError:
                raise Exception("Can't find char '" + char + "' of text in alphabet!")
            return ans

    @staticmethod
    def encrypt(text, keys, alphabet=ALL_CHARS):
        '''
        text:  String to encrypt with Affine Cipher\n
        keys:  List of keys to use.
         (See Affine help to understand keys of this cipher)\n
        alphabet: a subscriptable iterable which contains all characters  
        you want to use for Affine Cipher (default= lowers+uppers+digits+symbols)
        '''
        return Affine.Tools._EncDec(text, keys, alphabet, True)

    @staticmethod
    def decrypt(text, keys, alphabet=ALL_CHARS):
        '''
        text:  String to decrypt with Affine Cipher\n
        keys:  List of keys to use. ([key1, key2])
         (See Affine help to understand keys of this cipher)\n
        alphabet: a subscriptable iterable which contains all characters  
        you want to use for Affine Cipher (default= lowers+uppers+digits+symbols)
        '''
        return Affine.Tools._EncDec(text, keys, alphabet, False)

def atbash(text):
    
    cipher = ''
    for letter in text:
        if letter.lower() in LOWERS:
            cipher +=  LOWERS[25-LOWERS.index(letter)]
        else:
            cipher += letter

    return cipher
class Atbash(_Cipher):
    @staticmethod
    def encrypt(text):
        return atbash(text)
    @staticmethod
    def decrypt(text):
        return atbash(text)

class Autokey(_Cipher):
    """
    The Autokey Cipher (Vigenere Extension)
    Case Sensetive
    Support Numbers and Symbols
    Key must be in alphabets
    """
    class Tools:
        @staticmethod
        def _EncDec(text, key, alphabet, isEncrypt):
            ans = ""
            for i in range(len(text)):
                m = text[i]
                if i < len(key):
                    k = key[i]
                else:
                    if isEncrypt == 1:
                        k = text[i - len(key)]
                    else:
                        k = ans[i - len(key)]
                try:
                    alphI = alphabet.index(m)
                except ValueError:
                    wrchar = m.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                try:
                    alphI += isEncrypt * alphabet.index(k)
                except ValueError:
                    wrchar = k.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                alphI = alphI % len(alphabet)
                enc = alphabet[alphI]
                ans += enc
            return ans

    @staticmethod
    def encrypt(text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Autokey.Tools._EncDec(text, key, alphabet, 1)

    @staticmethod
    def decrypt(text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Autokey.Tools._EncDec(text, key, alphabet, -1)

class Baconian(_Cipher):
    """
    Baconian Cipher\n
    - Only Letters
    - Case Insensetive
    """
    _baconian_dict = {'a':'aaaaa', 'b':'aaaab', 'c':'aaaba', 'd':'aaabb',
                      'e':'aabaa', 'f':'aabab', 'g':'aabba', 'h':'aabbb', 
                      'i':'abaaa', 'j':'abaab', 'k':'ababa', 'l':'ababb', 
                      'm':'abbaa', 'n':'abbab', 'o':'abbba', 'p':'abbbb', 
                      'q':'baaaa', 'r':'baaab', 's':'baaba', 't':'baabb', 
                      'u':'babaa', 'v':'babab', 'w':'babba', 'x':'babbb', 
                      'y':'bbaaa', 'z':'bbaab'}

    _baconian_dict_24 = {'a':'aaaaa', 'b':'aaaab', 'c':'aaaba', 'd':'aaabb',
                         'e':'aabaa', 'f':'aabab', 'g':'aabba', 'h':'aabbb', 
                         'i':'abaaa', 'j':'abaaa', 'k':'abaab', 'l':'ababa', 
                         'm':'ababb', 'n':'abbaa', 'o':'abbab', 'p':'abbba', 
                         'q':'abbbb', 'r':'baaaa', 's':'baaab', 't':'baaba', 
                         'u':'baabb', 'v':'baabb', 'w':'babaa', 'x':'babab', 
                         'y':'babba', 'z':'babbb'}


    @staticmethod
    def encrypt(text, all_letters=True):
        Dict = Baconian._baconian_dict
        if not all_letters:
            Dict = Baconian._baconian_dict_24

        cipher = '' 
        for letter in text.lower(): 
            if(letter != ' '):
                cipher += Dict[letter] 
            else:
                cipher += ' '
        return cipher 

    @staticmethod
    def decrypt(text, all_letters=True):
        Dict = Baconian._baconian_dict
        if not all_letters:
            Dict = Baconian._baconian_dict_24

        decipher = '' 
        i = 0
        while True :
            if i < len(text)-4:
                substr = text[i:i + 5]
                if substr[0] != ' ':
                    decipher += list(Dict.keys())[list(Dict.values()).index(substr)]
                    i += 5
                else: 
                    decipher += ' '
                    i += 1
            else: 
                break
        return decipher

class Bazeries(_Cipher):
    """
    The Bazeries Cipher
    """
    class Tools:
        @staticmethod
        def __encDec(text, key, alphabet, isEncrypt):
            square1 = _PolybiusSquare(alphabet)

            # key is a number, make it a string
            square2 = _PolybiusSquare(alphabet, key[1])

            # prepare text: group and reverse
            temp = key[0]
            groups = []
            while temp > 0:
                rmd = temp % 10
                temp = int(temp / 10)
                groups.append(rmd)
            groups = groups[::-1]

            i = 0
            j = 0
            revtext = ""
            while i < len(text):
                num = groups[j]
                str1 = text[int(i):int(i+num)]
                revtext += str1[::-1]
                i += num
                j += 1
                if j == len(groups):
                    j = 0

            # now we have reversed text and we encrypt
            ret = ""
            if isEncrypt:
                for char in revtext:
                    coords = square1.get_coordinates(char)
                    ret += square2.get_char(coords[1], coords[0])
            else:
                for char in revtext:
                    coords = square2.get_coordinates(char)
                    ret += square1.get_char(coords[1], coords[0])
            return ret

    @staticmethod
    def encrypt(text, key=None, alphabet=ALL_CHARS):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Bazeries.Tools.__encDec(alphabet, text, key, True)

    @staticmethod
    def decrypt(text, key=None, alphabet=ALL_CHARS):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Bazeries.Tools.__encDec(alphabet, text, key, False)

def beaufort(text, key, alphabet):
    ans = ""
    for i in range(len(text)):
        char = text[i]
        keychar = key[i % len(key)]
        try:
            alphIndex = alphabet.index(keychar)
        except ValueError:
            wrchar = keychar.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        try:
            alphIndex -= alphabet.index(char)
        except ValueError:
            wrchar = char.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        alphIndex %= len(alphabet)
        ans += alphabet[alphIndex]
    return ans
class Beaufort(_Cipher):
    """
    The Beaufort Cipher
    """
    @staticmethod
    def encrypt(text, key, alphabet=ALL_CHARS):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return beaufort(text, key, alphabet)

    @staticmethod
    def decrypt(text, key, alphabet=ALL_CHARS):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return beaufort(text, key, alphabet)

class Bifid(_Cipher):
    """
    The Bifid Cipher
    """

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        if not key > 0:
            key = len(text)
        code = Polybius.encrypt(text, alphabet=alphabet)
        even = code[::2]
        odd = code[1::2]
        ret = ""
        for i in range(0, len(even), key):
            ret += even[i:i+key] + odd[i:i+key]
        return Polybius.decrypt(ret, alphabet=alphabet)

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        if not key > 0:
            key = len(text)
        code = Polybius.encrypt(text, alphabet=alphabet)
        even = ""
        odd = ""
        rem = len(code) % (key << 1)
        for i in range(0, len(code)-rem, key << 1):
            ikey = i+key
            even += code[i:ikey]
            odd += code[ikey:ikey+key]

        even += code[-rem:-(rem >> 1)]
        odd += code[-(rem >> 1):]

        code = ""
        for i in range(len(even)):
            code += even[i] + odd[i]
        return Polybius.decrypt(code, alphabet=alphabet)

class Caesar(_Cipher):
    """
    The Caesar Cipher
    """

    class Tools:
        @staticmethod
        def __encDec(text, key, alphabet, isEncrypt):
            ans = ""
            for char in text:
                try:
                    alphIndex = alphabet.index(char)
                except ValueError:
                    wrchar = char.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                alphIndex = (alphIndex + isEncrypt * key) % len(alphabet)
                ans += alphabet[alphIndex]
            return ans

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: encrypted text
        :rtype: string
        """
        return Caesar.Tools.__encDec(text, key, alphabet, 1)

    @staticmethod
    def decrypt(text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: decrypted text
        :rtype: string
        """
        return Caesar.Tools.__encDec(text, key, alphabet, -1)

class Chao(_Cipher):
    """
    The Chaocipher
    """
    class Tools:
        @staticmethod
        def permuteAlphabet(alphabet, i, isCrypt):
            alphabet = alphabet[i:] + alphabet[:i]     
            nadir = len(alphabet) / 2
            if isCrypt:
                alphabet = alphabet[0] + alphabet[2:int(nadir)+1] + alphabet[1] + alphabet[int(nadir)+1:]    
            else:
                alphabet = alphabet[1:] + alphabet[0]
                alphabet = alphabet[:2] + alphabet[3:int(nadir)+1] + alphabet[2] + alphabet[int(nadir)+1:]    
            return alphabet

        @staticmethod
        def _EncDec(text, key, tp_alphabet, isEncrypt):
            ret = ''
            for c in text:
                try:
                    if isEncrypt:
                        i = tp_alphabet.index(c)
                        ret += key[i]
                    else:
                        i = key.index(c)
                        ret += tp_alphabet[i]
                except ValueError:
                    wrchar = c.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                key = Chao.Tools.permuteAlphabet(key, i, True)
                tp_alphabet = Chao.Tools.permuteAlphabet(tp_alphabet, i, False)
            return ret 

    @staticmethod
    def encrypt(text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: encrypted text
        :rtype: string
        """
        return Chao.Tools._EncDec(text, key, alphabet, True)

    @staticmethod
    def decrypt(text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: decrypted text
        :rtype: string
        """
        return Chao.Tools._EncDec(text, key, alphabet, False)

class ColumnarTransposition(_Cipher):
    """
    The Columnar Transposition Cipher
    """
    class Tools:
        @staticmethod
        def get_index_in_alphabet(char, alphabet):
            for j in range(len(alphabet)):
                try:
                    alphabet[j].index(char)
                    break
                except ValueError:
                    pass
            return j

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        # add endings to the text to fill the square
        rmd = len(text) % len(key)
        if rmd != 0:
            text += alphabet[-1] * (len(key) - rmd)

        chars = [ColumnarTransposition.Tools.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])

        ret = u""
        for i in range(len(key)):
            ret += text[keyorder1[i][0]::len(key)]

        return ret

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        chars = [ColumnarTransposition.Tools.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder = sorted(enumerate(chars), key=lambda x: x[1])
        ret = u""
        rows = int(len(text) / len(key))

        cols = [0] * len(key)
        for i, item in enumerate(range(0, len(text), rows)):
            cols[keyorder[i][0]] = text[item: item + rows]

        for j in range(rows):
            for i in range(len(cols)):
                ret += cols[i][j]
        return ret

class FourSquare(_Cipher):
    """
    The Four-Square Cipher
    """

    class Tools:
        @staticmethod
        def __enc(text, key, alphabet, isEncrypt):
            square01 = _PolybiusSquare(alphabet, key[0])
            square10 = _PolybiusSquare(alphabet, key[1])
            square = _PolybiusSquare(alphabet, "")

            # text encryption
            if len(text) % 2:
                text += alphabet[-1][0]
            odd = text[1::2]
            even = text[::2]
            enc = u""
            if isEncrypt:
                for i in range(len(even)):
                    coords = square.get_coordinates(even[i])
                    row00 = coords[0]
                    column00 = coords[1]

                    coords = square.get_coordinates(odd[i])
                    row11 = coords[0]
                    column11 = coords[1]

                    enc += square01.get_char(row00, column11)
                    enc += square10.get_char(row11, column00)
            else:
                for i in range(len(even)):
                    coords = square01.get_coordinates(even[i])
                    row00 = coords[0]
                    column00 = coords[1]

                    coords = square10.get_coordinates(odd[i])
                    row11 = coords[0]
                    column11 = coords[1]

                    enc += square.get_char(row00, column11)
                    enc += square.get_char(row11, column00)
            return enc

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return FourSquare.Tools.__enc(text, key, alphabet, True)

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return FourSquare.Tools.__enc(text, key, alphabet, False)

class Gronsfeld(_Cipher):
    """
    The Gronsfeld Cipher
    """
    class Tools:
        @staticmethod
        def _EncDec(text, key, alphabet, isEncrypt):
            ans = ""
            for i in range(len(text)):
                char = text[i]
                keyi = key[i % len(key)]
                try:
                    alphIndex = (alphabet.index(char) +
                            isEncrypt * keyi) % len(alphabet)
                except ValueError:
                    wrchar = char.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                ans += alphabet[alphIndex]
            return ans

    @staticmethod
    def encrypt(text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Gronsfeld.Tools._EncDec(alphabet, key, text, 1)

    @staticmethod
    def decrypt(text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Gronsfeld.Tools._EncDec(text, key, alphabet, -1)

class Keyword(_Cipher):
    """
    The Keyword Cipher
    """
    class Tools:
        '''
        @staticmethod
        def __removeDup(input_str):
            newstring = input_str[0]
            for i in range(len(input_str)):
                if newstring[(len(newstring) - 1)] != input_str[i]:
                    newstring += input_str[i]
                else:
                    pass
            return newstring
        '''
        @staticmethod
        def __encDec(alphabet, key, text, isEncrypt):
            # remove repeats of letters in the key
            newkey = "".join(OrderedDict.fromkeys(key))
            # create the substitution string
            longkey = "".join(OrderedDict.fromkeys(newkey+"".join(alphabet)))
            # do encryption
            ans = ""
            for i in range(len(text)):
                m = text[i]
                try:
                    if isEncrypt == 1:
                        index = alphabet.index(m)
                        enc = longkey[index]
                    else:
                        index = longkey.index(m)
                        enc = alphabet[index]
                except ValueError:
                    wrchar = m.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                ans += enc
            return ans
    
    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Keyword.Tools.__encDec(alphabet, key, text, 1)

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Keyword.Tools.__encDec(alphabet, key, text, -1)

class Myszkowski(_Cipher):
    """
    -> Transposition
    The Myszkowski Transposition Cipher
    Key should be iterable and len(key) should be <= len(text)
    """

    class Tools:
        @staticmethod
        def _get_index_in_alphabet(char, alphabet):
            for j in range(len(alphabet)):
                try:
                    alphabet[j].index(char)
                    break
                except ValueError:
                    pass
            return j

    @staticmethod
    def encrypt(text, key, alphabet=ALL_CHARS):

        chars = [Myszkowski.Tools._get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])
        prev_key_char = ""
        cols = []
        col0 = []

        for i in range(len(key)):
            key_char = keyorder1[i][1]
            if prev_key_char != key_char:
                if len(col0) > 0:
                    cols.append(col0)
                col0 = []
                prev_key_char = key_char
            col0.append(text[keyorder1[i][0]::len(key)])

        if len(col0) > 0:
            cols.append(col0)

        ret = u""
        for col in cols:
            if len(col) == 1:
                ret += col[0]
            else:
                i = 0
                for i in range(len(col[0])):
                    for col0 in col:
                        try:
                            ret += col0[i]
                        except IndexError:
                            pass
        return ret

    @staticmethod
    def decrypt(text, key, alphabet=ALL_CHARS):
        
        chars = [Myszkowski.Tools._get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])

        next_arr = []
        temp = []
        it = iter(keyorder1)
        try:
            prev, current = None, next(it)
            while True:
                prev = current
                temp.append(prev[0])
                current = next(it)
                if (prev and prev[1] != current[1]):
                    next_arr.append(temp)
                    temp = []
        except StopIteration:
            pass

        if len(temp) > 0:
            next_arr.append(temp)

        rmd, quotient = len(text) % len(key), int(len(text) / len(key))
        ret_arr = [None] * len(key)
        i = 0
        for ar in next_arr:
            len_sum = 0
            for index in ar:
                index_len = quotient
                if index < rmd:
                    index_len += 1

                len_sum += index_len
            tmp = text[int(i):int(i+len_sum)]
            i += len_sum
            for j, index in enumerate(ar):
                ret_arr[index] = tmp[j::len(ar)]

        ret = ""
        for row in range(0, quotient):
            for item in ret_arr:
                ret += item[row]

        row = quotient
        for i in range(0, rmd):
            ret += ret_arr[i][row]
        return ret

class Nihilist(_Cipher):
    """
    The Nihilist Cipher
    """

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        code = Polybius.encrypt(text, alphabet=alphabet)
        enc = ""
        for i in range(0, len(code), 2):
            char = Polybius.encrypt(key[(i >> 1) % len(key)],
                                        alphabet=alphabet)
            enc += str(int(code[i:i+2]) + int(char)) + " "
        return enc.rstrip()

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        code = text.split(' ')
        code = list(map(int, code))
        dec = ""
        for i in range(0, len(code)):
            char = Polybius.encrypt(key[i % len(key)],
                                        alphabet=alphabet)
            pair = str(code[i] - int(char))
            dec += Polybius.decrypt(pair, alphabet=alphabet)
        return dec

class Playfair(_Cipher):
    """
    The Playfair Cipher
    """
    class Tools:
        @staticmethod
        def __dec_two_letters(a, b, square):
            cols = square.get_columns()
            rows = square.get_rows()

            coords = square.get_coordinates(a)
            arow = coords[0]
            acolumn = coords[1]

            coords = square.get_coordinates(b)
            brow = coords[0]
            bcolumn = coords[1]

            if arow == brow:
                a = square.get_char(arow, (acolumn - 1) % cols)
                b = square.get_char(brow, (bcolumn - 1) % cols)
            elif acolumn == bcolumn:
                arow -= 1
                if arow >= rows:
                    arow = 0
                a = square.get_char(arow, acolumn)

                brow -= 1
                if brow >= rows:
                    brow = 0
                b = square.get_char(brow, bcolumn)
            else:
                a = square.get_char(arow, bcolumn)
                b = square.get_char(brow, acolumn)
            return a + b

        @staticmethod
        def __enc_two_letters(a, b, square):
            cols = square.get_columns()
            rows = square.get_rows()

            coords = square.get_coordinates(a)
            arow = coords[0]
            acolumn = coords[1]

            coords = square.get_coordinates(b)
            brow = coords[0]
            bcolumn = coords[1]

            if arow == brow:
                a = square.get_char(arow, (acolumn + 1) % cols)
                b = square.get_char(brow, (bcolumn + 1) % cols)
            elif acolumn == bcolumn:
                arow += 1
                if arow >= rows:
                    arow = 0
                a = square.get_char(arow, acolumn)
                brow += 1
                if brow >= rows:
                    brow = 0
                b = square.get_char(brow, bcolumn)
            else:
                a = square.get_char(arow, bcolumn)
                b = square.get_char(brow, acolumn)
            return a + b

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        enc = u""
        insert_char = 'x'
        i = 1
        square = _PolybiusSquare(alphabet, key)

        while i < len(text):
            if text[i-1] == text[i]:
                text = text[:i] + insert_char + text[i:]
            enc += Playfair.Tools.__enc_two_letters(text[i-1], text[i], square)
            i += 2

        if len(text) & 1:
            enc += Playfair.Tools.__enc_two_letters(text[-1], insert_char, square)

        return enc

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        dec = ""
        insert_char = 'x'

        square = _PolybiusSquare(alphabet, key)

        for i in range(1, len(text), 2):
            pair = Playfair.Tools.__dec_two_letters(text[i-1], text[i], square)
            if len(dec) > 1 and dec[-1] == insert_char and pair[0] == dec[-2]:
                dec = dec[:-1] + pair[0]
                dec += pair[1]
            else:
                dec += Playfair.Tools.__dec_two_letters(text[i-1], text[i], square)
        if dec[-1] == insert_char:
            dec = dec[:-1]
        return dec

class Porta(_Cipher):
    '''
    Supports All Characters (BUT ONLY LETTERS WILL BE ENCRYPTED)
    Case Insensetive
    Key Insensetive
    Key must be string with 1<word<len(word) length which only cntains letters
    '''
    class Tools:
        @staticmethod
        def generate_table(key):
            return [Porta.Tools.Porta_Dict[char] for char in key.upper()]

        @staticmethod
        def get_position(table, char):
            if char in table[0]:
                row = 0
            else:
                row = 1 if char in table[1] else -1
            return (None, None) if row == -1 else (row, table[row].index(char))
        
        @staticmethod
        def get_opponent(table, char):
            row, col = Porta.Tools.get_position(table, char.upper())
            if row == 1:
                return table[0][col]
            else:
                return table[1][col] if row == 0 else char

        Porta_Dict = {
            "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
            "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
            "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
            "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
            "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
            "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
            "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
            "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
            "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
            "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
            "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
            "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
            "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
            "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
            "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
            "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
            "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
            "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
            "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
            "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
            "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
            "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
            "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
            "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
            "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
            "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
        }

    @staticmethod
    def encrypt(word, key):
        porta(word,key)    
    @staticmethod
    def decrypt(word, key):
        return porta(word, key)
def porta(text, key):
    cipher = ""
    count = 0
    table = Porta.Tools.generate_table(key)
    for char in text.upper():
        cipher += Porta.Tools.get_opponent(table[count], char)
        count = (count + 1) % len(table)
    return cipher

class RailFence(_Cipher):
    '''
    -> Transposition
    Case Sensetive.
    Support Numbers and Symbols.
    Key Must be an Integer Lower Than Word Length and Higher than 1.
    '''
    @staticmethod
    def encrypt(text, key):  
        rail = [ ['\n' for _2 in range(len(text))] for _ in range(key)]
        dir_down = False
        row, col = 0, 0
        
        for i in range(len(text)):
            if (row == 0) or (row == key - 1): 
                dir_down = not dir_down
            rail[row][col] = text[i] 
            col += 1
            if dir_down: 
                row += 1
            else: 
                row -= 1

        result = [] 
        for i in range(key): 
            for j in range(len(text)): 
                if rail[i][j] != '\n': 
                    result.append(rail[i][j]) 

        return "".join(result)

    @staticmethod
    def decrypt(text, key): 
        rail = [['\n' for i in range(len(text))]  
                    for j in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(text)): 
            if row == 0: 
                dir_down = True
            if row == key - 1: 
                dir_down = False 
            rail[row][col] = '*'
            col += 1 
            if dir_down: 
                row += 1
            else: 
                row -= 1

        index = 0
        for i in range(key): 
            for j in range(len(text)): 
                if ((rail[i][j] == '*') and
                (index < len(text))): 
                    rail[i][j] = text[index] 
                    index += 1

        result = [] 
        row, col = 0, 0
        for i in range(len(text)): 
            if row == 0: 
                dir_down = True
            if row == key-1: 
                dir_down = False
            if (rail[row][col] != '*'): 
                result.append(rail[row][col]) 
                col += 1
            if dir_down: 
                row += 1
            else: 
                row -= 1

        return "".join(result)

def rot13(word):
    '''
    Case Sensetive
    Support Numbers and Symbols But Not Work on Them (Under Maintaince)
    '''
    result = ""
    for v in word:
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
class Rot13(_Cipher):
    @staticmethod
    def encrypt(word, key=None):
        return rot13(word)
    @staticmethod
    def decrypt(word, key=None):
        return rot13(word)

class SimpleSubstitution(_Cipher):
    """
    The Simple Substitution Cipher
    """
    class Tools:
        @staticmethod
        def __encDec(text, key, alphabet, isEncrypt):
            if len(alphabet) != len(key):
                return

            ans = ""
            for i in range(len(text)):
                m = text[i]
                k = ""
                try:
                    if isEncrypt == 1:
                        k = key[alphabet.index(m)]
                    else:
                        k = alphabet[key.index(m)]
                except ValueError:
                    wrchar = m.encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                ans += k
            return ans

    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return SimpleSubstitution.Tools.__encDec(text, key, alphabet, 1)

    @staticmethod
    def decrypt(text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return SimpleSubstitution.Tools.__encDec(text, key, alphabet, -1)

class ThreeSquare(_Cipher):
    """
    The Three Square Cipher
    """
    class Tools:
        @staticmethod
        def __encDec(text, key, alphabet, isEncrypt):
            square1 = _PolybiusSquare(alphabet, key[0])
            square2 = _PolybiusSquare(alphabet, key[1])
            square3 = _PolybiusSquare(alphabet, key[2])

            enc = u""
            if isEncrypt:
                if len(text) % 2:
                    text += alphabet[-1][0]

                odd = text[1::2]
                even = text[::2]

                for i in range(len(even)):
                    row1, column1 = square1.get_coordinates(even[i])
                    row2, column2 = square2.get_coordinates(odd[i])

                    rows = square1.get_rows()
                    index = random.randrange(rows)
                    left = square1.get_char(index, column1)

                    middle = square3.get_char(row1, column2)

                    cols = square2.get_columns()
                    index = random.randrange(cols)
                    right = square2.get_char(row2, index)

                    enc += left + middle + right
            else:
                trigrams = []
                i = 0
                while i < len(text):
                    trigrams.append(text[i:i+3])
                    i += 3

                for trigram in trigrams:
                    col1 = square1.get_coordinates(trigram[0])[1]
                    row3, col3 = square3.get_coordinates(trigram[1])
                    row2 = square2.get_coordinates(trigram[2])[0]
                    enc += square1.get_char(row3, col1)
                    enc += square2.get_char(row2, col3)
            return enc

    @staticmethod
    def encrypt(text, key=None, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return ThreeSquare.Tools.__encDec(text, key, alphabet, True)

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return ThreeSquare.Tools.__encDec(text, key, alphabet, False)

class Transpose(_Cipher):
    '''
    len(word)>len(key)>1
    '''
    @staticmethod
    def encrypt(text, key):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    @staticmethod
    def decrypt(text, key):
        import math
        numOfColumns = math.ceil(len(text) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)

class Trifid(_Cipher):
    """
    The Trifid Cipher
    Key: integer <= len(text)
    """

    class Tools:
        @staticmethod
        def _code(text, alphabet):
            code = ""
            for char in text:
                for index in range(len(alphabet)):
                    try:
                        alphabet[index].index(char)
                        break
                    except ValueError:
                        pass
                square = int(index / 9)
                index = index % 9
                row = int(index / 3)
                col = index % 3
                code += str(square+1) + str(row+1) + str(col+1)
            return code
        @staticmethod
        def _decode(text, alphabet):
            code = ""
            for i in range(0, len(text), 3):
                square = int(text[i])-1
                row = int(text[i+1])-1
                col = int(text[i+2])-1
                index = square*9 + row*3 + col
                code += alphabet[index][0]
            return code


    @staticmethod
    def encrypt(text, key, alphabet=ALL_CHARS):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        key = int(key)
        if not key > 0:
            key = len(text)

        code = Trifid.Tools._code(text, alphabet)

        code0 = ""
        for j in range(0, len(text)*3, 3*key):
            for i in range(3):
                code0 += code[j+i:j+3*key:3]

        code = Trifid.Tools._decode(code0, alphabet)
        return code

    @staticmethod
    def decrypt(text, key=TEXT_LENGTH, alphabet=ALL_CHARS):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        key = int(key)
        if not key > 0:
            key = len(text)
        
        code = Trifid.Tools._code(text, alphabet)

        code0 = ""
        rmd = (len(text) % key)
        for j in range(0, (len(text) - rmd) * 3, 3*key):
            for i in range(key):
                code0 += code[j+i:j+3*key:key]

        j = (len(text) - rmd) * 3
        for i in range(rmd):
            code0 += code[j+i:j+3*rmd:rmd]

        code = Trifid.Tools._decode(code0, alphabet)
        return code

def two_square(text, key, alphabet):
    square1 = _PolybiusSquare(alphabet, key[0])
    square2 = _PolybiusSquare(alphabet, key[1])

    # text encryption
    if len(text) % 2:
        text += alphabet[-1][0]
    odd = text[1::2]
    even = text[::2]
    enc = u""

    for i in range(len(even)):
        coords = square1.get_coordinates(even[i])
        row1 = coords[0]
        column1 = coords[1]

        coords = square2.get_coordinates(odd[i])
        row2 = coords[0]
        column2 = coords[1]

        if column1 == column2:
            enc += square1.get_char(row2, column1)
            enc += square2.get_char(row1, column1)
        else:
            enc += square1.get_char(row1, column2)
            enc += square2.get_char(row2, column1)
    return enc
class TwoSquare(_Cipher):
    """
    The Two-Square Cipher
    """
    @staticmethod
    def encrypt(text, key, alphabet):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return two_square(alphabet, text, key)

    @staticmethod
    def decrypt(text, key, alphabet):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return two_square(alphabet, text, key)

class Vic(_Cipher):
    """
    -> Polybius square
    The Vic Cipher
    """
    class Tools:
        @staticmethod
        def _find_index_in_alphabet(char, alphabet):
            for j in range(len(alphabet)):
                try:
                    alphabet[j].index(char)
                    break
                except ValueError:
                    pass
            return j

        @staticmethod
        def _EncDec(text, key, alphabet, do_encrypt):
            columns = []
            width = 10
            # define columns with null string
            for i, value in enumerate(alphabet):
                if value == "":
                    columns.append(i)

            # encode chars to numbers
            code = ""
            for char in text:
                j = Vic.Tools._find_index_in_alphabet(char, alphabet)
                row = int(j / width)
                if row > 0:
                    column = j % width
                    code += str(columns[row-1]) + str(column)
                else:
                    code += str(j)

            enc = ""
            if do_encrypt:
                # addition by key
                for i in range(0, len(code)):
                    enc += str((int(code[i]) + int(key[i % len(key)])) % 10)
            else:
                # subraction by key
                for i in range(0, len(code)):
                    enc += str((int(code[i]) - int(key[i % len(key)])) % 10)

            # encode numbers to chars
            enc2 = ""
            row = 0
            for i in range(0, len(enc)):
                if row == 0 and (int(enc[i]) in columns):
                    row = columns.index(int(enc[i])) + 1
                else:
                    enc2 += alphabet[row * width + int(enc[i])][0]
                    row = 0
            return enc2

    @staticmethod
    def encrypt(text, key, alphabet=ALL_CHARS):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Vic.Tools._EncDec(text, key, alphabet, True)

    @staticmethod
    def decrypt(text, key, alphabet=ALL_CHARS):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return Vic.Tools._EncDec(text, key, alphabet, False)

class Vigenere(_Cipher):
    '''
    Case Sensetive
    Support Numbers and Symbols
    Key Is Case Sensetive
    '''

    class Tools:
        @staticmethod
        def generateKey(string, key):
            key = list(key) 
            if len(string) == len(key): 
                return(key) 
            else: 
                for i in range(len(string)-len(key)): 
                    key.append(key[i % len(key)]) 
            return("".join(key)) 

        @staticmethod
        def new_ALL_CHARS(ch, alphabet):
            new_ALL_CHARS = alphabet[alphabet.index(ch):] + alphabet[:alphabet.index(ch)]
            return new_ALL_CHARS

    
    @staticmethod
    def encrypt(text, key, alphabet=ALL_CHARS):
        res = ''
        i = 1
        key= Vigenere.Tools.generateKey(text,key)
        for char in key:
            new = Vigenere.Tools.new_ALL_CHARS(char, alphabet)
            for t in text:
                if alphabet.count(t) == 1:
                    res += new[alphabet.index(t)]
                    text = text[i:]
                    break
                else:
                    res += t
                    text = text[i:]
                    break
                i += 1    
        return res


    @staticmethod
    def decrypt(text, key, alphabet=ALL_CHARS):
        res = ''
        i = 1
        key= Vigenere.Tools.generateKey(text,key)
        for char in key:
            new = Vigenere.Tools.new_ALL_CHARS(char,alphabet)
            for t in text:
                if alphabet.count(t) == 1:
                    res += alphabet[new.index(t)]
                    text = text[i:]
                    break
                else:
                    res += t
                    text = text[i:]
                    break
                i += 1    
        return res

def XOR(word, key):
    for i in range(len(word)): 
        word = (word[:i] + chr(ord(word[i]) ^ ord(key)) + word[i + 1:])
    return word
class Xor(_Cipher):
    @staticmethod
    def encrypt(word, key):
        return XOR(word, key)
    @staticmethod
    def decrypt(word, key):
        return XOR(word, key)

ZigZag = RailFence
