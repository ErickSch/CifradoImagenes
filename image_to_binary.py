import os
import binascii
from cryptography.fernet import Fernet

filename = 'perro.jpeg'
with open(filename, 'rb') as file:
    image_data = file.read()

data = binascii.hexlify(image_data)

binary = bin(int(data, 16))
binary = binary[2:].zfill(32)

key = Fernet.generate_key()
 
# Instance the Fernet class with the key
 
fernet = Fernet(key)
 
# then use the Fernet class instance 
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(binary.encode())

binary = encMessage
 


parsed_filename = os.path.splitext(os.path.basename(filename))[0]
binary_filename = parsed_filename + '.bin'
with open(binary_filename, 'wb') as file:
    # file.write(binary.encode())
    file.write(binary)