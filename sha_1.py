# ===============
# HASH OPERATIONS
# ===============

import hashlib
from Reader import Reader
from timeit import default_timer as timer


class SHA_1:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = timer()
        hashed = hashlib.sha1( message )
        self.executionTime = timer() - start_time
        return hashed.hexdigest().upper()


