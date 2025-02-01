from cryptography.fernet import Fernet
import os

# Generate a key and save it if it doesn’t exist
KEY_FILE = "secret.key"

def generate_key():
    """Generates and saves an encryption key if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    """Loads the encryption key from file."""
    with open(KEY_FILE, "rb") as f:
        return f.read()

# Ensure the key is available
generate_key()
fernet = Fernet(load_key())

def encrypt(text: str) -> str:
    """Encrypts a string and returns the encrypted value as a string."""
    return fernet.encrypt(text.encode()).decode()

def decrypt(encrypted_text: str) -> str:
    """Decrypts an encrypted string."""
    return fernet.decrypt(encrypted_text.encode()).decode()
