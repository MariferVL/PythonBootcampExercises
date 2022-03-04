productos= {"Zapatillas": 20,
            "Poleras": 10, 
            "Zapatos": 15, 
            "Poleron": 3, 
            "Chaquetas": 5, 
            "Guantes": 4
            }


#Request purchase by customer id, product id and the units (1 by default) to buy.
def fill_bag():
    bag= {}
    print("Los ID de nuestros productos disponibles: ")
    for name in productos.keys():
        print(f'{name}')
    print('Ingresa el ID del producto a comprar: ')
    to_bag= input().capitalize()
    bag[to_bag]= 1
    return bag

#Confirm if required product has stock.
def product_validation(bag_items,productos):
    #Iterate through product_id dict.
    for item in bag_items.keys():
        # #Iterate through productos dict.
        # for name in productos.keys():
        if item in productos.keys():
            unit= int(productos[item])
            if unit >=1: 
                print(f'Tu producto {item} a sido agregado a tu carrito de compras.')
                return bag_items, True
            elif unit==0:
                print('Compra cancelada')
                print(f'Lo sentimos, no contamos con stock de {item} por el momento.')
            break
        elif item not in productos:
            print('Compra cancelada')
            print(f'Lo sentimos, no contamos con stock de {item} por el momento.')
            bag_items={}
            # product_validation(fill_bag(), productos)
            return bag_items, False

def confirm_purchase(final_bag):
    print('Su compra es: ')
    for item in final_bag.keys():
        print(f' {item}: 1 unidad ')
        answer= input('Si/No:  ').capitalize()
        if answer == "Sí" or "Si":
            print('Compra aprobada y en camino')
        elif answer == "No":
            print('Lo sentimos. Por favor, vuelve a a realizar tu compra.')
            break
        else:
            print("Respuesta inválida")


def main():
    contador=0
    validation=False
    while validation==False:
        bag = fill_bag()
        bag, validation = product_validation(bag,productos)
        contador=contador+1
        if contador==3:
            print('Fin del programa')
            break
    if validation==True:
        confirm_purchase(bag)
    print('Fin de sesión')

# Driver Code
if __name__ == "__main__":
    main()
