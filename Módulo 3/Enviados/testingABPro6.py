# Control Bodega

# Create a dict as a virtual warehouse with the initial products
productos= {"Zapatillas": 20,
            "Poleras": 10, 
            "Zapatos": 15, 
            "Poleron": 3, 
            "Chaquetas": 5, 
            "Guantes": 4
            }
#Check available products.
def checking_products(dict):
    #Iterate parameter keys.
    for key in dict.keys():
        print(f'Producto:{key} = {dict[key]} unidades')
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