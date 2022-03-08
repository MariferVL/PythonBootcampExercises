#Sistema de envío 

from Bodega import *
from Clientes import *

Bodega_A={}
Bodega_B={}

#Chose between Long or Express Shipping depending on distance in km.
def shipping():
    # Distance will be entered by terminal.
    print("Ingrese dirección de envío:")
    print("(Calle, Número, Población, Ciudad, Región y País)")
    address= input("")
    # Distance will be entered by terminal.
    print("Ingrese número de Kilometros de distancia")
    distance= int(input("(Sólo dígitos)   "))
    if distance <= 1000:
        print(f" {distance}Km: Le corresponde Envío Rápido")
        
    elif distance >= 1000:
        print(f" {distance}Km:Le corresponde Envío Largo")

def shipping_warehouse():
    if len(Bodega_A) == 500:
        print("Limite Alcanzado en Bodega de Envíos Rápidos")
        print("No se pueden ingresar más pedidos.")
    if len(Bodega_B) == 500:
        print("Limite Alcanzado en Bodega de Envíos Largos")
        print("No se pueden ingresar más pedidos.")



