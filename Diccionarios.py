"""
1- las claves deben ser inmutables
2- Si se repiten las claves el valor es el ultimo que encuentra
"""

diccionario = {'a': 1, 'b': True }
print(diccionario)

# Adicionar elementos
diccionario['c'] = 'Nuevo elemento'
print(diccionario)

# Modificar elementos si encuentra la clave sino lo crea
diccionario['a'] = False
print(diccionario)

# Obtener datos
valor  = diccionario['a']
print(valor)
""" Para evitar problemas sino encvuentra el elemnto se debe utilizar get"""
valor = diccionario.get('z',False)
print(valor) # Si encuentra la clave retorna el elemento sino False(pk se definio de esa manera)

# Eliminar datos
del diccionario['a']
print(diccionario)


# Obtener Claves
claves = diccionario.keys()
claves_lista = list(claves) # como lista
claves_tupla = tuple(claves) # como tupla

# Obtener elementos como tuplas
items = diccionario.items()
items_lista = list(items) # como lista
items_tupla = tuple(items) # como tupla


# Obtener valores
valores = diccionario.values()
valores_lista = list(valores) # como lista
valores_tupla = tuple(valores) # como tupla

# incrementar diccionarios
dic_incremento  = {'a': 'hola'}
dic_incremento.update({'b': 'mundo'})
print(" ".join(list(dic_incremento.values()))) # Return String Hola Mundo
