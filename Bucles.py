""" Bucle While que imnprime numeros del 1 al 10 """
contador = 10
while contador > 0: # Condicion
    #codigo cuando se cumpple
    print(11 - contador)
    contador -= 1
else:
    # codigo no cuando se cumpple
    print("Termino de contar")


""" Bucle While que imnprime numeros del 1 al 5 """
contador = 10
while contador > 0: # Condicion
    #codigo cuando se cumpple
    print(11 - contador)
    contador -= 1
    if contador == 5:
        print("Termino de contar pk es igual a 5")
        break
    else:
        continue
else:
    # codigo cuando no se cumpple
    print("Termino de contar")


""" Bucle for que imnprime numeros del 1 al 10 """
for item in range(1,10, 1): # range k crea iterador con paso 1
    print(item)

""" Bucle for que inprime los elementos de la lista e indices """
for i, item in enumerate(['a', 'b', 'c']): # enumerate k permite acceder al elemento e indice
    print(f'{item} tiene el indice {i}')