from Crypto.Hash import SHA512
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from timeit import default_timer as timer

class ECDSA:

    def sign(self, message):
        message = bytes(message.encode())
        key = ECC.generate(curve='P-521')
        h = SHA512.new(message)
        signer = DSS.new(key, 'fips-186-3')
        start_time = timer()
        signature = signer.sign(h)
        self.executionTime = timer() - start_time
        return signature
    
    def verify(self,message):
    	key = ECC.generate(curve='P-521')	#Genera una nueva llave privada usando la curva definida por P-521
    	h = SHA512.new(message)		#Genera la función Hash del mensaje.
    	signer = DSS.new(key, 'fips-186-3')	#Crea un objeto signature para hacer la firma.
    	signature = signer.sign(h)	#Genera la firma del mensaje.
    	pubKey = key.public_key()	#Obtiene la llave pública del par generado almacenado en "key".
    	start_time = timer()	#Función que permite iniciar una toma de tiempo.
    	verifier = DSS.new(pubKey, 'fips-186-3')	#Crea un objeto signature para hacer la validación de la firma.
    	try:
    		verifier.verify(h,signature)	#Hace la comparación entre el hash del mensaje y la firma.
    		print("La firma se pudo validar, es correcta.")
    		self.executionTime = timer() - start_time	#Fin de la toma de tiempo.
    		return 1
    	except(ValueError):	#Accede en caso de que los valores no sean correctos, es decir, la firma no es válida.
    		print("La firma no se pudo validar, no es correcta")
    		self.executionTime = timer() - start_time	#Fin de la toma de tiempo.
    		return 0

message = 'I give my permission to order #4355'

ecdsa = ECDSA()
ecdsa.sign(message)
ecdsa.verify(message)
