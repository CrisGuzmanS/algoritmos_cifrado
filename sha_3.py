# ===============
# HASH OPERATIONS
# ===============

from Crypto.Hash import SHA3_512
from timeit import default_timer as timer

class SHA_3:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        h_obj = SHA3_512.new()
        start_time = timer()
        h_obj.update(message)
        self.executionTime = timer() - start_time
        return h_obj.hexdigest().upper()


# message = b""
# sha_3 = SHA_3()
# print( sha_3.hash(message) )