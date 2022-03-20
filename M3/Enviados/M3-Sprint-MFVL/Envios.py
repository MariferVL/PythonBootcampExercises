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
    print("Despacho: \n")
    parcel={}
    for item in bag.keys():
        print(f'{item}: ')    
        # Distance will be entered by terminal.
        print("> Ingrese dirección de despacho:")
        print("(Calle, Número, Población, Ciudad, Región y País)")
        address= input("")
        # Distance will be entered by terminal.
        print("\n> Ingrese Kilometros de distancia")
        distance= int(input("(Sólo dígitos):    "))
        parcel[item]={'product': bag[item]["product"], 'units': bag[item]["units"], 'address': address }
        if distance <= 1000:
            check_warehouse(parcel,Bodega_A)
            print(f" {distance} Km: Le corresponde despacho 'Short-D'")
            print("\n\tCompra en camino.")
            print("\t\t¡Gracias por comprar Presentes! \n")
            return Bodega_A,costumer_menu()
        elif distance > 1000:
            check_warehouse(parcel,Bodega_B)
            print(f" {distance} Km:Le corresponde despacho 'Long-D'")
            print("\n\tCompra en camino.")
            print("\t\t¡Gracias por comprar Presentes! \n")
            return Bodega_B,costumer_menu()


def check_warehouse(parcel,bodega):
    for item in parcel.keys():
        for prod, info in bodega.items():
            if 'units' in info.values():
                print(bodega[prod]['units'])
                sum = bodega[prod]['units'] + sum
                print(sum)
                if sum < 500:
                    return bodega
                else: 
                    print("Limite Alcanzado en Bodega.")
                    print("Parcel será enviada momentaneamente a Bodega Auxiliar")
                    print("\t\t¡Gracias por comprar Presentes! \n")
                    Bodega_Auxiliar[item]={'product': parcel[item]["product"], 'units': parcel[item]["units"], 'address': parcel[item]["address"] } 
                    return Bodega_Auxiliar, costumer_menu()

