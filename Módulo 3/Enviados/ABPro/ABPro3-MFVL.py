# DESARROLLO:
    # Crear y agregar sentencias que nos permitan manipular un stock de productos. 
        #  Definir stock de un producto en una variable. 
        #  Solicitar stock disponible del producto por consola.
                # Almacenar en nueva variable ‘Productos seleccionados’.
        # No se pueden solicitar más de 20 unidades en un mismo pedido.
        # Entregar una unidad extra por compra > 12 unidades. 
            # Verificar que el stock posibilite entregar una unidad extra. 
            # Sino se entregan las unidades justas.
        # Productos reubicados serán descontados del stock inicial. 
        # Cada accion debe imprimir mensaje explicando lo realizado.
        # Si valor ingresado es superior a stock disponible:
            #Entregar mensaje indicando que no es posible 
            # realizar esta acción debido a que no hay stock suficiente.
    # * El código debe estar debidamente comentado para asegurar su comprensión

menu = {
    'chacarero': {'price': 5500, 'units': 0},
    'terremoto': {'price': 15000, 'units': 0},
    'completo': {'price': 3500, 'units': 0},
    'mojito': {'price': 5000, 'units': 0},
    'chorrillana': {'price': 18000, 'units': 0}
}

inventory= {
    'chacarero': 45,
    'terremoto': 66, 
    'completo': 77,
    'mojito': 0,
    'chorrillana': 12
}

def get_inventory():
    print('Ingrese producto a consultar')
    selected_product= input().lower()
    if selected_product in inventory.keys():
        unit= int(inventory[selected_product])
        print('Ingrese la cantidad')
        quantity_prod= int(input())
        if 0<quantity_prod<21:
            if quantity_prod >12:
                quantity_prod +=1
        if unit >= quantity_prod:
            if unit > 0:
                print(f'Hay {unit} unidades de {selected_product} en bodega.')
                inventory[selected_product]=inventory[selected_product]- quantity_prod
                print(f'Ahora tenemos {inventory[selected_product]} ')
            elif unit == 0:
                print(f'{selected_product.capitalize()} está agotado.')  
        
        else:
            print('No hay productos suficientes para abastecer su pedido')
    else:
        print(f'No contamos con {selected_product} en bodega.')

get_inventory()
