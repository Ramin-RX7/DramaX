import Cipher

cipher = Cipher.Autokey
key = 'rxishsadf'
enc = cipher.encrypt('ramin',key, 'abcdefghijklmnopqrstuvwxyz')
print(enc)
print(cipher.decrypt(enc,key,'abcdefghijklmnopqrstuvwxyz'))


