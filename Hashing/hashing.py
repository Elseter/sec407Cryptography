import rsa

message = b'this is our text to hash'

htext = rsa.compute_hash(message, 'SHA-512')

print("Digest:")
print(htext.hex())
print()

message = b'This is our text to hash'

htext = rsa.compute_hash(message, 'SHA-512')

print("Digest:")
print(htext.hex())
print()