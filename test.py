from timeit import default_timer as timer
import hashlib
import time

start = timer()
time.sleep(2)
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282