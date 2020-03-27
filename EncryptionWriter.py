from Writer import Writer

class EncryptionWriter:

    def __init__(self):
        self.writer = Writer('encryption_output.csv',['VECTORS','AES-EBC','AES-CBC','RSA_OAEP'])
    
    def write(self, row):
        self.writer.write( row )