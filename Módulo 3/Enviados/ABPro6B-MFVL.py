# Comments are in Elementary Learner Mode.

#Control de Ventas 

#Create a dictionary with customers names and IDs.
users={'u1_piloto': 'Jim Sturgess', 'u2_piloto': 'Ryan Gosling',
        'u3_piloto': 'Violeta Parra', 'u4_piloto': 'Gato Alquinta',
        'u5_piloto': 'Anne Hathaway', 'u6_piloto': 'Hae-Jo Chang',
        'u7_piloto': 'Willy Rodríguez', 'u8_piloto': 'Adele Blue',
        'u9_piloto': 'Jhon Lennon', 'u10_piloto': 'Ed Sheeran', 
        'u11_piloto': 'Franco Scott'}  

#Create an empty list to save customer purchases.
bags={'u1_piloto': {'bag': []}, 'u2_piloto': {'bag': []}, 'u3_piloto': {'bag': []},
        'u4_piloto': {'bag': []}, 'u5_piloto': {'bag': []}, 'u6_piloto': {'bag': []},
        'u7_piloto': {'bag': []}, 'u8_piloto': {'bag': []}, 'u9_piloto': {'bag': []},
        'u10_piloto': {'bag': []}, 'u11_piloto': {'bag': []}}

productos= {"prod1":{"Zapatillas": 20},
            "prod2":{"Poleras": 10}, 
            "prod3":{"Zapatos": 15}, 
            "prod1":{"Poleron": 3}, 
            "prod1":{"Chaquetas": 5}, 
            "prod1":{"Guantes": 4}
            }

#Display and return number of customers.
def users_number(x):
    #Var with len function, which returns number of items in an object.
    n_users=len(x.keys())
    #Display result.
    print(f'Actualmente contamos con {n_users} usuarios.')
    return n_users
#Call the function
users_number(users)
print(f'')

#Display and return all our customers.
def customers_list (x):  
    print('Estos son nuestros clientes:')
    #Put a dictionary directly into a for loop, activating __iter__() on that dictionary to iterate over its keys.
    for key in x.keys():
        #Display each user and their respective id.
        print(f"{key}: {x[key]}")
    return
customers_list (users)

#Identify customer.
def log_in(x):
    user_id= input('Ingrese su ID:  ')
    for id in x.keys():
        if user_id== id:
            print(f'!Bienvenid@ {x[user_id]}!')
        elif user_id not in x.keys():
            print("Aún no estás registrad@.Por favor, ingresa a Sing In.")           
log_in(users)

#Request purchase by customer id, product id and the units to buy.
def fill_bag():
    bag= {}
    print('Ingresa el ID del producto a comprar: ')
    to_bag= input().lower()
    bag[to_bag]= 1
    if product_validation():
        return bag

def product_validation(product):
    for item_bag in product.keys():
        for item, info in productos.items():
        #Iterate the items in the nested dictionary.
            for key in info.items():
                if item_bag in info.keys() and product[item_bag] >=1:
                    print(f'Tu producto {item_bag} a sido agregado a tu carrito de compras.')
                    return True
                else:
                    print('Compra cancelada')
                    print('Lo sentimos, no contamos con stock de {} por el momento.')
                    return False

def confirm_purchase(x):
    print('Su compra es: ')
    for item in x.items():
        print(f' {item}: 1 unidad ')
        answer= input('Si/No:  ')
        if answer == "Sí" or "Si":
            return True
        elif answer == "No":
            print('Lo sentimos. Por favor, vuelve a a realizar tu compra.')
            return False
        else:
            print("Respuesta inválida")


def main():
    bag = fill_bag()
    confirm_purchase(bag)
    print('Compra aprobada y en camino')

# Driver Code
if __name__ == "__main__":
    main()
