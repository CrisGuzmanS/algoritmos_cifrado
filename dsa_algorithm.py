from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from timeit import default_timer as timer

class DSA_ALGORITHM:

    def sign(self, message):
        # Create a new DSA key
        key = DSA.generate(1024)
        # Sign a message
        message = bytes( message.encode() )
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        start_time = timer()
        signature = signer.sign(hash_obj)
        self.executionTime = timer() - start_time
        return signature.hex().upper()



message = "Hello"
dsa = DSA_ALGORITHM()
print( dsa.sign(message) )