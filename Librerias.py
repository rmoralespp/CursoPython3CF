
""" Libreria random -------------------------------------------------------------------------------------------------"""
import random

# Uso 1
lista = [2, 4 ,16, 6 ]
valor_random1 = random.choice(lista) # Selecciona un valor aleatorio de la lista
print(valor_random1)

# Uso 2
valor_random2 = random.randint(1, 200) # Selecciona un valor aleatorio entre 1 y 200
print(valor_random2)

# Uso 3
lista = [2, 4 ,16, 6 ]
random.shuffle(lista) # Desordena la lista
print(lista)


""" Libreria datetime -----------------------------------------------------------------------------------------------"""
import datetime
print(datetime.datetime.now()) # Hora actual



