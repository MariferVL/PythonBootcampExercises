from Bodega import productos
from Clientes import *

employees={"emp1" : {"name": "Jim", "username": "Sturgess","age": 35},
        "emp2" :{"name": "Ryan", "username": "Gosling", "age": 35},
        "emp3" :{"name": "Violeta", "username": "Parra ", "age": 49},
        "emp4" :{"name": "Gato", "username": "Alquinta", "age": 35},
        "emp5" :{"name": "Anne", "username": "Hathaway", "age": 39},
        "emp6" :{"name": "Hae-Jo", "username": "Chang", "age": 35},
        "emp7" :{"name": "Willy", "username": "Rodríguez", "age": 44},
        "emp8" :{"name": "Adele", "username": "Blue", "age": 33},
        "emp9" :{"name": "Jhon", "username": "Lennon","age": 40},
        "emp10" :{"name": "Ed", "username": "Sheeran","age": 31}}

Bag={}

#Initiating shopping program.
#Step 2: Request purchase by customer id, product id and the units (1 by default) to buy.
#Identify customer.
def log_in():
    username= input('> Ingrese su Nombre de Usuario/ID:  ').capitalize
    if username in users.keys():
        print(f'!Bienvenid@ {users[username]}!')
        return username
    elif username not in users.keys():
        print("Aún no estás registrad@.")           
        print("Lo dirigiremos a sección Registro.")
        print('')
        return save_user()

def fill_bag():
    user_bag= {}
    #Display on terminal store products available.
    print("Nuestros productos disponibles son: ")
    for name in productos.keys():
        print(f'{name}')
    print('Ingresa el producto a comprar: ')
    to_bag= input().capitalize()
    print('')
    print('Ingresa unidades a comprar: (Sólo dígitos) ')
    units= int(input())
    user_bag[to_bag]= [units]


#Step 3: Confirm if required product has stock.
def product_validation(bag_items,productos):
    #Iterate through dict.
    for item in bag_items.keys():     
        if item in productos.keys():
            # unit= int(productos[item])
            if productos[item] >= bag_items[item]: 
                print('')
                print(f'Tu producto {item} a sido agregado a tu carrito de compras.')
                print('')
                return bag_items, True
            elif productos[item] <bag_items[item]:
                print('')
                print('Compra cancelada')
                print(f'Lo sentimos, no contamos con stock de {item} por el momento.')
                print('')
                return continue_or_exit()
            break
        elif item not in productos:
            print('')
            print('Compra cancelada')
            print(f'Lo sentimos, no contamos con stock de {item} por el momento.')
            print('')
            bag_items={}
            return bag_items, False


#Step 4: Confirm if product in bag is product customer wants.
def confirm_purchase(final_bag):
    print('Su compra es: ')
    for item in final_bag.keys():
        print(f' {item}: 1 unidad ')
        print('')
        answer= input('Si/No:  ').capitalize()
        if answer == "Sí" or "Si":
            print('Compra fue aprobada y está en camino.')
        elif answer == "No":
            print('Lo sentimos. Por favor, vuelve a a realizar tu compra.')
            return continue_or_exit()
        else:
            print("Respuesta inválida")
            print('')

#Step 1/5: Start/end the whole program.
def main():
    user=log_in()
    contador=0
    validation=False
    while validation==False:
        user_bag = fill_bag()
        user_bag, validation = product_validation(user_bag,productos)
        contador=contador+1
        if contador==3:
            print('Se agotaron sus intentos.')
            break
    if validation==True:
        confirm_purchase(user_bag)
    Bag[user]={user_bag}
    print('')
    print('Fin de sesión')

# Driver Code
if __name__ == "__main__":
    main()

