variable_global = "Esto es una variable global"

def setGlobal():
    global variable_global
    variable_global = "Variable global modificada desde una funcion"

print(variable_global)
setGlobal()
print(variable_global)


def createGlobal():
    global nueva_variable
    nueva_variable = "Variable global creada desde una funcion"

createGlobal()
print(nueva_variable)