# ABPro1



#  ----- Documentación -----



# 1) Creación de clases
# 2) Clase Cliente (atributos)
# 3) Clase Producto (atributos)
# 4) Clase Vendedor (atributos)
# 5) Encapsulación atributos
# 6) Cliente (métodos)
# 7) Integración métodos en menú
# 8) Instanciación
# 9) Gráfica las relaciones



#  ----- Desarrollo -----



# 1)
# Se crearán siguientes clases:
# Cliente --> linea 44
# Producto --> linea 74
# Vendedor --> linea 96



# 2)
# Clase Cliente

# atributos:
# a. ID Cliente
# b. Nombre
# c. Apellido
# d. Correo
# e. Fecha Registro
# f. __Saldo

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



# 3)
# Clase Producto:

# atributos:
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



# 4)
# Clase Vendedor

# atributos:
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



# 5)
# Atributos encapsulados
# __Saldo (Cliente) --> linea 42
# __Impuesto (Producto)  --> linea 82
# __Comision (Vendedor) --> linea 102



# 6)
# Creación métodos en la clase Cliente:
# saldo agregar --> linea 54
# mostrar saldo --> linea 57


# 7) Instanciación:

# Instanciación clase Clientes
cliente_1 = Cliente(1, 'Antorcha', 'Humana', 'antorcha@mail.com', '10-10-2022', 400100)
cliente_2 = Cliente(2, 'Batman', 'Wayne', 'batman@mail.com', '10-10-2022', 300200)
cliente_3 = Cliente(3, 'Capitán', 'America', 'capitan@mail.com', '10-10-2022', 20600)
cliente_4 = Cliente(4, 'Dalia', 'Negra', 'dalia@mail.com', '10-10-2022', 160000)
cliente_5 = Cliente(5, 'Mujer', 'Maravilla', 'maravilla@mail.com' , '10-10-2022', 200500)
cliente_6 = Cliente(6, 'Gato', 'Ton', 'gato@mail.com', '10-10-2022', 100200)

# Instanciación clase Productos
producto_1 = Producto(836942, 'zapatillas', 'calzado', 'china', 35, 329586)
producto_2 = Producto(642264, 'polearas', 'ropa', 'china', 735, 753773)
producto_3 = Producto(624426, 'zapatos', 'calzado', 'china', 24, 735735)
producto_4 = Producto(264624, 'poleron', 'ropa', 'eu', 45, 4685732)
producto_5 = Producto(624642, 'chaqueta', 'ropa', 'eu', 36, 753)
producto_6 = Producto(624642, 'guantes', 'accesorio', 'eu', 753, 735)

# Instanciación clase Vendedor
francisco = Vendedor('15999000-2', 'francisco', 'astete', 1)
ricardo = Vendedor('15555000-2', 'ricardo', 'castillo', 1)
javier = Vendedor('15666000-2', 'javier', 'espinoza', 1)
marifer = Vendedor('15777000-2', 'maría fernanda', 'villalobos', 1)
pato = Vendedor('158888000-2', 'patricio', 'garrido', 1)




# 5) 
# Integración con el desarrollo del módulo de Python Básico




# modulo con clases
from inspect import isclass
import modulo_pato as mp



# print(type(producto_1))
bodega = mp.Bodega(db,No)
bodega = mp.Bodega(bodega,producto_2)
bodega = mp.Bodega(bodega,producto_3)
# bodega = mp.Bodega(db,producto_1)

# x = bodega.crearBodega()
print(bodega)

# bodega.almacenarNuevosProductos(x)

# producto_7 = Producto(624642, 'gorros', 'accesorio', 'eu', 700, 300)
# bodega.almacenarNuevosProductos(producto_7)

# print(x[0].sku)
# print(len(x))

# 9)

# Piensen en una forma de graficar las relaciones
# entre las diferentes clases, 
# puede ser un diagrama o gráfica. Desarrollen el ejercicio de forma intuitiva.

# archivo adjunto: m4-ABP1-m4-ABPro1.jpg