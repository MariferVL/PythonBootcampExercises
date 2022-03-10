"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @staticmethod
    @abstractmethod
    def sonido(self):
        pass

    def saludar(self):
        print("hola, soy un animal y esto haciendo " + self.sonido())

class Perro(Animal):
    def sonido(self):
        return "Guau"


perro = Perro()
perro.saludar()
"""

#encapsulamiento
"""
class Clase:
    atributo_clase = "hola"
    __atributo_clase = "Hola! estoy encapsulado"

    def __mi_metodo(self):
        print("Estoy haciendo otras cosas")

    def metodo_normal(self):
        print("Estoy haciendo algo")
        self.__mi_metodo() #este metodo es accesible desde el interior

mi_clase = Clase()
#print(mi_clase.atributo_clase)
#mi_clase.metodo_normal()
#print(mi_clase.__atributo_clase)
#mi_clase.metodo_normal()
#print(dir(mi_clase))

#print(mi_clase._Clase__atributo_clase)
#mi_clase._Clase__mi_metodo()

"""

class Cuenta():
    def __init__(self, cli, sal, mon):
        self.__cliente = cli
        self.__saldo = sal
        self.__moneda = mon

    #getter
    def get_saldo(self):
        return self.__saldo

    @property
    def saldo(self):
        return "el saldo de la persona es de " + str(self.__saldo)

    def get_cliente(self):
        return self.__cliente
    
    def get_moneda(self):
        return self.__moneda
    
    #setter
    def set_moneda(self, moneda):
        self.__moneda = moneda


persona = Cuenta("Oscar Gonzalez", 14000, "USD")

#print(persona.get_saldo())
#print(persona.get_cliente())
#print(persona.get_moneda())
persona.set_moneda("pesos")
#print(persona.get_moneda())

print(persona.saldo)