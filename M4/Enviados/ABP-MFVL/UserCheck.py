
import re

class UserCheck:
    #Add and validate user birth date.
    def check_int(input):
        i=0
        #Start a loop with 3 chances to write their age following instructions.
        while i<3:
            i+=1
            #The try block lets you test a block of code for errors.
            try:
                # Convert it into integer
                val = int(input)
                # print(f'Fecha ingresada correctamente: ')
                print('')
                return input
            #The except block lets you handle the error. 
            # Execute a special block of code for a special kind of error: "ValueError".
            except ValueError:
                print("Debes ingresar sólo números.")
            if i==3:
                print("Se acabaron tu número de intentos.")
                print("Vuelve a registrarte.")
                # return continue_or_exit()
        
    #Add and validate password.
    def password_validation():
        i=0
        print('Ahora crea tu contraseña.')
        print('Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
        #Start a loop with 3 chances to write their password following instructions.
        while i <3:
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
            #Leave the loop.
            elif val:
                print('')
                print('¡Usuario creado con éxito!')
                print('')
                return password
            if i==3:
                print("Se acabaron tu número de intentos.")
                print("Vuelve a registrarte.")
                # return continue_or_exit()

