#Rodrigo:  No comenté los códigos que ya vengo usando 
# hace varios trabajos atrás para no ser tan riteratiba.

#Import the re module, which can be used to work with Regular Expressions.
import re
#Import the time module.
import time

#Spacing sentences so my teacher doesn't go into OCD. LOL
print("")
print ('1. Programa para loguear usuarios')

#Create an empty dictionary.
users={}

#Program to add new customers.
#Step 2: Add name.
def sign_in():
    user_name= input('Ingrese Nombre de Usuario:  ').capitalize ()
    print(f'¡Bienvenid@ {user_name}!')
    print('')
    return user_name

#Step 3: Add and validate age.
def user_age():
    i=0
    #Start a loop with 3 chances to write their age following instructions.
    while i<3:
        i+=1
        print('Ingrese su edad (Sólo dígitos):')
        age= input()
        #The try block lets you test a block of code for errors.
        try:
            # Convert it into integer
            val = int(age)
            print(f'Edad ingresada correctamente: {val}')
            print('')
            return age
        #The except block lets you handle the error. 
        # Execute a special block of code for a special kind of error: "ValueError".
        except ValueError:
            print("Debes ingresar sólo números.")
        if i==3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte.")
            return continue_or_exit()

#Step 4: Add and validate password.
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
            return continue_or_exit()

#Step 5: Ask continue adding users or exit.
def continue_or_exit():
    print("¿Qué desea hacer?")
    print("Continuar agregando usuario o Salir")
    answer = input("Salir/Continuar: ").capitalize ()
    if answer == "Salir":
        return True
    elif answer == "Continuar":
        return False
    else:
        print("Respuesta Inválida")
        #Start function again.
        continue_or_exit()

#Step 6: Display registered users.
def updated_users(users_dict):
    print("Los usuarios registrados son:")
    for i in range(3):
        for user in users_dict.keys():
            print(user+': \n       edad:',users_dict[user]['age']+', contraseña:',users_dict[user]['password'])
            time.sleep(0.5)

#Step 1/7: Start/end the whole program.
def main():
    val=False
    while val==False:
        name = sign_in()
        age= user_age()
        password=password_validation()
        # Save user info in users dict.
        users[name]= {'age': age, 'password': password}
        if continue_or_exit():
            val=True
    updated_users(users)
    print('')
    print("Programa Finalizado")

if __name__ == "__main__":
    main()