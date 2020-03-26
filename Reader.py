class Reader:

    def __init__(self, filename):
        self.filename = filename
        self.vectors = []

    def read(self):
        f = open( self.filename )
        self.vectors = f.readlines()
        self.vectors = [line.rstrip() for line in self.vectors]
    
    def getVectors(self):
        return self.vectors

reader = Reader('input.txt')
reader.read()
print( reader.getVectors() )