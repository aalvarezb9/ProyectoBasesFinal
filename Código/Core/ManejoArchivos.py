# -*- coding: utf-8 -*-


"""
    ! Se hace la compresión de los archivos y su proceso inverso
        * Esto se hace para enviar el archivo con ese formato a la BD B

    @author: Ángel
    @date: 13 \ 12 \ 2020 

"""

import gzip

class Manejo:
    def __init__(self, filename):
        self.filename = filename

    def comprimir(self, content):
        with gzip.open(self.filename + '.gz', 'wt') as f:
            f.write(content)

        return self.filename + '.gz'

    def descomprimir(self):
        with gzip.open(self.filename, 'rt') as f:
            data = f.read()

        return data
