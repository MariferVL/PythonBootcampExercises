
#Import the re module, which can be used to work with Regular Expressions.
import re
from Venta import log_in


#Create an empty dictionary.
users={'Tamara':{'name': 'Tamara', 'surname': 'Neira', "age": 35, "gender": "F", "password": "LocaLoca15" , "email": "tam@presentes.com", "contact": 987654321,"joinDate": "15/11/1986" },
'Pau':{'name': 'Paula', 'surname': 'Ramirez',"age": 24, "gender": "F", "password": "laliR820" , "email": "pau@presentes.com", "contact": 912345678, "joinDate": "08/01/1998"},
'Flo':{'name': 'Florencia', 'surname': 'Miralla',"age": 28, "gender": "F", "password": "Flor3c3r" , "email": "flo@presentes.com", "contact":923456789, "joinDate":"31/01/1994" },
'Marete':{'name': 'Mario', 'surname': 'Sonrisa',"age": 35, "gender": "M", "password": "Marete1135" , "email": "marete@presentes.com", "contact":934567891, "Mechadenac": "06/11/1984" },
'Dany':{'name': 'Daniel', 'surname': 'Vargas',"age": 24, "gender": "M", "password": "Gemini33" , "email": "dany@presentes.com", "contact":945678912, "joinDate": "19/07/1999"},
'Ama':{'name': 'Amanel', 'surname': 'LaVida',"age": 35, "gender": "F", "password": "AmaVida11" , "email": "ama@presentes.com", "contact":956789123, "joinDate": "11/11/1986"},
'Upek':{'name': 'Sam', 'surname': 'Ecuánime',"age": 35, "gender": "M", "password": "Upekkha33" , "email": "sam@presentes.com", "contact":967891234, "joinDate": "22/11/1986"},
}


#Program to add new customers.
#Step 2: Add user.
def sign_in():
    user_name= input('Cree su Nombre de Usuario:  ').capitalize ()
    print(f'¡Bienvenid@ {user_name}!')
    #Spacing sentences so my teacher doesn't go into OCD. LOL
    print('')
    return user_name

def user_name():
    print('Ahora ingresa tu:')
    name=input("Nombre: ").capitalize ()
    return name

def user_surname():
    print('Ahora ingresa tu:')
    surname=input("Apellido: ").capitalize ()
    return surname

def user_contact():
    i=0
    #Start a loop with 3 chances to write their contact following instructions.
    while i<3:
        i+=1
        print('Ingrese tu número de contacto (Sólo dígitos):')
        contact= input()
        #The try block lets you test a block of code for errors.
        try:
            # Convert it into integer
            val = int(contact)
            print(f'Número ingresado correctamente: {val}')
            print('')
            return contact
        #The except block lets you handle the error. 
        # Execute a special block of code for a special kind of error: "ValueError".
        except ValueError:
            print("Debes ingresar sólo números.")
        if i==3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte.")
            return continue_or_exit()

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
    print("> Agregar Usuario (A)")
    print("> Eliminar Usuario (E)")
    print("> Comprar (C)")
    print("> Salir (S)")
    answer = input("A|E|S: ").capitalize ()
    if answer == "S":
        return True
    elif answer == "A":
        return False
    elif answer == "E":
        return delete_user(users)
    elif answer == "C":
        return log_in()
    else:
        print("Respuesta Inválida")
        #Start function again.
        continue_or_exit()

#Step 6: Delete user by username/id.
def delete_user(user_dict):
    i=0
    while i <3:
        i+=1
        print("Ingrese el nombre de usuario del cliente a eliminar:")
        d_user=input().capitalize ()
        if d_user in user_dict:
            user_dict.pop(d_user)
            return user_dict,continue_or_exit() 
        elif d_user not in user_dict:
            print("")
            print(f"{d_user} ya había sido eliminado.")
            return continue_or_exit()
        if i==3:
            print("Se acabaron tu número de intentos.")
            return continue_or_exit()


#Step 7: Display registered users.
def updated_users(users_dict):
    print("Los usuarios registrados son:")
    print("")
    for user in users_dict.keys():
        print(user+': Nombre y Apellido:',users_dict[user]['name'],
        users_dict[user]['surname'],'\n      | Edad:',users_dict[user]['age'],
        '| Contraseña:',users_dict[user]['password'],
        '\n      | Contacto:',users_dict[user]['contact'])
        print("")


#Step 1/8: Start/end the whole program.
def main():
    val=False
    while val==False:
        user_nickname = sign_in()
        name=user_name()
        surname=user_surname()
        contact=user_contact()
        age= user_age()
        password=password_validation()
        # Save user info in users dict.
        users[user_nickname]= {'name': name, 'surname': surname, 
                                'age': age, 'password': password,
                                'contact': contact}
        if continue_or_exit():
            val=True
    updated_users(users)
    print('')
    print("Programa Finalizado")

if __name__ == "__main__":
    main()



#Next time add: print(user+': Nombre y Apellido:',users_dict[user]['name'],
# users_dict[user]['surname'],'|\n      Edad:',users_dict[user]['age'],
# '| Contraseña:',users_dict[user]['password'],'|\n      Email:',
# users_dict[user]['email'],'| Contacto:',users_dict[user]['contacto']