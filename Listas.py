my_lista = [1, "string", "de Locos"]

""" Metodos Principales Listas """
my_lista.append(6) # Adicionar 6 al final de la lista
my_lista.insert(2, "Nuevo elemento") # Insertar Nuevo elemento en la pos 2
my_lista.remove("string") # Eliminar elemento string
print(my_lista)

""" Ordenar Listas """
my_lista = [1, 2, 3]
my_lista.sort(reverse = True)
print(my_lista)


""" Conctatenar Listas """
my_lista1 = [5, 6, 7]
my_lista.extend(my_lista1) # Concatenar listas forma 1
print(my_lista)
print(my_lista + my_lista1) # Concatenar listas forma 2

""" Buscar en Listas """
a = my_lista.__contains__(1) # True si lo encuentra sino False
b = my_lista.count(1) # Cantidad de elementos 1 que encuentra
