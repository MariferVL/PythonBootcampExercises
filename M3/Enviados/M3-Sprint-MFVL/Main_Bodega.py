from Bodega import *
from Clientes import updated_users

# Warehouse menu options.
def menu():
    print("¿Qué desea hacer?")
    print("> Agregar Nuevo Producto o Stock (A)")
    print("> Restar Stock por Producto (R)")
    print("> Eliminar Producto (E)")
    print("> Inventario (I)")
    print("> Registro Usuarios (U)")
    print("> Salir (S)")
    answer = input("A|R|E|I|U|S: ").capitalize ()
    if answer == "S":
        print("\n\t Gracias por ser parte de Comprando Presentes.")
        print("\t\t ¡Disfruta de tu día! \n")
    elif answer == "A":
        add_products()==True
    elif answer == "R":
        rest_units()==True
    elif answer == "E":
        remove_products()==True
    elif answer == "I":
        whole_warehouse()==True
    elif answer == "U":
        updated_users()==True
    else:
        print("Respuesta Inválida")
        menu()

#Drive code
#Start/end the Warehouse program.
if __name__ == "__main__":
    stock_alert()
    menu()