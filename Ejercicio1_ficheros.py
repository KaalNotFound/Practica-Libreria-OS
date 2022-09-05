import os
import pprint

dir = 'C:/Users/Usuario/Downloads'

with os.scandir(dir) as ficheros:
    for fichero in ficheros:

        #      fichero.name for fichero in ficheros if fichero.is_file() and fichero.endswith('jpg')]
        # Esto se hace asi
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file(
        )]
