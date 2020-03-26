from timeit import default_timer as timer
import hashlib

start = timer()
hashed = hashlib.sha1( "abc".encode() )
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282