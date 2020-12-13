# -*- coding: utf-8 -*-

class Blob:

    def __init__(self, filename):
        self.filename = filename
    
    def toBinary(self):
        with open(self.filename, 'rb') as file:
            binarydata = file.read()

        return binarydata

    def toFile(self, binarydata):
        with open(self.filename, 'wb') as file:
            file.write(binarydata)