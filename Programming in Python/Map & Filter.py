'''
map()
-Toma todos los objetos en la lista y permite aplicarle una función

map(function,iterable)
'''

cofees = ['Capuchino','Moca','Cortado','Americano']

def find(cofee):
    if cofee[0]=='C':
        return cofee

map_coffe = map(find,cofees)
# for i in map_coffe:
#     print(i)

'''
Salida:
Capuchino
None
Cortado
None
'''

'''
filter()
-Toma todos los objetos de la lista, crea una nueva lista y solo devuelve los valores donde la función evaluada es True

filter(function,iterable)

'''
filter_coffee = filter(find,cofees)
for i in filter_coffee:
    print(i)

'''
Salida:
Capuchino
Cortado
'''