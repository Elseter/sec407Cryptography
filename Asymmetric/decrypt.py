import rsa
from cryptography.fernet import Fernet

with open('private_key_file.pem', 'rb') as file:
    privkey = rsa.PrivateKey.load_pkcs1(file.read())

with open('encryptTest.txt.encrypted', 'rb') as file:
    encrypted_key = file.read(128)
    eData = file.read()

decrypted_key = rsa.decrypt(encrypted_key, privkey)
cipher = Fernet(decrypted_key)
decrypted_data = cipher.decrypt(eData)

with open('encryptTest.txt.decrypted', 'wb') as file:
    file.write(decrypted_data)

print("Decryption complete")
