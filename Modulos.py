import Funciones #1- Importar Modulo
from Funciones import division, createFuncionValidacion #2- Importar funcionalidades de un modulo
from Funciones import division as myDivision #3- Importar funcionalidades de un modulo sobrescribiendo su nombre
from Funciones import * #4- Importar todas las funcionalidades de un modulo

valor = Funciones.division(1,2) #1
valor1 = division(1,2) #2
funcion = createFuncionValidacion(1, 2) #2
valor2 = myDivision(1, 2) #3

""" Estructura Modulo """

#1
""" 
Es necesario escrbibir la Documentacion del Modulo 
"""


#2
""" Metadatos del modulo """
__author__ = "Rolando Morales Perez"
__copyright__ = "Copyright 2018"
__credits__ = "Los creditos"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rolando Morales Perez"
__status__ = "Developer"
__email__ = "rmoralesp@gmail.com"


#3
""" Uso de la palabra __main__ """
if __name__ == '__main__': # Es este el script principal, o sea es el script que estoy ejecutando?
     #Si soy el script principal ejecuta el code
     pass
else:
    # Entonces soy un import
    pass