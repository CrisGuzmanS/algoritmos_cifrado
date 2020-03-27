from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from timeit import default_timer as timer

class RSA_OAEP:

    def __init__(self):
        pass

    def encrypt(self, message):

        message = bytes.fromhex(message)

        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        cipher = PKCS1_OAEP.new(key)
        start_time = timer()
        ciphertext = cipher.encrypt(message)
        self.executionTime = timer() - start_time
        return ciphertext.hex().upper()
    
    def decrypt(self):
        pass


message = '19875AB493FD83475D'
rsa_oaep = RSA_OAEP()
rsa_oaep.encrypt( message )