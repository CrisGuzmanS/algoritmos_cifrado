from Writer import Writer

class VerifyWriter:

    def __init__(self):
        self.writer = Writer('verify_output.csv',['VECTORS','RSA_PSS','ECDSA','DSA'])
    
    def write(self, row):
        self.writer.write( row )
