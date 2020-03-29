# ===============
# HASH OPERATIONS
# ===============

from Crypto.Hash import SHA256
from timeit import default_timer as timer

class SHA_2:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        h = SHA256.new()
        start_time = timer()
        h.update(message)
        self.executionTime = timer() - start_time
        return h.hexdigest().upper()


# message = b""
# sha_2 = SHA_2()
# print( sha_2.hash(message) )