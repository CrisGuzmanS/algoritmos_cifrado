from Crypto.Hash import SHA512
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from timeit import default_timer as timer

class ECDSA:

    def sign(self, message):
        message = bytes(message.encode())
        key = ECC.generate(curve='P-521')
        h = SHA512.new(message)
        signer = DSS.new(key, 'fips-186-3')
        start_time = timer()
        signature = signer.sign(h)
        self.executionTime = timer() - start_time
        return signature

message = 'I give my permission to order #4355'

ecdsa = ECDSA()
ecdsa.sign(message)