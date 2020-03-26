from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import time
BLOCK_SIZE = 26 # Bytes

class FileWriter:

	def __init__(self, filename):

		self.file = open( filename, "w+" )

	def write(self, text):
		for i in range(10):
			self.file.write( "The text is: %s\r" %text )

	def close(self):
		self.file.close()

class AESECB:

	def __init__( self, key, message ):
		self.key = key.encode('utf8')
		self.message = bytes( message.encode() )
	
	def encrypt(self):
		start_time = time.time()
		cipher = AES.new(self.key, AES.MODE_ECB)
		self.message = cipher.encrypt( pad(self.message, 16) )
		self.executionTime = time.time() - start_time
		print("MESSAGE ENCRYPTED")
		print( self.message.hex() )
		print("=================")

	def decrypt(self):
		decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
		self.message = decipher.decrypt(self.message)
		print("MESSAGE DECRYPTED")
		print(unpad(self.message, 16))
		print("=================")

fileWriter = FileWriter('output.txt')
fileWriter.write('12.32')
fileWriter.close()

key = 'abcdefghijklmnop'
message = 'TechTutorialsX!!TechTutorialsX!!'

aesecb = AESECB( key, message )
aesecb.encrypt()

print("EXECUTION TIME")
print( aesecb.executionTime )
print("======================")

aesecb.decrypt()