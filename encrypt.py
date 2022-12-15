# Import the necessary modules
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Generate a password
class pManager:
    pass_ = 'hi'
    password = bytes(pass_, 'utf-8')

    # Generate a key using the password
    salt = b'MySalt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # Use the key to encrypt the data
    f = Fernet(key)
    encrypted_data = f.encrypt(password)

    # Use the key to decrypt the data
    decrypted_data = f.decrypt(encrypted_data)
    print(decrypted_data)