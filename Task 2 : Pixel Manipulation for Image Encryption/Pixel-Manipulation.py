import os
from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    random.seed(key)

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r, b = b, r 
            r = (r + random.randint(0, 255)) % 256
            g = (g + random.randint(0, 255)) % 256
            b = (b + random.randint(0, 255)) % 256
            pixels[x, y] = (r, g, b)

    img.save(output_path)

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    random.seed(key)

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r, b = b, r  
            r = (r - random.randint(0, 255)) % 256
            g = (g - random.randint(0, 255)) % 256
            b = (b - random.randint(0, 255)) % 256
            pixels[x, y] = (r, g, b)

    img.save(output_path)
    
output_dir_encrypted = "/home/mr-srj/Desktop/Prodigy Info Tech Internship/encrypted"
output_dir_decrypted = "/home/mr-srj/Desktop/Prodigy Info Tech Internship/decrypted"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

while True:
    print("Options:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_dir = input("Enter the input directory path: ")
        filename = input("Enter the filename of the image to encrypt: ")
        key = int(input("Enter the encryption key: "))
        create_directory(output_dir_encrypted)
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir_encrypted, filename)
        if os.path.exists(input_path):
            encrypt_image(input_path, output_path, key)
            print("Encryption completed!")
            print("The encrypted image is located at", output_dir_encrypted)
        else:
            print("File not found in the input directory.")

    elif choice == 2:
        key = int(input("Enter the decryption key: "))
        create_directory(output_dir_decrypted)
        filename = input("Enter the filename of the image to decrypt: ")
        input_path = os.path.join(output_dir_encrypted, filename)
        output_path = os.path.join(output_dir_decrypted, filename)
        if os.path.exists(input_path):
            decrypt_image(input_path, output_path, key)
            print("Decryption completed!")
            print("The decrypted image is Located at", output_dir_decrypted)
        else:
            print("File not found in the encrypted directory.")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice!")
