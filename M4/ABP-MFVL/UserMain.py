from Users import Users


def main ():
    print("Bienvenido a Comprando Presente")
    print ("¿Qué deseas hacer?")
    print("")
    print(" Resgistrarme -> 1 /n Ingresar a cuenta -> 2 /n Comprar -> 3 /n Eliminar Cuenta -> 4 /n Solicitud/Reclamo -> 5 ")
    print("")
    answer= int(input("Ingrese sólo el número:"))
    if answer == 1:
        Users.sign_up()
    elif answer == 2:
        Users.log_in() 
    elif answer == 3:
        return 
    elif answer == 4:
        Users.delete_user 
    elif answer == 5:
        Users.contact_us 
    else:
        print("Respuesta Inválida")
        #Start function again.
        main ()


if __name__ == "__main__":
        main()