import functools

""" Valores por omision """
def factorial(numero, resultado = 1):
    if numero == 0:
        return 0
    elif numero == 1:
        return resultado
    else:
        return factorial(numero - 1, resultado * numero)
print(factorial(5))

"""
Tipos de Argumentos
*   -> n valores -> tuplas
**  -> n valores -> diccionario
"""

""" Argumentos """
def division(valor1, valor2):
    return  valor1/valor2
resultado1 = division(3, 1) # Argumentos por posicion
resultado2 = division(valor2=1, valor1=3) # Argumentos por clave


""" Uso de la utilidad reduce + argumentos posicionales + lambda """
def suma(*valores):
    return functools.reduce(lambda v1, v2: v1+v2, valores)
print(suma(2, 4, 6))


""" Uso de argumentos por clave """
def imprimirArgumentos(**kwargs):
    print(kwargs) # Se tiene accesso a todos los parametros por clave en forma de diccionario
    valor_a = kwargs.get('a', False) # Tomo el valor de la clave a, sino tomo False
    if not valor_a:
        print("No contiene valor a")
imprimirArgumentos(b = 3, c =4, d = 5)


""" Retornar multiples valores """
def multiples():
    return "1", 2, {1: 1}, 'ssss'
resultado = multiples()
a, b, c, d = multiples()
print(resultado)
print(a, b, c, d)


""" Almacenando funciones en variables """
variable = multiples
print(variable())


""" Funciones Lambda """
funcion_lambda = lambda arg1, arg2: max(arg1, arg2) # Funcion anomima que retorna maximo valor
resultado3 = funcion_lambda(1, 3)
no_argumeto = lambda : 'no arugmento pasados'
print(resultado3)
print(no_argumeto())


""" Funciones Anidadas """
def division(numero1, numero2):
    def validacion():
        return numero1 > 0 and numero2 > 0
    if validacion():
        return numero1/numero2
    else:
        return "Parametros no validos"

print(division(2,5)) # retorna 0.4
print(division(2,0)) # retorna Parametros no validos


""" Closures -> Funciones que crean funciones """
def createFuncionValidacion(numero1, numero2):
    def validacion():
        return numero1 > 0 and numero2 > 0
    return validacion

my_funcion_validacion = createFuncionValidacion(2, 4)
print(my_funcion_validacion())



""" Generadores. Funciones que nos permiten crear objetos sin necesidad de guardarlos en memoria """
def generador(*args):
    """ Generador que nos permite elevar al cuadrado una lista de numeros """
    for valor in args:
        yield valor**2, True # Puedo retornar mas de 1 valor
for generado, myBool  in generador(1,2,3,4,5,6):
    print(generado, myBool)


""" Docstring. Documentar funciones """
def funcionDocumentada():
    """ Esta funcion imprime el mensaje Hola Mundo """
    print("Hola Mundo")
documentacion = funcionDocumentada.__doc__
nombre = funcionDocumentada.__name__
print(documentacion)
print(nombre)