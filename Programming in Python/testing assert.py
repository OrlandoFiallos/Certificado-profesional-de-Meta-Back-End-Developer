'''
Assert
-Prueba si una condición retorna True, si no, se generará un AssertionError
-La palabra clave assert se utiliza cuando depuramos código
-Podemos escribir un mensaje si el código retorna falso

'''


#Ejemplo 1
word = 'palabra'
assert word == 'palabra' 
#Sí se cumple la condición no pasa nada

#Ejemplo 2
word2 = 'palabra2'
assert word2 =='palabreria'

'''
Nos generea un AssertionError si la condición retorna False
Salida:
File "c:\Users\Manuel Fiallos\Documents\Back-End Developer Meta\Programming in Python\testing assert.py", line 16, in <module>
    assert word2 =='palabreria'
AssertionError
'''
#Ejemplo 3 escribiendo un mensaje si la condición es falsa

word3 = 'espectacular'
assert word3 =='palabra 3', "word3 debe ser igual a palabra 3"

'''
Salida:
Traceback (most recent call last):
  File "c:\Users\Manuel Fiallos\Documents\Back-End Developer Meta\Programming in Python\testing assert.py", line 9, in <module>
    assert word3 =='palabra 3', "word3 debe ser igual a palabra 3"
AssertionError: word3 debe ser igual a palabra 3
'''