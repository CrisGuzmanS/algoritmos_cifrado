# ===============
# HASH OPERATIONS
# ===============

import hashlib

class SHA_3:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message)
        return hashlib.sha3_256( message ).hexdigest()


message = b"abc"
sha_3 = SHA_3()
print( sha_3.hash(message) )