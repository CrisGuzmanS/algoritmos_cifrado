# ===============
# HASH OPERATIONS
# ===============

import hashlib
import datetime

class SHA_2:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = datetime.datetime.now()
        hashed = hashlib.sha256( message )
        self.executionTime = datetime.datetime.now() - start_time
        self.executionTime = self.executionTime.microseconds
        return hashed.hexdigest().upper()


# message = b""
# sha_2 = SHA_2()
# print( sha_2.hash(message) )