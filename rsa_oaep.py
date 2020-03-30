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
     def decrypt(self,message):
        message= bytes.fromhex(message)
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        cipher = PKCS1_OAEP.new(key)
        
        start_time = timer()
       
        decrypted= cipher.decrypt(message)
        self.executionTime = timer() - start_time
        return decrypted.hex()
        


