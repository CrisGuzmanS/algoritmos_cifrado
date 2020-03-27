# ==================================
# ENCRYPTION / DECRYPTION OPERATIONS
# ==================================

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from timeit import default_timer as timer


class AES_CBC:

    def __init__(self):
        self.key = bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000000")
        self.iv = bytes.fromhex("00000000000000000000000000000000")
        self.block_size = 16
        AES.block_size = 16

    def encrypt(self, message):
        message = bytes.fromhex(message)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        start_time = timer()
        ciphered = cipher.encrypt(pad(message, self.block_size))
        self.executionTime = timer() - start_time
        return ciphered.hex().upper()


# message = "014730f80ac625fe84f026c60bfd547d"

# aes_cbc = AES_CBC()
# print( aes_cbc.encrypt( message ) )