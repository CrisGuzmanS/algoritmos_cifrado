from aes_cbc import AES_CBC
from aes_ebc import AES_EBC

from sha_1 import SHA_1
from sha_2 import SHA_2
from sha_3 import SHA_3

message = b"GeeksforGeeks"

sha_1 = SHA_1()
sha_2 = SHA_2()
sha_3 = SHA_3()

print( sha_1.hash( message ) )
print( sha_2.hash( message ) )
print( sha_3.hash( message ) )