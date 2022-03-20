# Manejo de bodega  
from Main_Bodega import menu
import time
import random


# n = random.randint(300,500)

# Create a dict as a virtual warehouse with the initial products. 
# Random stock between 300 and 500 units + product description.
productos= {"Vasos": {"units": random.randint(300,500), "made": "Chile" },
            "Cucharas": {"units": random.randint(300,500), "made": "Chile" }, 
            "Cuchillos": {"units": random.randint(300,500), "made": "Chile" },
            "Tenedores": {"units": random.randint(300,500), "made": "Chile" },
            }

employees= {"emp1" : {"name": "Jim", "username": "Sturgess","age": 35},
        "emp2" :{"name": "Ryan", "username": "Gosling", "age": 35},
        "emp3" :{"name": "Violeta", "username": "Parra ", "age": 49},
        "emp4" :{"name": "Gato", "username": "Alquinta", "age": 35},
        "emp5" :{"name": "Anne", "username": "Hathaway", "age": 39},
        "emp6" :{"name": "Hae-Jo", "username": "Chang", "age": 35},
        "emp7" :{"name": "Willy", "username": "Rodríguez", "age": 44},
        "emp8" :{"name": "Adele", "username": "Blue", "age": 33},
        "emp9" :{"name": "Jhon", "username": "Lennon","age": 40},
        "emp10" :{"name": "Ed", "username": "Sheeran","age": 31}
            }

#Store new products or add units.
def add_products():
    print ("\n Adición de productos o unidades: \n")
    print(productos)    
    #Data will be entered by terminal.
    add_prod=input('\n>   Ingrese nombre de producto: ').capitalize()
    #Data will be converted to integer. 
    add_units=int(input('>   Ingrese número de unidades (sólo digitos): '))
    if add_prod in productos.keys():
        #Update products units.
        productos[add_prod]["units"] = productos[add_prod]["units"] + add_units
        #Update products stock and respective values in virtual warehouse.
        print(f'\n Producto {add_prod} actualizado exitosamente: {add_prod}: {productos[add_prod]["units"]} unidades. \n')
    elif add_prod not in productos:     
        print(f'\n Nuevo producto {add_prod} será agregado a Bodega Virtual. \n')
        made= input(">   Ingrese país de origen del producto: ").capitalize()
        #Add new product with respctive key and value.
        productos[add_prod]={"unit":add_units, "made": made}
        #Update products stock in virtual warehouse.
        print(f'\n Producto {add_prod} agregado exitosamente: {add_prod}: {add_units} unidades, hecho en {made}. \n')
    return productos, menu()   

#Decrease units number per product.
def rest_units():
    print ("\n Reducción de unidades: \n")    
    rest_prod=input('>   Ingrese nombre de producto: ').capitalize()
    if rest_prod in productos.keys():
        print(f'\n Actualmente contamos con {productos[rest_prod]["units"]} de {rest_prod}.')
        print('>   Ingrese número de unidades a eliminar (sólo digitos): ')
        #Data will be converted to integer.
        rest_units=int(input())
        #Update products units.
        productos[rest_prod]["units"] = productos[rest_prod]["units"] - rest_units
        #Update products stock and respective values in virtual warehouse.
        print(f'\n Unidades de {rest_prod} actualizado exitosamente: {rest_prod}: {productos[rest_prod]["units"]} unidades \n')
        return productos, menu()
    else:
        print(f'{rest_prod} no es parte de nuestro inventario.\n')
    return productos, menu()

#Remove products from the virtual warehouse.
def remove_products():
    print ("\n Eliminación de productos: \n")    
    rest_prod=input('>   Ingrese nombre de producto: ').capitalize()
    remove_prod = productos.pop(rest_prod, None)
    if remove_prod != None:
        print(f"\t{rest_prod} ha sido removido de la bodega.\n")
        
    else:
        print(f'\t{rest_prod} no es parte de nuestro inventario.\n')
    return productos, menu()


#Display and return all products in the store.
#NameError if it's used after another function. Works if it's used first.
def whole_warehouse(): 
    print('\n Actualmente contamos con los siguientes productos:')
    #Go through each value in the data structure (dict).
    for key in productos.keys():
        print(f"{key}: {productos[key]}")
        time.sleep(1)
    print("")
    return productos, menu()

#Check if a product units are < 400  and send an alert.
def stock_alert():
    for key in productos.keys():
        if productos[key]["units"] < 400:
            print(f'\n La bodega cuenta con {productos[key]["units"]} de {key}')
            repo= 400- productos[key]["units"] 
            productos[key]["units"]= productos[key]["units"] + repo
            print(f'\n Hemos recibido {repo} unidades del Proveedor.')
            print(f'Ahora contamos con {productos[key]["units"]} de {key} \n')
    return productos

