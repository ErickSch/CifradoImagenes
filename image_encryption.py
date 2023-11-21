import os
import codecs
import binascii
from cryptography.fernet import Fernet

# Github para la conversión de la imagen a binario
    # https://github.com/henriland/image-to-binary/tree/master

key = Fernet.generate_key()
    
# Instance the Fernet class with the key 
fernet = Fernet(key)


# Binario a imagen
def binary_to_image(filename):

    # Lee el archivo de la imagen cidrada
    binFile = open(filename,'rb')
    binaryData = binFile.read()

    # Desencripta la imagen encriptda
    binaryData = fernet.decrypt(binaryData).decode()

    # Traduce el bianrio a imagen
    hexData = '%0*X' % ((len(binaryData) + 3) // 4, int(binaryData, 2))
    decode_hex = codecs.getdecoder("hex_codec")
    hexData = decode_hex(hexData)[0]
    parsed_filename = os.path.splitext(os.path.basename(filename))[0]
    png_filename = parsed_filename + '_from_binary.png'

    # Crea el archivo de la imagen
    with open(png_filename, 'wb') as file:
        file.write(hexData)


# Imagen a binario
def image_to_binary(filename):

    # Lee el archivo de la imagen en formato de binario
    with open(filename, 'rb') as file:
        image_data = file.read()

    # Traduce la imagen a binario
    data = binascii.hexlify(image_data)
    binary = bin(int(data, 16))
    binary = binary[2:].zfill(32)

    # Encripta el código binario de la imagen
    encMessage = fernet.encrypt(binary.encode())
    binary = encMessage

    # Guarda la imagen encriptada en el archivo nombreImagen.bin
    parsed_filename = os.path.splitext(os.path.basename(filename))[0]
    binary_filename = parsed_filename + '.bin'
    with open(binary_filename, 'wb') as file:
        file.write(binary)


# filename_cifrado = 'perro.bin'
# filename_imagen = 'perro.jpeg'

filename_imagen = input("Ingresa el nombre de la imagen (Debe de estar en el mismo directorio): ")

# La imagen cifrada se encuentra en perro.bin
image_to_binary(filename_imagen)

filename_cifrado = filename_imagen.split(".")[0] + ".bin"

# La imagen descifrada se encuentra en perro.jpeg
binary_to_image(filename_cifrado)

