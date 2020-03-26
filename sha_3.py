# ===============
# HASH OPERATIONS
# ===============

import hashlib
import datetime

class SHA_3:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = datetime.datetime.now()
        hashed = hashlib.sha3_256( message )
        self.executionTime = datetime.datetime.now() - start_time
        self.executionTime = self.executionTime.microseconds
        return hashed.hexdigest().upper()


# message = b""
# sha_3 = SHA_3()
# print( sha_3.hash(message) )