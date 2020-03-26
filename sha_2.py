# ===============
# HASH OPERATIONS
# ===============

import hashlib
from timeit import default_timer as timer

class SHA_2:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = timer()
        hashed = hashlib.sha256( message )
        self.executionTime = timer() - start_time
        return hashed.hexdigest().upper()


# message = b""
# sha_2 = SHA_2()
# print( sha_2.hash(message) )