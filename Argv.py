import  sys

if __name__ == '__main__':
    print(sys.argv) # Acceso a los argumentos pasados al ejecutar el script en forma de lista
    if len(sys.argv) == 1:
        # El 1er argumento es el filename del script
        print("Es necesario colocar al menos un argumento")
    else:
        pass
