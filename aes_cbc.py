# ==================================
# ENCRYPTION / DECRYPTION OPERATIONS
# ==================================

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
from timeit import default_timer as timer


class AES_CBC:

    def __init__(self):
        self.key = hashlib.sha256("0000000000000000000000000000000000000000000000000000000000000000".encode()).digest()
        self.iv = Random.new().read(AES.block_size)

    def encrypt(self, message):
        message = bytes.fromhex(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        start_time = timer()
        ciphered = cipher.encrypt(pad(message, AES.block_size))
        self.executionTime = timer() - start_time
        return ciphered.hex().upper()


# message = "014730f80ac625fe84f026c60bfd547d"

# aes_cbc = AES_CBC()
# print( aes_cbc.encrypt( message ) )