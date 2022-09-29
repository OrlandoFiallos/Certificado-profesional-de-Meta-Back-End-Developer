

'''
Method Resolution Order o MRO
-Funciona de abajo hacia arriba y de izquierda a derecha

Métodos para encontrar el MRO de una clase
-Método mro()
sintaxis
-Clase.mro()

-Método help() : Provee información más detallada
sintaxis
-help(clase)
'''
#Ejemplo 1

class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(C.mro())

'''
Salida:
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
'''

#Ejemplo 2
class A:
    pass
class B:
    pass
class C(A,B):
    pass

print(C.mro())
'''
Salida:
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
'''

# Ejemplo usando la función help
print(help(C))

'''
Help on class C in module __main__:

class C(A, B)
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object
 |
 |  Data descriptors inherited from A:
 |
-- Más  --
'''