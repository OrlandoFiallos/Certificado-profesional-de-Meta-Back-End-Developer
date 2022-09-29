'''
Creando nuevos archivos con la función open y añadiendoles contenido

'''
#Creando el nuevo archivo
# with open('new.txt','w') as file:
#     file.write('Nuevo archivo creado')

# Utilizando el método write
# with open('new.txt','w') as file:
#     file.write('Nuevo archivo creado skuuuu')

# Utilizando el método writelines
'''
writelines([]) escribe los elementos de una lista en el archivo (le pasamos como argumento una lista)
'''
with open('new.txt','a')as file:
    file.writelines(['\nPrimera linea','\nSegunda linea agregada con writelines'])