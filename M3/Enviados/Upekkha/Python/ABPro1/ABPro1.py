"""Definir un listado de 5 productos con su respectivo valor unitario. (paltas: 30, tomates:50, churrascos: 45, mayonesa: 6, chucrut: 4)
● Crear un archivo .py el cual deberá solicitar ingresar una cantidad por cada producto 
(definido de la lista).
● Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto.
● Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado.
● Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA)."""


PRECIOS = {'chorrillana' : 22000,'chacarero': 7000,'completo': 6000,'terremoto':15000,'mojito': 20000}

print("¿Cuánt@s  desea?")
cant= int(input())

shares = input('How many shares? ')
stock = input('What\'s the stock? ')

for name in PRECIOS.keys():
    precio = (PRECIOS[name])
    if name == cant:
        result = int(precio) * cant
        percIVA= 19
        iva= result * (percIVA / 100) 
        precioplussIva= result + iva
        print("Total: ${}".format(result))
        print("IVA: ${}".format(iva))
        print("Total con IVA: ${}".format(precioplussIva))


"""chorr= 22000 
chac= 7000 
comp= 6000
terr= 15000
moj= 20000 """


# print("¿Cuántas chorrillanas desea?")
# chorrCant= int(input())
# print("¿Cuántos chacareros desea?")
# chacCant= int(input())
# print("¿Cuántos completos desea?")
# compCant= int(input())
# print("¿Cuántos terremotos desea?")
# terrCant= int(input())
# print("¿Cuántos mojitos desea?")
# mojCant= int(input())

"""result= chorr*chorrCant + chac*chacCant + comp*compCant + terr*terrCant +  moj*mojCant
percIVA= 19
iva= result * (percIVA / 100) 
precioplussIva= result + iva
print("Total: ${}".format(result))
print("IVA: ${}".format(iva))
print("Total con IVA: ${}".format(precioplussIva))"""
