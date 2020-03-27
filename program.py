
from Reader import Reader
from Operation import Operation
from HashingWriter import HashingWriter

from aes_cbc import AES_CBC
from aes_ebc import AES_EBC
from rsa_oaep import RSA_OAEP
from rsa_pss import RSA_PSS

from sha_1 import SHA_1
from sha_2 import SHA_2
from sha_3 import SHA_3

from aes_cbc import AES_CBC
from aes_ebc import AES_EBC

operation = Operation()
operation.read()

reader = Reader('input.txt')
reader.read()

if( operation.isHashing() ):

    hashingWriter = HashingWriter()

    sha_1 = SHA_1()
    sha_2 = SHA_2()
    sha_3 = SHA_3()

    for vector in reader.getVectors():
        sha_1.hash( vector )
        sha_2.hash( vector )
        sha_3.hash( vector )
        hashingWriter.write( [vector, sha_1.executionTime, sha_2.executionTime, sha_3.executionTime] )

if( operation.isEncryption() ):
        aes_ebc = AES_EBC()
        aes_cbc = AES_CBC()
        rsa_oaep = RSA_OAEP()

if( operation.isDecryption() ):
        # AES_EBC
        # AES_CBC
        # RSA_OAEP
        pass

if( operation.isVerifying() ):
        # RSA PSS
        # DSA
        # ECDSA
        pass

if( operation.isSigning() ):
        rsa_pss = RSA_PSS()
        # DSA
        # ECDSA
        pass