import os

# Listado de archivos
fileDir = r'C:/Users/Usuario/Downloads'
fileExt = r'.exe'
# Printeo la lista
print('')
print('Voy a DETECTAR el OOrDen')
print('')

for file in os.listdir(fileDir):
    if file.endswith(fileExt):
        print(file)

print('')
# Obteniendo la Ruta de Trabajo
obtener_ruta = os.getcwd()
print(obtener_ruta)
