import csv

class Writer:
    def __init__(self,filename,header):
        self.filename = filename
        with open(filename, 'w',  newline='' ) as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(header)

    def write(self, row):
        with open(self.filename, 'a', newline='' ) as myfile:
            wr = csv.writer(myfile)
            wr.writerow(row)