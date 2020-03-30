from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from timeit import default_timer as timer



class RSA_PSS:

    def __init__(self):
        pass

    def sign(self, message):
        message = bytes.fromhex(message)
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        h = SHA256.new(message)
        rsa_pss = pss.new(key)
        start_time = timer()
        signature = rsa_pss.sign(h)
        self.executionTime = timer() - start_time
        return signature.hex().upper()

    def verify(self,message):
        message = bytes.fromhex(message)    #Convierte el mensaje a bytes.
        random_generator = Random.new().read    #Genera una secuencia aleatoria.
        key = RSA.generate(1024,random_generator)   #Se usa la secuencia para generar un par de llaves.
        h = SHA256.new(message) #Se obtiene la transformada hash del mensaje.
        signature = pss.new(key).sign(h)    #Se crea un objeto que permite hacer la firma y validación.
        start_time = timer()    #Se empieza a tomar el tiempo de ejecución.
        verifier = pss.new(key.publickey()) #Se crea el objeto capaz de validar la firma, para ello se usa la llave pública.
        try:
            verifier.verify(h,signature)    #Función que hace la valdiación de la firma.
            self.executionTime = timer() - start_time   #Fin de la toma de tiempo.
            print("La firma es correcta.")
            return 1    #La firma es auténtica.
        except(ValueError, TypeError):
            self.executionTime = timer() - start_time   #fin de la toma de tiempo.
            print("La firma no es correcta.")
            return 0    #La firma no es auténtica.

message = "04df2328374635f9f023"

rsa_pss = RSA_PSS()
rsa_pss.verify(message)
