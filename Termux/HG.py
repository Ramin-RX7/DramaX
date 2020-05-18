import hashlib,sys,os

def print_hashes(word):
    print( 'MD5:       ' + hashlib.md5(word).hexdigest())
    print( 'SHA1:      ' + hashlib.sha1(word).hexdigest())
    print( 'SHA224:    ' + hashlib.sha224(word).hexdigest())
    print( 'SHA256:    ' + hashlib.sha256(word).hexdigest())
    print( 'SHA384:    ' + hashlib.sha384(word).hexdigest())
    print( 'SHA512:    ' + hashlib.sha512(word).hexdigest())
    print( 'SHA3-224:  ' + hashlib.sha3_224(word).hexdigest())
    print( 'SHA3-256:  ' + hashlib.sha3_256(word).hexdigest())
    print( 'SHA3-384:  ' + hashlib.sha3_384(word).hexdigest())
    print( 'SHA3-512:  ' + hashlib.sha3_512(word).hexdigest())    

if len(sys.argv)!=2:
    x=True
    while x:
        inp= input('Enter String to Create Hashes:  ')
        if inp=='99':
            x=False
        elif inp:
            inp=bytes(inp, encoding='utf-8')
            print_hashes(inp)
            os.system('pause')
            os.system('clear')
else:
    print_hashes(bytes(sys.argv[1], encoding='utf-8'))
    os.system('pause')
