import base64

s1 = base64.encodestring('aVBpjfY9rp5gO-pmH2qD0QVryMoThN_Qkp8RiM_x')
s2 = base64.decodestring(s1)
print s1, s2

# from Crypto.Cipher import AES

# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message = "The answer is no"
# ciphertext = obj.encrypt(message)
# print ciphertext
# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# print obj2.decrypt(ciphertext)
