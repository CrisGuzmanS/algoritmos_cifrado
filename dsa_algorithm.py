from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from timeit import default_timer as timer

class DSA_ALGORITHM:

    def sign(self, message):
        # Create a new DSA key
        key = DSA.generate(1024)
        # Sign a message
        message = bytes( message.encode() )
        hash_obj = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        start_time = timer()
        signature = signer.sign(hash_obj)
        self.executionTime = timer() - start_time
        return signature.hex().upper()
    
    def verify(self,message):
        key = DSA.generate(1024)    #Se genera un par de llaves.
        h = SHA256.new(message) #Se obtiene la transformada hash del mensaje.
        signer = DSS.new(key,'fips-186-3')  #Se obtiene una firma según el estandar definido en fips 186-3.
        signature = signer.sign(h)  #Se crea hace la firma.
        pubKey = key.publickey()    #Se obtiene la llave pública del par generado.
        start_time = timer()  #Se inicia la toma de tiempo.
        verifier = DSS.new(pubKey,'fips-186-3') #Se hace un objeto que permite hacer la validación de la firma.
        try:
            verifier.verify(h,signature)    #Se hace la validación de la firma.
            print("La firma se pudo validar, es correcta.")
            self.executionTime = timer() - start_time   #Fin de la toma de  tiempo.
            return 1
        except(ValueError):
            print("La firma no se pudo validar, no es correcta.")
            self.executionTime = timer() - start_time   #Fin de la toma de tiempo.
            return 0


message = "Hello"
dsa = DSA_ALGORITHM()
