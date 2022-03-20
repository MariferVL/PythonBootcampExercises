""" Sistema de envío """
from Clientes import costumer_menu

Bodega_A={'Ama':{'product': 'helado', 'units': 100, 'address': 'Viña'}, 
            'PAm':{'product': 'helado', 'units': 35, 'address': 'Viña'},
            'Love':{'product': 'helado', 'units': 89, 'address': 'Viña'},
            'Alma':{'product': 'helado', 'units': 34, 'address': 'Viña'},} 

Bodega_B={
    'Pepa':{'product': 'paltas', 'units': 100, 'address': 'Viña'},
    'Jose':{'product': 'paltas', 'units': 230, 'address': 'Viña'},
    'Tonto':{'product': 'paltas', 'units': 34, 'address': 'Viña'},
    'Pol':{'product': 'paltas', 'units': 50, 'address': 'Viña'},
    'Marcos':{'product': 'paltas', 'units': 80, 'address': 'Viña'},
}
Bodega_Auxiliar= {}

#Chose between Long-distance or Short-distance Shipping depending on distance in km.
def shipping(bag):
    print("\nDespacho: \n")
    for item in bag.keys():
        print(f'{item}: ')    
        # Distance will be entered by terminal.
        print("> Ingrese dirección de despacho:")
        print("(Calle, Número, Población, Ciudad, Región y País)")
        address= input("")
        # Distance will be entered by terminal.
        print("> Ingrese Kilometros de distancia")
        distance= int(input("(Sólo dígitos):    "))
        if distance <= 1000:
            check_warehouse(Bodega_A,bag)
            print(f" {distance} Km: Le corresponde despacho 'Short-D'")
            print("Proceso de despacho iniciado")
            print("Gracias por comprar Presentes.")
            return Bodega_A,costumer_menu()
        elif distance > 1000:
            check_warehouse(Bodega_B,bag)
            print(f" {distance} Km:Le corresponde despacho 'Long-D'")
            print("Proceso de despacho iniciado")
            print("Gracias por comprar Presentes.")
            Bodega_B[item]={'product': bag[item]["product"], 'units': bag[item]["units"], 'address': address } 
            return Bodega_B,costumer_menu()


def check_warehouse(warehouse,bag):
    for item in bag.keys():
        for prod, info in warehouse.items():
            if 'units' in info.values():
                print(warehouse[prod]['units'])
                sum = warehouse[prod]['units'] + sum
                print(sum)
                if sum < 500:
                    warehouse[item]={'product': bag[item]["product"], 'units': bag[item]["units"], 'address': address } 
                    return warehouse
                else: 
                    print(f"Limite Alcanzado en Bodega.")
                    print("Parcel será enviada momentaneamente a Bodega Auxiliar")
                    print("Proceso de despacho iniciado")
                    print("Gracias por comprar Presentes.")
                    Bodega_Auxiliar[item]={'product': bag[item]["product"], 'units': bag[item]["units"], 'address': address } 
                    return Bodega_Auxiliar, costumer_menu()

