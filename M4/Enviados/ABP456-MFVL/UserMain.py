from Users import *

customer={}

def main():
    print("\t\n ¡Bienvenido a Comprando Presentes!\n")
    print ("¿Eres Cliente o TeamNow?")
    print("> Cliente 1 \n> TeamNow 2\n> Salir 3")
    answer= int(input("> Ingrese sólo el número:"))
    if answer == 1:
        customer_menu()
    elif answer == 2:
        Users.log_in() 
    elif answer == 3:
        print("\n\t Gracias por visitar Comprando Presentes.")
        print("\t\t ¡Disfruta tu día! \n")
    else:
        print("Respuesta Inválida")
        #Start function again.
        main ()


def customer_menu():
    print ("\n¿Qué deseas hacer?")
    print("> Resgistrarme 1 \n> Ingresar 2 \n> Comprar 3 \n> Eliminar Cuenta 4 \n> Solicitud/Reclamo 5 \n> Salir 6 ")
    answer= int(input("> Ingrese sólo el número:"))
    if answer == 1:
        Customer.sign_up()
    elif answer == 2:
        Customer.log_in() 
    elif answer == 3:
        return 
    elif answer == 4:
        Customer.delete_user 
    elif answer == 5:
        Customer.contact_us 
    elif answer== 6:
        print("\n\t Gracias por ser parte de Comprando Presentes.")
        print("\t\t ¡Disfruta tu día! \n")
    else:
        print("Respuesta Inválida")
        #Start function again.
        main ()

def company_menu():
    print("\n\t ¡Bienvenid@ a tu Jornada Laboral!")
    print("\t\t Mucho ánimo para este nuevo presente. \n")
    print("¿Qué desea hacer?")
    print("> Agregar Nuevo Producto o Stock (A) \n> Restar Stock por Producto (R) \n> Eliminar Producto (E) \n> Inventario (I) \n> Registro Usuarios (U) \n> Salir (S)")
    answer = input("A|R|E|I|U|S: ").capitalize()
    if answer == "S":
        print("\n\t Gracias por ser parte de Comprando Presentes.")
        print("\t\t ¡Disfruta tu día! \n")
    elif answer == "A":
        True
        # add_products()==True
    elif answer == "R":
        True
        # rest_units()==True
    elif answer == "E":
        True
        # remove_products()==True
    elif answer == "I":
        True
        # whole_warehouse()==True
    elif answer == "U":
        True
        # updated_users()==True
    else:
        print("Respuesta Inválida")
        company_menu()


if __name__ == "__main__":
        main()
        print(Greatest.mro())