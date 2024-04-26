from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Key:\n{key}")

cipher = Fernet(key)

# Basic literals are utilized for representing binary data like encoded text, pictures
#  audio or any other type of data
# that may not directly correspond to any characters

encrypted_text = cipher.encrypt(b'this is my secret') # encrypt the string
print(f"\nEncrypted text:\n{encrypted_text}")

decrypted_text = cipher.decrypt(encrypted_text) # decrypt the string

print(f"\nDecrypted text:\n{decrypted_text.decode()}")

# save the key to a file called mykey.key
with open("mykey.key", "wb") as key_file:
    key_file.write(key)

