# In this program we will be creating a basic
# ecryption and decryption using two lib

import random
import string

chars = " " + string.punctuation + string.digits + string.digits + string.ascii_letters
str1 = list(chars)
key = str1.copy()
random.shuffle(key)

#Encrypt 

to_encrypt = input("Enter what you want to encrypt: ")
encr =  ""
for letter in to_encrypt:
    index = chars.index(letter)
    encr += key[index]

print(f"The encrypted message is : {encr}")


#Decrypt 

to_decrypt = input("Enter what you want to decrypt: ")
# for num in to_decrypt:
#     if to_decrypt.isnumeric:
#         to_decrypt = str(to_decrypt)
#     else:
#         pass          #This is the mistake i did, because in the beginning i didn't convert the char to string  

print(to_decrypt)

decr =  ""


for letter in to_decrypt:
    index = key.index(letter)
    decr += chars[index]


print(f"The decrypted message is : {decr}")
