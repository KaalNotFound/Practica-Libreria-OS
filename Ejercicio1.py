import os

# Guarda el path
# Siempre importante reemprazar "\" por "/"
dir = 'C:/Users/Usuario/Downloads'

# Hago print de dir; listando archivos en el path asignado
with os.scandir(dir) as ficheros:
    for fichero in ficheros:
        print(fichero.name)
