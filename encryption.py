# encryption.py
from cryptography.fernet import Fernet

def load_key():
    """Load the encryption key from the secret.key file."""
    return open('secret.key', 'rb').read()

def encrypt_password(password: str) -> bytes:
    """Encrypts a password using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    """Decrypts an encrypted password using the loaded key."""
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password).decode()
