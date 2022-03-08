""" 
random 300 y 500 unidades.
● Debe definir funciones que puedan: 
● Verificar si un producto tiene menos de 400 unidades y enviar una alerta. """

import time
import random

# Create a dict as a virtual warehouse with the initial products
productos= {"vasos": {"units": 0, "made": "Chile" },
            "cucharas": {"units": 0, "made": "Chile" }, 
            "cuchillos": {"units": 0, "made": "Chile" },
            "tenedores": {"units": 0, "made": "Chile" },
            }


#Store new products or add units.
def add_products():
    while True:
        store=productos
        #Data will be entered by terminal.
        add_prod=input(' Ingrese nuevo producto: ').capitalize()
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
        # if storage_complete():
            return store 

##Add and decrease the units number per product.
# def rest_units():

##Remove products from the virtual warehouse.
# def remove_products():


#Display and return all products in the store.
def whole_warehouse (): 
    #if is
    print('6. Actualmente contamos con los siguientes productos:')
    #Go through each value in the data structure (dict).
    for key in productos.keys():
        print(f"{key}: {productos[key]}")
        time.sleep(1)
#Call function.            
whole_warehouse ()