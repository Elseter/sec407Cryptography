from cryptography.fernet import Fernet

with open("mykey.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

with open("TestFile.txt.encrypted", "rb") as file:
    encrypted = file.read()

decrypted = cipher.decrypt(encrypted)

with open("TestFile.txt.decrypted", "wb") as file:
    file.write(decrypted)

