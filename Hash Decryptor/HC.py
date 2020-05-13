import hashlib,sys

# Names of files
#print(sys.argv)
words_file_name = "english_more.txt" if not sys.argv[1] else sys.argv[1] #input file name
hashed_words_file_name = "english_sha3-512.txt" if not sys.argv[2] else sys.argv[2]  #output file name

sa={'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha224':hashlib.sha224,'sha256':hashlib.sha256,
	'sha384':hashlib.sha384,'sha512':hashlib.sha512,'sha3_224':hashlib.sha3_224,
	'sha3_256':hashlib.sha3_256, 'sha3_384':hashlib.sha3_384,'sha3_512':hashlib.sha3_512}

cr= hashlib.sha3_512 if not sa[sys.argv[3]] else sa[sys.argv[3]]

def create_hash_md5_text_file(input_list, output_file_name):
	input_list = list(map(str.strip, input_list)) # strips away the \n
	hashesToExport = []

	# loop through the words in the input list
	for word in input_list:
		crypt = cr()
		crypt.update(bytes(word, encoding='utf-8'))
		hashOfWord = crypt.hexdigest()
		hashesToExport.append(hashOfWord)
	if not sys.argv[1]:
		print("Creating hash text file: {} ...".format(output_file_name))

	# Creating the output file
	with open(output_file_name, 'w') as f:
	    for hashOfWord in hashesToExport:
	        f.write("%s\n" % hashOfWord)
		

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


