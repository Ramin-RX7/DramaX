import hashlib
from rx7 import write
chars= __import__('string').ascii_lowercase*2
password= input('Type Word To Start Encryption:  ')
main_dic={}
for i in range(26):
    main_dic[f'case{i}']=''.join(list(chars[chars.index(char)+i] for char in password))
    print(main_dic[f'case{i}'])
print('\n')
cbfyn= input('Create Hash Bruteforce File? (Y/n)  ')
if cbfyn.lower()in('y','yes'):
    crypt_lst=[hashlib.md5,hashlib.sha1,hashlib.sha224,hashlib.sha256,hashlib.sha384,hashlib.sha512,
               hashlib.sha3_224,hashlib.sha3_256,hashlib.sha3_384,hashlib.sha3_512]    
    file_content=''
    oh= input('Create Hashes Only (Y/n):  ')
    if oh in ('y','yes'):
        for item in main_dic.values():
            item=bytes(item, encoding='utf-8')
            for crypt in crypt_lst:
                file_content+= f'{crypt(item).hexdigest()}\n'
        write(f'{password}.txt',file_content)
        title=''

    else:
        crypt_name= ['md5:       ','sha1:      ','sha224:    ','sha256:    ','sha384:    ','sha512:    ',
                    'sha3_224:  ','sha3_256:  ','sha3_384:  ','sha3_512:  ']
        for item in main_dic.values():
            file_content+=f'{item}\n'
            item=bytes(item, encoding='utf-8')
            for crypt in crypt_lst:
                file_content+= f'  {crypt_name[crypt_lst.index(crypt)]}{crypt(item).hexdigest()}\n'
            file_content+= '\n'
            title=f'Caesar Hash Bruteforce of {password}\n\n'
    write(f'{password}.txt',title+file_content)
#input('FINNISHED...')
