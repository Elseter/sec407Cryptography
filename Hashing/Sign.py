import rsa
with open('samplePDF.pdf', 'rb') as file:
    message = file.read()

with open('private_key.pem', 'rb') as file:
    privkey = rsa.PrivateKey.load_pkcs1(file.read())

signature = rsa.sign(message, privkey, 'SHA-1')

print("Digest Size:")
print(len(signature))

with open('signature.sig', 'wb') as file:
    file.write(signature)

print("Signature created and saved")