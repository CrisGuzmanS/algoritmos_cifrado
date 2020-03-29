from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from timeit import default_timer as timer

class RSA_OAEP:
    key = RSA.generate(1024, random_generator)
    random_generator = Random.new().read

    def __init__(self):
        pass

    def encrypt(self, message, key):

        message = bytes.fromhex(message)


        cipher = PKCS1_OAEP.new(key)
        start_time = timer()
        ciphertext = cipher.encrypt(message)
        self.executionTime = timer() - start_time
        return ciphertext.hex().upper()

    
    def decrypt(self, msg_encrypted, key):
        dec = PKCS1_OAEP.new(key)
        start_time = timer()
        msg = cipher.decrypt(ciphertext)
        self.executionTime = timer() - start_time
        return msg.hex().upper()
        
        
        
        


message = '19875AB493FD83475D'
rsa_oaep = RSA_OAEP()
msg_encrypted = rsa_oaep.encrypt( message, key)
rsa_oaep.decrypt(msg_encrypted)
