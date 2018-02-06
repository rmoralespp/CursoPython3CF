import datetime

course = "Python 3"
name = "Rolando Morales"
fecha = datetime.date(2018, 1, 27)


""" Formas de Escribir Cadenas """
final_message1 = "Nuevo curso "+ course+ " por " + name # 1
final_message2 = "Nuevo curso %s por %s"%(course, name) # 2
final_message3 = "Nuevo curso {} por {}".format(course, name) # 3
final_message4 =  f'Nuevo curso Python {2+1} por {name}, {fecha:%A} {fecha:%d}, {fecha:%B}, {fecha:%Y}' # 4

print(final_message1)
print(final_message2)
print(final_message3)
print(final_message4)


""" Metodos de Cadenas """
cadena = 'Curso de Codigo Facilito de Python 3 por Rolando Morales'

print(cadena[0:5]) # Recorte de la cadena hasta el caratacter 4
print(cadena[-15:-8]) # Recorte de la cadena del caracter -15 hasta -7, imprimiria Rolando
print(cadena[0:10:2]) # Recorte de la cadena desde la posicion inicial hasta la 9 con salto 2
print(cadena[::-1]) # Imprimir la cadena revertida
print(cadena.replace(" ",',')) # Substituir espacios por comas
print(cadena.split(" ",)) # Convertir Cadena en Lista segun espacios en blanco
print(cadena.lower()) # Convertir a minusculas
print(cadena.upper()) # Convertir a mayusculas
print(cadena.title()) # Convertir cada incicial de cada palabra a mayusculas


""" Busqueda """
cadena = 'Curso de Codigo Facilito de Python 3 por Rolando Morales'

pos = cadena.find('Facilito') # 16
pos1 = cadena.find('facilito') # -1
count = cadena.count('a') # Cantidad de veces que encuentra el caracter


