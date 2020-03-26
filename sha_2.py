# ===============
# HASH OPERATIONS
# ===============

import hashlib

class SHA_2:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message)
        return hashlib.sha256( message ).hexdigest()


# message = b""
# sha_2 = SHA_2()
# print( sha_2.hash(message) )