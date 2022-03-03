""" DESARROLLO
OPCIÓN 1:
    Elaborar un programa que:
        Crear un usuario, este debe ingresar una contraseña.
            contraseña:
                acorde a criterios de seguridad
                al menos 8 caracteres: mayúsculas+ minúsculas + cifras.
                Indicar a usuario  criterios faltantes para contraseña segura.
                programa envía un mensaje con los criterios no cumplidos.

"""

import re

def sign_in(password):
    print('Bienvenido a Comprando Presentes')
    print('Ahora creemos tu usuario')
    print("Introduce tu nombre:")
    user = input()
    user_cap= user.capitalize()
    print(f'Bienvenida {user_cap}! Ahora crea tu clave.')
    print('Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
    password= input('Crear Clave: ')
    val = True
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

def main():
    password = 'Marifer1111'

    if (sign_in(password)):
        print("Clave creada exitosamente!")
    else:
        print("Clave inválida!")

if __name__ == '__main__':
    main()

