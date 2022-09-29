'''
Recursion o Recursividad

-Recursividad es una función que se llama a si misma
-La declaración de retorno devuelve la misma función
-La recursividad es similar a un bucle for
'''
#Comparación, encontrar el factorial de un número usando un ciclo for y usando una función recursiva

def factorial1(number):
    if number < 0:
        return 0
    else:
        factorial = 1
        for i in range(1,number+1):
            factorial *=i
        return factorial

print(factorial1(5))

def factorial2(number):
    if number == 1:
        return 1
    else:
        return number * factorial2(number - 1)

print(factorial2(5))

'''
Ventajas de la recursion
-Código más ordenado y menos voluminoso
-Las tareas complejas se pueden desglosar en subproblemas más fáciles de leer
-La generación de secuencias puede ser más fácil de entender que los bucles anidados

Desventajas de la recursion
-Puede ser más difícil seguir la lógica en código recursivo
-En términos de memoria puede ser costoso en ineficiente
-Puede ser difícil de depurar y seguir el código
'''