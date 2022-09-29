'''
Programación funcional
-Es un paradigma de programación que utiliza funciones para un código limpio, consistente y mantenible
-Particularmente hábil para manipular grandes cantidades de datos
-La programación funcional no cambia los datos fuera del alcance de la función, significa que la función debe evitar modificar los datos de entrada o argumentos

Hay dos tipos de funciones
-Tradicionales o traditional
-Puras o pure 

Funciones puras
-Es una función que no cambia o tiene un efecto sobre una variable, datos, listas, conjuntos más allá de su propio alcance
-Siempre harán lo mismo y devolverán los mismos resultados sin importar cuántas veces se llamen

Diferencias entre funciones tradicionales y puras
Tracicionales                                                            Puras
-Pueden acceder y modificar variables en el estado global           -No pueden
-Pueden acceder a variables en el estado local                      -Pueden acceder a variables en el estado local
-Pueden cambiar nuestros argumentos                                 -No pueden cambiar los argumentos
-Las salidas o output no dependen de las entradas                   -Las salidas o output sí dependen de las entradas



'''
'''Ejemplo de Pure function'''
list1 = [1,2,3,4]

def copy(list,new_item):
    new_list = list.copy()
    new_list.append(new_item)
    return new_list

new_list = copy(list1,8)
print(list1)
print(new_list)

'''
Salida:
[1, 2, 3, 4]
[1, 2, 3, 4, 8]
'''