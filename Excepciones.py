try:
    lista = [2, 0]
    print(lista[9])
    print(2/0)
except ZeroDivisionError as ex:
    print(ex) # Mensaje por defecto
    print("Ocurrio un error de division") # Mensaje personalizado
except IndexError as ex:
    print(ex) # Mensaje por defecto
    print("lista fuera de rango") # Mensaje personalizado
except Exception as ex:
    print(ex) # Mensaje por defecto
    print("Otro tipo de error") # Mensaje personalizado
finally: # Este bloque se va ejecutar siempre, aunque no haya error
    print("Se termino el script")
