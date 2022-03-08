#La Clase Cliente deberá contar con los siguientes atributos:
# a. ID Cliente
# b. Nombre
# c. Apellido
# d. Correo
# e. Fecha Registro
# f. __Saldo
# import random


class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo

    # Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
    def add_saldo(self, cantidad):
        self.__saldo += cantidad

    def get_saldo(self):
        return self.__saldo


# La Clase Producto deberá contar con los siguientes atributos:
# g. SKU
# h. Nombre
# i. Categoría
# j. Proveedor
# k. Stock
# l. Valor_Neto
# m. __Impuesto = 1.19

class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19


# La Clase Vendedor deberá contar con los siguientes atributos:
# n. RUN
# o. Nombre
# p. Apellido
# q. Sección
# r. __Comision = 0

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0



# Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Vendedor) se
# encuentren encapsulados.

  # ok


# Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
# correctamente los métodos de las clases en las opciones del menú desarrollado.





# Instanciación clase Clientes
cliente_1 = Cliente(1, 'Antorcha', 'Humana', 'antorcha@mail.com', '10-10-2022', 400100)
cliente_2 = Cliente(2, 'Batman', 'Wayne', 'batman@mail.com', '10-10-2022', 300200)
cliente_3 = Cliente(3, 'Capitán', 'America', 'capitan@mail.com', '10-10-2022', 20600)
cliente_4 = Cliente(4, 'Dalia', 'Negra', 'dalia@mail.com', '10-10-2022', 120000)
cliente_5 = Cliente(5, 'Mujer', 'Maravilla', 'maravilla@mail.com' , '10-10-2022', 200500)
cliente_6 = Cliente(6, 'Gato', 'Ton', 'gato@mail.com', '10-10-2022', 100200)

# Instanciación clase Productos
tenedor_1 = Producto('123', 'tenedor', 'cubiertos', 'Plasticos Alfa', 714, 34)
tenedor_2 = Producto('124', 'tenedor', 'cubiertos', 'Plasticos Alfa', 114, 34)
tenedor_3 = Producto('125', 'tenedor', 'cubiertos', 'Plasticos Alfa', 514, 44)
tenedor_4 = Producto('126', 'tenedor', 'cubiertos', 'Plasticos Alfa', 414, 24)
tenedor_5 = Producto('127', 'tenedor', 'cubiertos', 'Plasticos Alfa', 314, 14)

# Instanciación clase Vendedor
francisco = Vendedor('15999000-2', 'francisco', 'astete', 1)
ricardo = Vendedor('15555000-2', 'ricardo', 'castillo', 1)
javier = Vendedor('15666000-2', 'javier', 'espinoza', 1)
marifer = Vendedor('15777000-2', 'maria fernanda', 'villalobos', 1)
pato = Vendedor('158888000-2', 'patricio', 'garrido', 1)


# Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
# Piensen en una forma de graficar las relaciones entre las diferentes clases,
# puede ser un diagrama o gráfica
# Desarrollen el ejercicio de forma intuitiva.








# class Casa:
#     def __init__(self, direccion, dueno):
#         self.direccion = direccion
#         self.__dueno = dueno # __ no heredable
#
# class tipoCasa(Casa):
#     def __init__(self, direccion, dueno, tipo):
#         super().__init__(direccion, dueno)
#         self.tipo = tipo
#
# ca = tipoCasa("Calle falsa 123", "Juan", "mansion")
# print(ca.__dueno)
#
