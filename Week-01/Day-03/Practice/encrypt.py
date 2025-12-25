# Encryption and Decryption of a Message using Caesar Cipher
import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)
key = chars.copy() #shallow copy

random.shuffle(key) #shuffle the key for encryption

# user input                        
plain_txt = input("Enter the message to be encrypted: ")

# Encryption function
def encrypt(message):
    cipher_txt = ""
    for char in message:
        idx = chars.index(char)
        cipher_txt += key[idx] # Shift by key
    return cipher_txt

# Decryption function
def decrypt(message):
    decrypted_txt = ""
    for char in message:
        idx = key.index(char)
        decrypted_txt += chars[idx] # Shift back by chars
    return decrypted_txt

print(f"Original Message: {plain_txt}")

# User choice for encryption or decryption
print("What to do with the message?")
choice = input("1. Encrypt 2. Decrypt (Enter 1 or 2): ")
if choice == '1':
    encrypted_message = encrypt(plain_txt)
    print(f"Encrypted Message: {encrypted_message}")
elif choice == '2':
    decrypted_message = decrypt(plain_txt)
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Invalid choice. Please enter 1 or 2.")