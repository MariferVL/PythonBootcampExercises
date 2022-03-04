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
print("")

# def user_confirmation():
#     for id in user.keys():
#         if user_name== id:
#             print(f'!Bienvenid@ {user[user_name]}!')
#             print(f'{user[user_name]}, !')
#         elif user_name not in user.keys():
#             print("Aún no estás registrad@.Por favor, ingresa a Sing In.")  

users={}

#Identify customer.
def sign_in():
    while True:
        user_name= input('Ingrese Nombre de Usuario:  ')
        user_age= int(input('Ingrese su edad: (Sólo dígitos)  '))
        print(f'¡Bienvenid@ {user_name}! Ahora crea tu contraseña.')
        print('Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
        # user_password= input('Crear Contraseña:  ')
        user_password=password_validation()
        users[user_name]={'password': user_password, 'age': user_age}
                    
        if continue_or_exit():
            return users

def password_validation():
    val = True
    while val == True:
        for i in range(3):
            password= input('Crear Contraseña:  ')
            if len(password) < 8:
                print('Recuerda que son mínimo 8 caracteres')
                val = False
            elif len(password) > 11:
                print('Recuerda que son máximo 11 caracteres')
                val = False
            elif not re.search("[0-9]", password):
                print('No olvides incluir al menos un número.')
                val = False
            elif not re.search("[A-Z]", password):
                print('No olvides incluir al menos una letra en Mayúscula.')
                val = False
            elif not re.search("[a-z]", password):
                print('No olvides incluir al menos una letra en minúscula.')
                val = False
            elif val:
                return val
        print('Se agotaron sus intentos.')
        break

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
    for user in users_dict:
        print(user)


def main():
    users = sign_in()
    updated_users(users)
    print("Programa Finalizado")

if __name__ == "__main__":
    main()