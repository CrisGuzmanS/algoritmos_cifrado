# ==================================
# ENCRYPTION / DECRYPTION OPERATIONS
# ==================================

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from timeit import default_timer as timer

class AES_EBC:

    def __init__(self):
        self.key = bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000000")


    def encrypt(self, message):
        message = bytes.fromhex(message)
        cipher = AES.new(self.key, AES.MODE_ECB)
        start_time = timer()
        message = cipher.encrypt( pad(message, 16) )
        self.executionTime = timer() - start_time
        return message.hex()

    def decrypt(self, message):
        message = bytes.fromhex(message)
        dec = AES.new(self.key, AES.MODE_ECB)
        start_time = timer()
        d=dec.decrypt(message)
        self.executionTime = timer() - start_time
        return d.hex()

# key = "0000000000000000000000000000000000000000000000000000000000000000"
# message = "014730f80ac625fe84f026c60bfd547d"

# aes_ebc = AES_EBC( key )
# print( aes_ebc.encrypt( message ) )
