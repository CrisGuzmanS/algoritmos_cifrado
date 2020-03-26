# ==================================
# ENCRYPTION / DECRYPTION OPERATIONS
# ==================================

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AES_CBC:

    def __init__(self, key, iv, block_size):
        self.key = bytes.fromhex(key)
        self.iv = bytes.fromhex(iv)
        self.block_size = block_size
        AES.block_size = self.block_size

    def encrypt(self, message):
        message = bytes.fromhex(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return (cipher.encrypt(pad(message, self.block_size))).hex()