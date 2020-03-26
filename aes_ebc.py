from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AES_EBC:

    def __init__(self, key):
        self.key = bytes.fromhex(key)


    def encrypt(self, message):
        message = bytes.fromhex(message)
        cipher = AES.new(self.key, AES.MODE_ECB)
        message = cipher.encrypt( pad(message, 16) )
        return message.hex()


key = "0000000000000000000000000000000000000000000000000000000000000000"
message = "014730f80ac625fe84f026c60bfd547d"

aes_ebc = AES_EBC( key )
print( aes_ebc.encrypt( message ) )