import hashlib,rx7,sys,os

# Names of files
words_file_name = ".txt" if not sys.argv[1] else sys.argv[1] #input file name
hashed_words_file_name = "" if not sys.argv[2] else sys.argv[2] #output file name

md5,sha1,sha224,sha256,sha384,sha512,sha3_224,sha3_256,sha3_384,sha3_512=[],[],[],[],[],[],[],[],[],[]
def create_hash_md5_text_file(input_list, output_file_name):
    input_list = list(map(str.strip, input_list)) # strips away the \n

    # loop through the words in the input list
    for word in input_list:
        word=bytes(word, encoding='utf-8')
        md5.append(hashlib.md5(word).hexdigest())
        sha1.append(hashlib.sha1(word).hexdigest())
        sha224.append(hashlib.sha224(word).hexdigest())
        sha256.append(hashlib.sha256(word).hexdigest())
        sha384.append(hashlib.sha384(word).hexdigest())
        sha512.append(hashlib.sha512(word).hexdigest())
        sha3_224.append(hashlib.sha3_224(word).hexdigest())
        sha3_256.append(hashlib.sha3_256(word).hexdigest())
        sha3_384.append(hashlib.sha3_384(word).hexdigest())
        sha3_512.append(hashlib.sha3_512(word).hexdigest())
    if not sys.argv[1]:
        print("Creating hash text file: {} ...".format(output_file_name))

    pre= './' if not sys.argv[3] else sys.argv[3]
	# Creating the output file
    try:
        rx7.write( pre + output_file_name + '_md5.txt'     , '\n'.join(md5)  )
    except FileNotFoundError:
        os.mkdir(pre) 
        rx7.write( pre + output_file_name + '_md5.txt' , '\n'.join(md5)      )

    rx7.write( pre + output_file_name + '_sha1.txt'    , '\n'.join(sha1)     )
    rx7.write( pre + output_file_name + '_sha224.txt'  , '\n'.join(sha224)   )
    rx7.write( pre + output_file_name + '_sha256.txt'  , '\n'.join(sha256)   )
    rx7.write( pre + output_file_name + '_sha384.txt'  , '\n'.join(sha384)   )
    rx7.write( pre + output_file_name + '_sha512.txt'  , '\n'.join(sha512)   )
    rx7.write( pre + output_file_name + '_sha3-224.txt', '\n'.join(sha3_224) )
    rx7.write( pre + output_file_name + '_sha3-256.txt', '\n'.join(sha3_256) )
    rx7.write( pre + output_file_name + '_sha3-384.txt', '\n'.join(sha3_384) )
    rx7.write( pre + output_file_name + '_sha3-512.txt', '\n'.join(sha3_512) )
    if not sys.argv[1]:
        print("{} has been successfully created".format(output_file_name))


def get_list_of_words_from_file(filename):
	# OPENING FILE
    if not sys.argv[1]:
        print("Opening file: {}".format(filename))
    list_of_words = open(filename, 'r', errors='ignore').readlines()
    if not sys.argv[1]:
        print("Striping breakline characters from the file: {}.".format(filename))
    list_of_words = list(map(str.strip, list_of_words))
    return (list_of_words)

# get words from file
words_list = get_list_of_words_from_file(words_file_name)
# create the hash
create_hash_md5_text_file(words_list, hashed_words_file_name)


