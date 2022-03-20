

def main ():
    print("Gracias por ser parte de la familia Upekkha.")
    print ("¿Qué deseas hacer?")
    print("")
    print(" Resgistrarme -> 1 /n Ingresar a cuenta -> 2 /n Comprar -> 3 /n Eliminar Cuenta -> 4 /n Solicitud/Reclamo -> 5 ")
    print("")
    answer= int(input("Ingrese sólo el númro:"))
    if answer == 1:
        return
    elif answer == 2:
        return
    elif answer == 3:
        return False
    elif answer == 4:
        return False
    elif answer == 5:
        return 
    else:
        print("Respuesta Inválida")
        #Start function again.
        main ()


if __name__ == "__main__":
        main()