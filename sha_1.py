# ===============
# HASH OPERATIONS
# ===============

import hashlib
from Reader import Reader
import datetime


class SHA_1:

    def __init__(self):
        pass

    def hash(self, message):
        message = bytes(message.encode())
        start_time = datetime.datetime.now()
        hashed = hashlib.sha1( message )
        self.executionTime = datetime.datetime.now() - start_time
        self.executionTime = self.executionTime.microseconds
        return hashed.hexdigest().upper()


