import os
import codecs
import binascii
from cryptography.fernet import Fernet

filename = 'perro.bin'

def binary_to_image():

    binFile = open(filename,'rb')
    binaryData = binFile.read()
    hexData = '%0*X' % ((len(binaryData) + 3) // 4, int(binaryData, 2))

    decode_hex = codecs.getdecoder("hex_codec")
    hexData = decode_hex(hexData)[0]

    parsed_filename = os.path.splitext(os.path.basename(filename))[0]
    png_filename = parsed_filename + '_from_binary.png'
    with open(png_filename, 'wb') as file:
        file.write(hexData)



def image_to_binary():
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