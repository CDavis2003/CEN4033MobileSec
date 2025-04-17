import hashlib
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def hash_with_salt(data):
    salt = os.urandom(16)
    return hashlib.sha256(salt + data.encode()).hexdigest()

def generate_rsa_keypair():
    key = rsa.generate_private_key( 
        public_exponent=65537,
        key_size=2048
        )
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    return public_key, private_key
