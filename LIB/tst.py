import Cipher

cipher = Cipher.SimpleSubstitution
key = 'qwertyuioplkjhgfdsazxcvb'
enc = cipher.encrypt('ramin',key,Cipher.LOWERS)
print(enc)
print(cipher.decrypt(enc,key,Cipher.LOWERS))


