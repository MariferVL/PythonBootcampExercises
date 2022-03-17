from main import *
from poo import *

class Excepcion:

    # Chequear si stock de producto1= Producto(), sucursal1=Sucursal() y bodega1=Bodega()   > 0
    def sin_stock(x):
        try:
            x.stock >= 1
        except:
            print(f'{x.nombre} no tiene stock')
        else:
            print(f'El stock actual es de {x.stock} unidades.')

    # Chequear que carro de clientes tenga máx 10 productos. De lo contrario, enviar mensaje de error.
    def max_compra(cliente):
        # cantidad=  productos_venta[key][0] 
        poo.total_carrito <= 10
        try:
            print(f'Su carro contiene {cliente.carrito} unidades.')
        except:
            delete = len(cliente.carrito) - 10
            if delete >= 1:
                print(f' Debe eliminar {delete} items de su carrito')
                print(f' ¿Qué desea eliminar?')
                print(cliente.carrito)
                eliminar = input('Producto a eliminar:')
                if eliminar in cliente.carrito:
                    cliente.carrito.remove(eliminar)
        finally:
            print(f' {cliente.id_cliente},gracias por comprar en nuestra tienda.')

    # Obtener valor promedio de compras del cliente y enviar mensaje en caso de que sea 0.
    def compra_promedio(cliente, compras):
        try:
            resultado = sum(cliente.compras) / 2
        except:
            print(f' {cliente.id_cliente} no ha realizado compras')
        else:
            print(f'La compra promedio de {cliente.id_cliente} equivale a {resultado}')

        # (*Si “compras” es una lista en el constructor de esa clase: sum(self.compras))


# cantidad = productos_venta[key][0]