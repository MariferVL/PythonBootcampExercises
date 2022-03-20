import datetime

date =datetime.datetime.now().strftime("%d/%m/%Y")

# class Excepcion:

#     # Chequear si stock de producto1= Producto(), sucursal1=Sucursal() y bodega1=Bodega()   > 0
#     def sin_stock(x):
#         try:
#             x.stock >= 1
#         except:
#             print(f'{x.nombre} no tiene stock')
#         else:
#             print(f'El stock actual es de {x.stock} unidades.')

#     # Chequear que carro de clientes tenga máx 10 productos. De lo contrario, enviar mensaje de error.
#     def max_compra(cliente):
#         # cantidad=  productos_venta[key][0] 
#         poo.total_carrito <= 10
#         try:
#             print(f'Su carro contiene {cliente.carrito} unidades.')
#         except:
#             delete = len(cliente.carrito) - 10
#             if delete >= 1:
#                 print(f' Debe eliminar {delete} items de su carrito')
#                 print(f' ¿Qué desea eliminar?')
#                 print(cliente.carrito)
#                 eliminar = input('Producto a eliminar:')
#                 if eliminar in cliente.carrito:
#                     cliente.carrito.remove(eliminar)
#         finally:
#             print(f' {cliente.id_cliente},gracias por comprar en nuestra tienda.')

#     # Obtener valor promedio de compras del cliente y enviar mensaje en caso de que sea 0.
#     def compra_promedio(cliente, compras):
#         try:
#             resultado = sum(cliente.compras) / 2
#         except:
#             print(f' {cliente.id_cliente} no ha realizado compras')
#         else:
#             print(f'La compra promedio de {cliente.id_cliente} equivale a {resultado}')
#         finally:
#             print(f' Información actualizada al {date}.')

def indexError():
    n=int(input("\n> Ingrese folio del cliente:  "))
    try:
        shopping_list = [43500,33900,22500,80000] 
        print(f'>Los montos de compras de {str(n)} son: {str(shopping_list[n])}')
    except IndexError as e:
        print(f'>Cliente ID {str(n)} no existe')
        print(e)
    finally:
        print(f'\n > Información actualizada al {date}.\n')

def keyError():
    balance= {'Amanel': 110000000, 'Flame': 22000000, 'SS': 33333333}
    customer= input('\n> Ingrese nombre de usuario de cliente: ').capitalize()
    try:
        print(f'{customer} tiene ${balance[customer]} de saldo disponible en su cuenta.')
    except KeyError:
        print(f"> No se pudo obtener saldo disponible  de {customer}.")
    finally:
        print(f'\n > Información actualizada al {date}.\n')

def typeError():
    employee_list = ["Jim", "Ed", "Adele", "Paul"]
    indices = [0, 1, "2", 3]
    for i in range(len(indices)):
        try:
            print(employee_list[indices[i]])
        except TypeError:
            print("TypeError: Revise lista de índices.")
        finally:
            print(f'\n > La vida sigue...\n')


indexError()
keyError()
typeError()