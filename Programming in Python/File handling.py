'''
Manejo de archivos o File handling
-El manejo de archivos incluye abrir, leer y escribir archivos entre otras operaciones.
-En Python hay dos funciones para el manejo de archivos estas son open y close
'''
'''
Open function
open(<FILENAME><FILELOCATION>,<MODE>)
-mode: indica que acción se requiere como leer, escribir o crear, además indica si desea que el archivo salga en formato de texto o binario

'''
'''
Mode sets o modos de manejo de archivo (parámetro mode)
mode = 'r' Se utiliza para abrir y leer un archivo en formato texto, para binario rb
mode = 'r+' Abre el archivo tanto para lectura como para escritura 
mode = 'w' Abre el archivo para escritura, sobreescribirá el archivo existente
mode = 'a' Abre el archivo para editar o agregar datos
'''

'''
Close function o función de cierre
-Se utiliza para cerrar la conexión de archivos abiertos, no necesita ningún argumento
'''
'''
Otra forma de abrir y manejar archivos en Python
-Con With open function
-La ventaja con respecto a la otra forma es que no necesitamos cerrar el archivo(utilizar la función close()) porque él lo hace automáticamente
'''
#Ejemplo 1 primera forma

file = open('Handling.txt','r')
data = file.readline()
print(data)
file.close()

'''
Salida:
Contenido dentro de File handling!!!!
'''

#Ejemplo 2 segunda forma with open
with open('Handling.txt','r') as file:
    data = file.readline()
    print(data)

'''
Salida:
Contenido dentro de File handling!!!!
'''
