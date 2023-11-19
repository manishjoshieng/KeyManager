import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encryptor:
    def __init__(self, key:str) -> None:
        self._ecryptor = Fernet(self.getKey(key.encode()))

    def getKey(self,password):
        salt = password[:16]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt(self,msg:str):
        msg = msg.encode()
        try:
            output = self._ecryptor.encrypt(msg)
        except Exception as e:
            print(f"Error while decription: {e}")
        else:
            return output
        return ""
    
    def decrypt(self,msg):
        try:
            output =  self._ecryptor.decrypt(msg).decode()
        except Exception as e:
            print(f"Error while decription: {e}")
        else:
            return output
        return ""
    
    @staticmethod
    def hashCode(key: str):
        # Encode the key as bytes before hashing
        return hashlib.sha256(key.encode()).hexdigest()