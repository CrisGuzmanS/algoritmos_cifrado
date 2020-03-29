from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from timeit import default_timer as timer



class RSA_PSS:

    def __init__(self):
        pass

    def sign(self, message):
        message = bytes.fromhex(message)
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        h = SHA256.new(message)
        rsa_pss = pss.new(key)
        start_time = timer()
        signature = rsa_pss.sign(h)
        self.executionTime = timer() - start_time
        return signature.hex().upper()

    def verify(self):
        pass

message = "04df2328374635f9f023"

rsa_pss = RSA_PSS()