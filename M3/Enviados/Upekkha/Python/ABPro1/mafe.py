
MENU = {'chorrillana' ,'chacarero','completo','terremoto','mojito'}
PRICES = {'chorrillana' : 22000,'chacarero': 7000,'completo': 6000,'terremoto':15000,'mojito': 20000}


def get_order():
        current_order = []
        while True:
            print("¿Qúe deseas pedir?")
            order = input()
            if order in MENU:
                current_order.append(result)
                print(f"¿Cuántas/os {order} deseas?")
                units= int(input())
                if units >0:
                    receipt_list = []
                    for name in PRICES.keys():
                        price = (PRICES[name])
                        if name == order:
                            result = int(price) * units
                            receipt_list.append(result)                             
            else:
                print("Lo sentimos. No contamos con ese producto")
                continue
            if is_order_complete():
                return current_order

def is_order_complete():
        print("¿Deseas algo más? si/no")
        choice = input()
        if choice == "no":      
            return True        
        elif choice == "si":
            return False
        else:
            print("Respuesta inválida") 
            
def main():
    order = get_order()
    output_order(order)
    print("Please drive through to the second window.")


if __name__ == "__main__":
    main()
"""
        
def output_order(order_list):
    print("Okay, so you want")
    for order in order_list:
        print(order)

def get_receipt(): 
        for receipt_list in get_order():
            percIVA= 19
            subtotal= sum(receipt_list) #no sé donde poner esto 
            iva= subtotal * (percIVA / 100) 
            precioplussIva= subtotal + iva
            print("Total: ${}".format(subtotal))
            print("IVA: ${}".format(iva))
            print("Total con IVA: ${}".format(precioplussIva))
 """

