# -*- coding: utf-8 -*-

"""
    ! Clase que trabaja con binarios

    @author: Ángel
    @date: 13 \ 12 \ 2020 
"""

class Blob:

    def __init__(self, filename):
        self.filename = filename
    
    # Convierte a binario
    def toBinary(self):
        with open(self.filename, 'rb') as file:
            binarydata = file.read()

        return binarydata

    # Lo contrario a la función anterior
    def toFile(self, binarydata):
        with open(self.filename, 'wb') as file:
            file.write(binarydata)
