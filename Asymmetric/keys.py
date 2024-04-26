import rsa

pubkey, privkey = rsa.newkeys(1024)


def load_keys(filename):
    with open(filename, "wb") as file:
        if filename == 'public_key_file.pem':
            file.write(pubkey.save_pkcs1('PEM'))
        elif filename == 'private_key_file.pem':
            file.write(privkey.save_pkcs1('PEM'))


load_keys('public_key_file.pem')
load_keys('private_key_file.pem')
