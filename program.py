
from Reader import Reader

from HashingWriter import HashingWriter

from aes_cbc import AES_CBC
from aes_ebc import AES_EBC

from sha_1 import SHA_1
from sha_2 import SHA_2
from sha_3 import SHA_3

reader = Reader('input.txt')
reader.read()

if( True ):

    hashingWriter = HashingWriter()

    sha_1 = SHA_1()
    sha_2 = SHA_2()
    sha_3 = SHA_3()

    for vector in reader.getVectors():
        print( sha_1.hash( vector ) )
        print( sha_2.hash( vector ) )
        print( sha_3.hash( vector ) )
        hashingWriter.write( [vector, sha_1.executionTime, sha_2.executionTime, sha_3.executionTime] )