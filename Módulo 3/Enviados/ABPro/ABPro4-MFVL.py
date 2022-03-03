# DESARROLLO
# Problema:   Muchos usuarios comprando desesperadamente. 
#             Alto movimiento de proveedores que renuevan nuestro stock de productos a ofrecer. 
# Programa:
    # Almacenar stock de dos productos. 
    #     Primer producto tendrá 120 unidades.
    #     Segundo 150.
    # 'n' representa un número aleatorio entre 1 y 10. 
    # Cuando producto tenga stock < 100 unidades:
            #Enviar automáticamente 50 unidades más.
            #Reflejar en el stock de cada producto.
            #Proveedores con stock suficiente para enviar 150 unidades en total de productos 1 y 2.
    # Cada 3 segundos comprar “n” unidades de cualquiera de los dos productos.
    # Cada compra se debe descontar del stock inicial. 
    # Cada 10 compras
        #imprimir en pantalla: número de unidades disponibles por producto. 


import random
import time


inventory= {
    'Zero Limits': 120,
    'Mafalda': 150, 
}
supplier= 150

while True:
    for i in range(10):
        n= random.randint(1,10)
        selected_product= random.choice(list(inventory))
        if n <= inventory[selected_product]:
                print(f'Se han vendido {n} unidades de {selected_product}.')
                inventory[selected_product]=inventory[selected_product]- n
                time.sleep(0.5)
    if (inventory['Zero Limits']<100) and (supplier > 0):
        supplier= supplier-50
        inventory['Zero Limits'] = inventory['Zero Limits'] + 50
    if (inventory['Mafalda'] <100) and (supplier > 0):
        supplier= supplier-50
        inventory['Mafalda'] = inventory['Mafalda'] + 50
    if (inventory['Mafalda'] >0) or (inventory['Zero Limits'] >0):
        print (f'Ahora tenemos {[value for value in inventory.values()][0]} unidades de {[key for key in inventory.keys()][0]} y {[value for value in inventory.values()][1]} unidades de {[key for key in inventory.keys()][1]} ')

