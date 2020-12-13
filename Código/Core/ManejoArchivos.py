# -*- coding: utf-8 -*-

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
