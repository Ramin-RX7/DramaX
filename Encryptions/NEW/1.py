TEXT_PUB= list(input('Enter Public Text:  '))
TEXT_PV=  list(input('Enter Private Text:  '))

KEY_PUB= input('Enter Public Key:   ')
KEY_PV=  input('Enter Private Key:  ')


if len(TEXT_PUB)!=len(TEXT_PV):
    if len(TEXT_PUB)>len(TEXT_PV):
        while len(TEXT_PUB)!=len(TEXT_PV):
            TEXT_PV.append(' ')
    if len(TEXT_PV)>len(TEXT_PUB):
        while len(TEXT_PV)!=len(TEXT_PUB):
            TEXT_PUB.append(' ')

#print(TEXT_PUB)
#print(TEXT_PV)

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789</>!"@£$%^&*()-=_+?~,.'
def generateKey(string, key):
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def new_alph(ch):
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph

def encrypt(text, big_key):
    res = '';i = 1;big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :  res += new[alph.index(t)]; text = text[i:]; break
            elif alph.count(t) == 1: res += new[alph.index(t)]; text = text[i:]; break
            else: res += t; text = text[i:]; break
            i += 1    
    return res[::-1]

def decrypt(text, big_key):
    text= text[::-1]
    res = ''
    i = 1
    big_key= generateKey(text,big_key)
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t) == 1:
                res += alph[new.index(t)]
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res


TEXT_PUB= encrypt(TEXT_PUB,KEY_PUB)
TEXT_PV = encrypt(TEXT_PV ,KEY_PV )




lvl_1=''
for i in range(len(TEXT_PUB)):
    lvl_1+=TEXT_PUB[i]+TEXT_PV[i]


print('-'*50)


import rx7 as rx
LST= [''.join([x for x in lvl_1 if lvl_1.index(x)%2==0]),''.join([x for x in lvl_1 if lvl_1.index(x)%2==1])]
for cipher in LST:
    rx.style.print(decrypt(cipher,KEY_PUB),BG='dark_green')
for cipher in LST:
    rx.style.print(decrypt(cipher,KEY_PV),BG='dark_green')
