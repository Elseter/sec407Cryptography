import rsa
with open('samplePDF.pdf', 'rb') as file:
    message = file.read()

with open('public_key.pem', 'rb') as file:
    pubkey = rsa.PublicKey.load_pkcs1(file.read())

with open('signature.sig', 'rb') as file:
    signature = file.read()

verified = rsa.verify(message, signature, pubkey)

print("Signature verified: " + str(verified))