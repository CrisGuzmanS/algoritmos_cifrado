from Writer import Writer

class DecryptionWriter:

    def __init__(self):
        self.writer = Writer('decryption_output.csv',['VECTORS','AES-EBC','AES-CBC','RSA_OAEP'])
    
    def write(self, row):
        self.writer.write( row )
