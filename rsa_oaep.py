import binascii
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from timeit import default_timer as timer

class RSA_OAEP:
    
    def __init__(self):
        self.key = RSA.generate(1024)
        self.pubkey = self.key.publickey()
        # self.publicKey = self.key.publickey()

    def encrypt(self, message):
        message = bytes.fromhex(message)


        cipher = PKCS1_OAEP.new(self.pubkey)
        start_time = timer()
        ciphertext = cipher.encrypt(message)
        self.executionTime = timer() - start_time
        return ciphertext.hex().upper()

    
    def decrypt(self, message):
        message = binascii.unhexlify( self.encrypt( (message)) )
        cipher = PKCS1_OAEP.new(self.key)
        start_time = timer()
        msg = cipher.decrypt(message)
        self.executionTime = timer() - start_time
        return msg.hex().upper()
        
rsa_oaep = RSA_OAEP()
print( rsa_oaep.encrypt('293847fa') )
print( rsa_oaep.decrypt('293847fa') )
# print( rsa_oaep.publicKey )