'''
Clases abstractas
-Una clase abstracta puede considerarse como un modelo para otras clases
-No se pueden crear instancias de una clase abstracta
-Los métodos abstractos deben crearse en las clases derivadas
-Una clase abstracta puede tener uno o más métodos abstractos

Método abstracto
-Es un método que tiene una declaración pero no tiene una implementación
-Un método se vuelve abstracto cuando está decorado con la palabra clave @abstractmethod
'''
# Ejemplo de clase abstracta
from abc import ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangulo(Poligono):
    def sides(self):
        return '3 lados'

class Cuadrado(Poligono):
    def sides(self):
        return '4 lados'

t1 = Triangulo()
c1 = Cuadrado()

print(t1.sides(),'\n',c1.sides())
