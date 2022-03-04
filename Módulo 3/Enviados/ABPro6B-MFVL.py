# Comments are in Elementary Learner Mode.

#Rodrigo: Algunos comentarios los redacté en nivel básico para entenderlos y recordarlos.
# Otros ya son repetidos así que los comprimí. También dispuse algunos print como breakpoints 
# para que sea más fácil leer la terminal.

# Create a dict as a virtual warehouse with the initial products
productos= {"Zapatillas": 20,
            "Poleras": 10, 
            "Zapatos": 15, 
            "Poleron": 3, 
            "Chaquetas": 5, 
            "Guantes": 4
            }

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
        'u10_piloto': {'bag': []}, 'u11_piloto': {'bag': []}
        }

print("Comenzando Control de Bodega")

#Check available products.
def checking_products(dict):
    #Iterate parameter keys.
    for key in dict.keys():
        print(f'Producto:   {key}= {dict[key]} unidades')
#Call function with specific parameter (global var).                
checking_products(productos)

#Initiating new program from line 21 to 63.
#Step 2: Store new products.
def add_products():
    while True:
        store=productos
        #Data will be entered by terminal.
        #1st letter will be capitalized. Other option: all to lowercase(.lower()) or uppercase (.upper()).
        add_prod=input('Ingrese nuevo producto: ').capitalize()
        #Data will be converted to integer. 
        add_units=int(input('Ingrese número de unidades (sólo digitos): '))
        if add_prod in productos.keys():
            #Update products units.
            productos[add_prod]=productos[add_prod]+add_units
            #Update products stock and respective values in virtual warehouse.
            print(f'Producto {add_prod} actualizado exitosamente: {add_prod}: {productos[add_prod]} unidades')
        elif add_prod not in productos:      
            #Add new product with respctive key and value.
            productos[add_prod]=add_units
            #Update products stock in virtual warehouse.
            print(f'Producto {add_prod} agregado exitosamente: {add_prod}: {add_units} unidades')
        #if next function return True the var store will return updated.
        if storage_complete():
            return store 

#Step 3: Ask to add another product or to stop.
def storage_complete():
    answer = input("Desea agregar otro producto a bodega?: ").capitalize ()
    if answer == "No":
        #Continue with program.
        return True
    elif answer == "Sí" or "Si":
        #Comeback to add_products().
        return False
    else:
        print("Respuesta inválida")

#Step 4: Display the available/updated units per product.
def update_warehouse(storage_list):
    print(f'Bodega actualizada con nuevos productos: ' )
    #Go through each value in the data structure (dict), assign the value to a variable, and perform logic on each one individually.
    for product in storage_list:
        print(f"{product}: {storage_list[product]}")

#Step 1/5: Start/end the whole program.
def main():
    store= add_products()
    update_warehouse(store)
    print("Almacenaje Completado Exitosamente.")

# Driver Code
if __name__ == "__main__":
    main()

#Display breakpoint between main program and independent functions.
print("Funciones independientes según solicitado por ABPro6: ")

#Display and return an specific product in the store searching by name.
def specific_product():
    product= input('1. Ingrese el producto que desea revisar: ').capitalize()
    if product in productos:
        print(f'Disponemos de {productos[product]} unidades de {product}')
    elif product not in productos:
        print(f'Lo sentimos. Actualmente no contamos con {product}.')
        #Start function again.
        return specific_product()
#Call function.            
specific_product()

#Display and return all products in the store.
def whole_warehouse ():  
    print('2. Actualmente contamos con los siguientes productos:')
    #Go through each value in the data structure (dict).
    for key in productos.keys():
        print(f"{key}: {productos[key]}")
#Call function.            
whole_warehouse ()

#Display and return of products requested by the customer by entering a certain number of units.
def product_by_num():
    #Create an empty list to use in 'elif' condition.
    request=[]
    #Ask to the customer units they need.
    requested_prod=int(input('3. Ingrese unidades que necesita (sólo digitos): '))
    for key in productos.keys():        
        if requested_prod <= productos[key]:
            #Fill the list to use it in next condition.
            request.append(requested_prod)
            print(f'{key}: {productos[key]}') 
        #Condition to corroborate and inform the customer in case we don't have requested units.
        elif len(request) == 0:             
            print(f'Lo sentimos. Ninguno de nuestros productos tiene el stock que usted requiere.') 
            #Start function again.
            return product_by_num()
#Call function.            
product_by_num()

print("Fin Control de Bodega")
print('')
print("Comenzando Control de Ventas")

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

#Display all our customers.
def customers_list (x):  
    print('1. Estos son nuestros clientes:')
    #Put a dictionary directly into a for loop, activating __iter__() on that dictionary to iterate over its keys.
    for key in x.keys():
        #Display each user and their respective id.
        print(f"{key}: {x[key]}")
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
    #Iterate through dict.
    for item in bag_items.keys():
        # #Iterate through productos dict.
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
            print('Se agotaron sus intentos.')
            break
    if validation==True:
        confirm_purchase(bag)
    print('Fin de sesión')

# Driver Code
if __name__ == "__main__":
    main()

print("Fin Control de Ventas")