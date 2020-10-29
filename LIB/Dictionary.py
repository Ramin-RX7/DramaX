letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = letters_lowercase + letters_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
space = ' '
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def dict_creator_generator(SS,LENGTH):
    
    for current in range(LENGTH):
        a = [i for i in SS]
        for _ in range(current):
            a = [x+i for i in SS for x in a] # if x!=i
        for item in a:
            yield item

def dict_creator(SS,LENGTH):
    return list(dict_creator_generator(SS,LENGTH))



