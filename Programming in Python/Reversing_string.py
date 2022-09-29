'''
Como revertir el orden de los elementos de una cadena
-En python no hay una función integrada que resuelva este problema

Hay 2 formas de hacerlo
-Utilizando slice function
-Recursion

'''

#Utilizando slice function
str = 'reversal'
new_str = str[::-1]
print(new_str)

'''
Salida:
lasrever
'''

#Utilizando recursion
def strin_reverse(str):
    if len(str) == 0:
        return str
    else:
        return strin_reverse(str[1:]) + str[0]

reverse = strin_reverse(str)
print(reverse)

'''
Salida:
lasrever
'''
