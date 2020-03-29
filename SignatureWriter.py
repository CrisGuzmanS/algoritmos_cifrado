from Writer import Writer

class SignatureWriter:

    def __init__(self):
        self.writer = Writer('signature_output.csv',['VECTORS','RSA-PSS','DSA','ECDSA'])
    
    def write(self, row):
        self.writer.write( row )