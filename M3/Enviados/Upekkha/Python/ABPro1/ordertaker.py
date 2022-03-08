Menu = {
    'chacarero': {'price': 5500, 'units': 0},
    'terremoto': {'price': 15000, 'units': 0},
    'completo': {'price': 3500, 'units': 0},
    'mojito': {'price': 5000, 'units': 0},
    'chorrillana': {'price': 18000, 'units': 0}
}

# preguntar al usuario que es lo que quiere

# def get_order():
while True:
    
    print('¿Qúe deseas pedir?')
    order = input()
    if order in Menu.keys():
        units = input(f'¿Cuántas/os {order} deseas?')
        Menu[order]['cantidad'] = int(units)
    else:
        print('Lo sentimos. No contamos con ese producto.')
        extra_order= input('¿Deseas algo más?') 
        if extra_order == 'no':
            print(Menu)
            break
        if extra_order == 'si':
            continue
        continue
    extra_order = input('¿Desea algo más?') 
    if extra_order == 'no':
        print(Menu) #TO-DO: borrar esto luego
        break
    if extra_order == 'si':
        continue

def output_order():
    for product in Menu.keys():
        prod_units= Menu[product]['units'] 
        prod_total= Menu[product]['price']
        if Menu[product]['units'] != 0:
            print(f'Entonces su pedido final es: {prod_units} {product}: {prod_units} * {prod_total}')

# def get_receipt():
#         for receipt_list in get_order():
#             percIVA= 19
#             subtotal= sum(int(receipt_list)) 
#             iva= subtotal * (percIVA / 100) 
#             precioplussIva= subtotal + iva
#             print("Total: ${}".format(subtotal))
#             print("IVA: ${}".format(iva))
#             print("Total con IVA: ${}".format(precioplussIva))





