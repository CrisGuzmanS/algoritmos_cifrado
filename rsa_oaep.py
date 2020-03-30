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

     def decrypt(self,message):
        message= bytes.fromhex(message)
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(message)
        start_time = timer()
       
        decrypted= cipher.decrypt(ciphertext)
        self.executionTime = timer() - start_time
        return decrypted.hex()
        
        

# print( rsa_oaep.publicKey )
