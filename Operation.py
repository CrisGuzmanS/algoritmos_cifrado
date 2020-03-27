class Operation:

    def read(self):
        f = open("operation.txt","r")
        self.operation = f.readline().lower()
    
    def isHashing(self):
        return self.operation == 'hashing'

    def isEncryption(self):
        return self.operation == 'encryption'

    def isDecryption(self):
        return self.operation == 'decryption'

    def isVerifying(self):
        return self.operation == 'verifying'
    
    def isSigning(self):
        return self.operation == 'signing'