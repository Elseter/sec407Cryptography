from cryptography.fernet import Fernet

with open("mykey.key", "rb") as key_file:
    key = key_file.read()

print("Key:\n", key)

cipher = Fernet(key)

encrypted_text = cipher.encrypt(b'this is my secret') # encrypt the string

print("\nEncrypted text:\n", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text) # decrypt the string

print("\nDecrypted text:\n", decrypted_text.decode())