# mpodulo que permite interconectar las clases
import datetime

class Proveedor:
    def __init__(self, nombre, RUT, nombre_legal, razon_social, pais, persona):
        self.nombre = nombre
        self.RUT = RUT
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.persona = persona


class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo, edad):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.edad = edad
        self.fecha_registro = fecha_registro
        self.saldito = saldo


    # Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
    def add_saldo(self, cantidad):
        self.__saldo += cantidad

    def get_saldo(self):
        print(self.saldito)


class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, color):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.color = color
        self.stock = stock
        self.__impuesto = 0.19
        self.valor_neto = valor_neto
        self.valor_bruto = self.valor_neto * (1 + self.__impuesto)


class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, fecha_ingreso):
        self.run = run
        self.nombre = nombre
        self.fechna_ingreso = fecha_ingreso
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        self.id_venta = []

        #+ Clase Vendedor:
                # Crear un método vender:
                #  ok       + clase Producto: Descontar el valor del atributo stock.
                #         + clase Vendedor: Sumar a atributo comisión (0.5% de comisión referente a valor_neto(producto))
                #  ok       + clase Cliente: descontar del atributo saldo (calcular el valor final del producto ).

    def vender(self, id_venta, cliente, productos, cantidad):

        # sobrecarga
        if id_venta in self.id_venta:
            print('ya hay una venta con esa id')
            exit()
        else:
            self.id_venta.append(id_venta)

        fecha_venta = datetime.datetime.now()

        productos_venta = {}

        try:
            for producto, cantidad in zip(productos, cantidad):
                # la llave del diccionario es una instancia de la clase producto
                productos_venta[producto] = [cantidad, producto.valor_neto, producto.valor_bruto]
        except Exception as error:
            print(error)
            print("El producto no existe")

        sub_total = sum(
            [productos_venta[key][0] * productos_venta[key][1] for key in productos_venta.keys()])

        impuesto_venta  = sum(
            [productos_venta[key][0] * (productos_venta[key][2] - productos_venta[key][1]) for key in productos_venta.keys()])

        total = sub_total + impuesto_venta

        if total > cliente.saldito:
            print("el cliente es pobre, terminando la transaccion")
            exit()
        else:
            cliente.saldito = cliente.saldito - total
            for producto in productos_venta.keys():
                if producto.stock >= productos_venta[producto][0]:
                    producto.stock = producto.stock - productos_venta[producto][0]
                else:
                    print(f"no hay stock del producto {producto.nombre}")

        suma_comision = sub_total*0.05
        self.__comision = self.__comision + suma_comision

        print("Resumen de venta")
        print("ID de venta: ", id_venta)
        print("Fecha de venta: ", fecha_venta)
        print("Cliente: ", cliente.id_cliente)
        print("Vendedor: ", self.run)
        print("\tcomision vendedor: ", self.__comision)
        print("Productos: ")
        for producto, cantidad in productos_venta.items():
            print("\t", producto.nombre, ": ", cantidad)
        print("Subtotal: ", sub_total)
        print("Impuesto: ", impuesto_venta)
        print("Total: ", total)


def reporte_estadistica_productos(db_productos: dict):
    """funcion que devuelve un reporte del estado del inventario"""
    # Se debe crear una lista con los productos que esten en stock
    print("Reporte de estado del inventario")
    for key in db_productos.keys():
        print(f'SKU {db_productos[key].sku} - {db_productos[key].nombre} - {db_productos[key].stock} en stock - '
            f'${db_productos[key].valor_neto}/unidad, '
            f'valor total en inventario: ${db_productos[key].valor_neto*db_productos[key].stock}'
            )
    print("Fin del reporte", end="\n\n")
