def password_check(password):
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
    if len(password) > 11:
        print('Recuerda que son máximo 11 caracteres')
        val = False
    if not any(char.isdigit() for char in password):
        print('No olvides incluir al menos un número.')
        val = False
    if not any(char.isupper() for char in password):
        print('No olvides incluir al menos una letra en Mayúscula.')
        val = False
    if not any(char.islower() for char in password):
        print('No olvides incluir al menos una letra en minúscula.')
        val = False
    if val:
        return val

# Main method


def main():
    password = 'Marifer1111'

    if (password_check(password)):
        print("Clave creada exitosamente!")
    else:
        print("Clave inválida!")



if __name__ == '__main__':
    main()
