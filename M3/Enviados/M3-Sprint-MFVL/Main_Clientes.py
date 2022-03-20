from Clientes import *
from Venta import *

# Customer menu options.
def costumer_menu():
    print("¿Qué desea hacer?")
    print("> Agregar Usuario (A)")
    print("> Eliminar Usuario (E)")
    print("> Comprar (C)")
    print("> Salir (S)")
    answer = input("A|E|C|S: ").capitalize ()
    if answer == "S":
        print("\n\t Gracias por ser parte de Comprando Presentes.")
        print("\t\t ¡Disfruta de tu día! \n")
    elif answer == "A":
        save_user()
    elif answer == "E":
        delete_user()
    elif answer == "C":
        log_in()
    else:
        print("Respuesta Inválida \n")
        #Start function again.
        costumer_menu()

#Drive code
# Start/end Customer program.
if __name__ == "__main__":
    costumer_menu()