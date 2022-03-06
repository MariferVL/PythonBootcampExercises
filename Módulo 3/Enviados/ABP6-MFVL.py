
import re
import time

#Spacing sentences so my teacher doesn't go into OCD.
print("")
print ('1. Programa para loguear usuarios')

users={}

#Identify new customer.
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


def password_validation():
    i=0
    print('Ahora crea tu contraseña.')
    print('Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
    while i <4:
        i+=1
        password= input('Crear Contraseña:  ')
        val=True
        if len(password) < 8:
            print('Recuerda que son mínimo 8 caracteres')
            val = False
        if len(password) > 11:
            print('Recuerda que son máximo 11 caracteres')
            val = False
        if not re.search("[0-9]", password):
            print('Debes incluir al menos un número.')
            val = False
        if not re.search("[A-Z]", password):
            print('Debes incluir al menos una letra en Mayúscula.')
            val = False
        if not re.search("[a-z]", password):
            print('Debes incluir al menos una letra en minúscula.')
            val = False
        elif val:
            print('')
            print('¡Usuario creado con éxito!')
            print('')
            return password
        if i==3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte.")
            return continue_or_exit()


def continue_or_exit():
    print("¿Qué desea hacer? Salir/Continuar: ")
    answer = input().capitalize ()
    if answer == "Salir":
        return True
    elif answer == "Continuar":
        return False
    else:
        print("Respuesta Inválida")
        continue_or_exit()


def updated_users(users_dict):
    print("Los usuarios registrados son:")
    for i in range(3):
        for user in users_dict.keys():
            print(user+': \n       edad:',users_dict[user]['age']+', contraseña:',users_dict[user]['password'])
            time.sleep(0.5)


def main():
    val=False
    while val==False:
        name = sign_in()
        age= user_age()
        password=password_validation()
        users[name]= {'age': age, 'password': password}
        # print(users)
        if continue_or_exit():
            val=True
    updated_users(users)
    print('')
    print("Programa Finalizado")

if __name__ == "__main__":
    main()