# ===============
# HASH OPERATIONS
# ===============

from Crypto.Hash import SHA1
from Reader import Reader
from timeit import default_timer as timer


class SHA_1:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        h = SHA1.new()
        start_time = timer()
        h.update( message )
        self.executionTime = timer() - start_time
        return h.hexdigest().upper()


