from cryptography.fernet import Fernet

with open("mykey.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

with open("TestFile.txt", "rb") as file:
    original = file.read()

edata = cipher.encrypt(original)

with open("TestFile.txt.encrypted", "wb") as file:
    file.write(edata)

