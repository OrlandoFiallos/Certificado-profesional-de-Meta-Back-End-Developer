'''
Métodos para leer archivos en python

-read() Devuelve todo el contenido del archivo como un string que contendrá TODOS los caracteres, además acepta como parámtro un entero que determina el número de caracteres que queremos mostrar
-readline() Devuelve la PRIMERA LINEA del archivo como un string, de igual manera que read() acepta como parámetro un entero para especificar el número de caracteres que queremos mostrar
-readlines() Lee todo el contenido del archivo y lo retorna como una LISTA ORDENADA, importante porque podemos iterar sobre la lista y mostrar el contenido de manera más ordenada
'''

with open('new.txt','r') as file:
    data = file.readlines()
    print(len(data))
    for indx, i in enumerate(data):
        print(indx+1,'.',i)