# ===============
# HASH OPERATIONS
# ===============

import hashlib

message = b""

result = hashlib.sha1( message )
print(result.hexdigest())