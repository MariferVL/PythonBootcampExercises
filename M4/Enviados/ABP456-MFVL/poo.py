import datetime
import dalecolor as dc

# Agregar una clase Proveedor con los siguientes atributos:
# ● RUT 
# ● Nombre Legal
# ● Razón Social
# ● País
# ● Una distinción entre persona jurídica o persona natural
# A las clases creadas en la actividad anterior, incorpore un atributo opcional a cada una. 
# Al momento de instanciar un objeto de la clase Producto, deberá existir una Composición con la clase 
# Proveedor
#  https://pediaa.com/wp-content/uploads/2019/01/Difference-Between-Aggregation-and-Composition-Comparison-Summary-1.jpg

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
        print(dc.f(dc.jumbo('Saldo Cliente',1),'blue'))
        print(dc.f(f'El saldo de {self.nombre} {self.apellido} es: ${int(self.saldito)}','green','bold'))


class Producto:
    def __init__(self, sku, nombre, categoria, proveedor,stock, valor_neto, color):
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
    total_carrito=0
    def __init__(self, run, nombre, apellido, seccion, fecha_ingreso):
        self.run = run
        self.nombre = nombre
        self.fechna_ingreso = fecha_ingreso
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        self.id_venta = []


    def vender(self, id_venta, cliente, productos, cantidad):

        # sobrecarga
        if id_venta in self.id_venta:
            print('Existe venta previa con ese id.')
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
            print("El producto no existe.")
        despacho = 5000
        sub_total = sum(
            [productos_venta[key][0] * productos_venta[key][1] for key in productos_venta.keys()])

        impuesto_venta  = sum(
            [productos_venta[key][0] * (productos_venta[key][2] - productos_venta[key][1]) for key in productos_venta.keys()])

        total = sub_total + impuesto_venta + despacho

        if total > cliente.saldito:
            print("El cliente es pobre. Terminando la transacción")
            exit()
        else:
            cliente.saldito = cliente.saldito - total
            for producto in productos_venta.keys():
                if producto.stock >= productos_venta[producto][0]:
                    producto.stock = producto.stock - productos_venta[producto][0]
                else:
                    print(f"No hay stock del producto {producto.nombre}.")

        suma_comision = sub_total*0.05
        self.__comision = self.__comision + suma_comision

        # print list with table()       
        for key, value in productos_venta.items():
            p = (f'{producto.nombre} x {productos_venta[key][0]} unidades')

        print(dc.f(dc.jumbo('RESUMEN DE VENTAS',1),'blue'))
        list = [
            ["ID de venta:", str(id_venta)],
            ["Fecha de venta: ", str(fecha_venta)],
            ["Cliente:", str(cliente.id_cliente)],
            ["Vendedor:", str(self.run)],
            ["Productos:","           " ],
            ["           ",p],
            ["Despacho:", "$"+str(despacho)],
            ["Subtotal:", "$"+str(sub_total)],
            ["Impuesto:", "$"+str(int(impuesto_venta))],
            ["Total:", "$"+str(int(total))],
            ["",""],
            ["Comision vendedor:", "$"+str(self.__comision)],
        ]

        dc.table(
            list,
            # head = ['RESUMEN DE VENTAS', ''],
            # head_style = ['bold', 'white', 'BLUE'],
            style = ['normal', 'white', 'BLUE'],
            align = 'rigth',
            padding = ' ',
            margin = ''
            )

    def vender2(self, productos, cantidad):
        total_carrito= productos*cantidad
        return total_carrito

class BodegaPrincipal:
    def __init__(self,dirección,mts2,stock):
        self.dirección=dirección 
        self.mts2=mts2 
        self.stock = stock

    # descontará un valor desde su stock y luego sumará a una sucursa
    def despachar_producto(self,sucursal):
        #puse las mismas condiciones del método control_stock de Sucursal().
        if self.stock >= 300:
            if sucursal.stock <50:
                print ('solicitando y reponiendo productos')
                self.stock=self.stock-300
                sucursal.stock=sucursal.stock+300
            else: 
                print('No existe stock suficiente para reponer')

    def recepcionar_producto(self,repo):
        self.stock= self.stock + repo

#Falta instanciar Sucursal, Bodega
class Sucursal(BodegaPrincipal):
    def __init__(self, dirección, mts2,sku, nombre, categoria, proveedor,stock, valor_neto, color):
        self.stock= Producto(sku, nombre, categoria, proveedor,stock, valor_neto, color)
        super().__init__(dirección, mts2, stock)

    def despachar_producto(self, bodega): 
        extra= self.stock - 1000
        if extra >= 10:
            print ('Devolviendo productos a Bodega')
            bodega.stock=bodega.stock - extra
            self.stock=self.stock + extra

    def control_stock(self, bodega, sucursal):
        if bodega.stock >= 300:
            if sucursal.stock <50:
                print ('solicitando y reponiendo productos')
                bodega.stock=bodega.stock-300
                sucursal.stock=sucursal.stock+300
            else: 
                print('No existe stock suficiente para reponer')

    def limite_max(self,bodega):
        extra = self.stock - 500
        if extra >= 1:
            print('Se está enviando sobrecarga a Bodega.')
            bodega.stock=bodega.stock+ extra
            self.stock= self.stock - extra


class OrdenCompra:
    def __init__(self,id_ordencompra, sku, nombre, categoria, proveedor,stock, valor_neto, color):
        self.id_ordencompra = id_ordencompra
        #composición de la clase Producto y el atributo despacho, solo almacenará valores booleanos.
        self.producto= Producto(sku, nombre, categoria, proveedor,stock, valor_neto, color)
        self.despacho= True



def reporte_estadistica_productos(db_productos: dict):
    """funcion que devuelve un reporte del estado del inventario"""
    # Se debe crear una lista con los productos que esten en stock

    print(dc.f(dc.jumbo('Reporte de Estado del Inventario',1),'blue'))

    list = []
    for key in db_productos.keys():
        temp = [
            str(db_productos[key].sku),
            str(db_productos[key].nombre),
            str(db_productos[key].stock)+' en stock',
            str(db_productos[key].valor_neto),
            str(db_productos[key].valor_neto*db_productos[key].stock)
        ]
        list.append(temp)


    dc.table(
        list,
        head = ['SKU', 'PRODUCTO', 'STOCK', 'NETO ($)', 'TOTAL NETO (en inventario $)'],
        head_style = ['bold', 'white', 'BLUE'],
        style = ['normal', 'white', 'BLUE'],
        align = 'rigth',
        padding = ' ',
        margin = ''
        )



#BodegaPrincipal y Sucursal representan un caso de polimorfismo con el método despachar_producto.
#Definan la utilidad de MRO para determinados ejercicios de herencia.
# Orden de resolución de método (MRO) indica la forma en que un lenguaje de programación resuelve un método o atributo.En Python, el orden de resolución del método define el orden en el que se buscan las clases base al ejecutar un método. Primero, se busca el método o atributo dentro de una clase y luego sigue el orden que especificamos al heredar. Este orden también se denomina Linealización de una clase y el conjunto de reglas se denomina MRO(Orden de resolución de método). 
# Mientras hereda de otra clase, el intérprete necesita una forma de resolver los métodos que se llaman a través de una instancia. Por tanto, necesitamos el orden de resolución de método.
#             New style classes(Py 3.x & 2.2) → C3 Linearization algorithm 
