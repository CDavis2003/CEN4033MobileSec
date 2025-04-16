import hashlib
import os
from Crypto.PublicKey import RSA

def hash_with_salt(data):
    salt = os.urandom(16)
    return hashlib.sha256(salt + data.encode()).hexdigest()

def generate_rsa_keypair():
    key = RSA.generate(2048)
    return key.publickey().export_key().decode(), key.export_key().decode()
