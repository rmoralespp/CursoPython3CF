""" Uso de properties para personalizar el acceso a los atributos de una clase """
class User:

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generatePassword(password)
        self.email = email

    def __generatePassword(self, passsword):
        return hash(passsword)

    @property
    def password(self):
        return  self.__password

    @password.setter
    def password(self, password):
        self.__password = self.__generatePassword(password)


rolando = User('rmoralesp', 'osolandia2018', 'rmoralespp@gamil.com')
print(rolando.password)
rolando.password = '2222'
print(rolando.password)

""" Metodos estaticos """

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @staticmethod
    def pi(): # Metodo de instancia
        return 3.14

    def area(self): # Metodo de instancia
        return self.radio**2 * Circulo.pi()


instacia_circulo = Circulo(20)
print(instacia_circulo.area())


""" Metodos de clase """

class Cocodrilo:
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def createCococdrilo(cls):
        return cls('cocodrilo jess')


c = Cocodrilo.createCococdrilo()
print(c.nombre)

