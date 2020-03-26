from Writer import Writer

class HashingWriter:

    def __init__(self):
        self.writer = Writer('hashing_output.csv',['VECTORS','SHA-1','SHA-2','SHA-3'])
    
    def write(self, row):
        self.writer.write( row )