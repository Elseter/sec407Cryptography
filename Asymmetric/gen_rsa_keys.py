import rsa

pubkey, privkey = rsa.newkeys(512)

print(privkey.save_pkcs1('PEM').decode())
print(pubkey.save_pkcs1('PEM').decode())

e_data = rsa.encrypt(b'this is my secret message', pubkey)

print("\nEncrypted text:\n", e_data)

d_data = rsa.decrypt(e_data, privkey)

print("\nDecrypted text:\n", d_data.decode())
