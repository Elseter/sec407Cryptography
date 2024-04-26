from cryptography.fernet import Fernet
import rsa

key = Fernet.generate_key()
cipher = Fernet(key)

with open('public_key_file.pem', 'rb') as file:
    pubkey = rsa.PublicKey.load_pkcs1(file.read())
    encrypted_key = rsa.encrypt(key, pubkey)

with open('encryptTest.txt', 'rb') as file:
    edata = cipher.encrypt(file.read())

with open('encryptTest.txt.encrypted', 'wb') as file:
    file.write(encrypted_key)
    file.write(edata)

print("Encryption complete")