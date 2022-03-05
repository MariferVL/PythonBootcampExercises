""" En esa ocasión se solicita un programa que:
- Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario. 
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos. 
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar 
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir 
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’. """

import re
import time

print("")
print ('1. Programa para loguear usuarios')

users={}

#Identify customer.
def sign_in():
    user_name= input('Ingrese Nombre de Usuario:  ').capitalize ()
    print(f'¡Bienvenid@ {user_name}!')
    print('')
    return user_name

def user_age():
    i=0
    while i<3:
        i+=1
        print('Ingrese su edad (Sólo dígitos):')
        age= input()
        try:
            # Convert it into integer
            val = int(age)
            print(f'Edad ingresada correctamente: {val}')
            print('')
            return age
        except ValueError:
            print("Debes ingresar sólo números.")
        if i==3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte.")
            return continue_or_exit()

# def user_age():
#     i=0
#     while i<3:
#         i+=1
#         print('Ingrese su edad')
#         age= int(input('(Sólo dígitos)  '))
#         if age is int:
#             print("Edad ingresada correctamente.")  
#             return age
#         elif age not is int:
#             print("Debes ingresar sólo números.")
#         elif i==3:
#             print("Se acabaron tu número de intentos.")
#             print("Vuelve a registrarte.")

def password_validation():
    val=False
    i=0
    print('Ahora crea tu contraseña.')
    print('Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
    while i<4 and val==False:
        i+=1
        if i==4:
            print("Se acabaron tu número de intento.")
            print("Vuelve a registrarte.")
            break
        password= input('Crear Contraseña:  ')
        if len(password) < 8:
            print('Recuerda que son mínimo 8 caracteres')
            val = False
        if len(password) > 11:
            print('Recuerda que son máximo 11 caracteres')
            val = False
        if not re.search("[0-9]", password):
            print('No olvides incluir al menos un número.')
            val = False
        if not re.search("[A-Z]", password):
            print('No olvides incluir al menos una letra en Mayúscula.')
            val = False
        if not re.search("[a-z]", password):
            print('No olvides incluir al menos una letra en minúscula.')
            val = False
        return password


def continue_or_exit():
    print("¿Qué desea hacer? Salir/Continuar: ")
    answer = input().capitalize ()
    if answer == "Salir":
        return True
    elif answer == "Continuar":
        return False
    else:
        print("Respuesta Inválida")


def updated_users(users_dict):
    print("Los usuarios registrados son:")
    for user in users_dict.keys():
        print(user+': \n       edad:',users_dict[user]['age']+', contraseña:',users_dict[user]['password'])
        time.sleep(0.5)


def main():
    name = sign_in()
    age= user_age()
    password=password_validation()
    users[name]= {'age': age, 'password': password}
    print(users)
    print('')
    print('¡Usuario creado con éxito!')
    print('')
    if continue_or_exit() ==False:
        sign_in()
    updated_users(users)
    print('')
    print("Programa Finalizado")

if __name__ == "__main__":
    main()