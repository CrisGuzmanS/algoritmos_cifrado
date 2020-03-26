# ===============
# HASH OPERATIONS
# ===============

import hashlib
from timeit import default_timer as timer

class SHA_3:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = timer()
        hashed = hashlib.sha3_256( message )
        self.executionTime = timer() - start_time
        return hashed.hexdigest().upper()


# message = b""
# sha_3 = SHA_3()
# print( sha_3.hash(message) )