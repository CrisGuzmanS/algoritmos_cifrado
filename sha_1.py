# ===============
# HASH OPERATIONS
# ===============

import hashlib

class SHA_1:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message)
        return hashlib.sha1( message ).hexdigest()


# message = b""
# sha_1 = SHA_1()
# print( sha_1.hash(message) )