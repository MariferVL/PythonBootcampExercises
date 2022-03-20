""" Información clientes """

# Import the re module, which can be used to work with Regular Expressions.
import re
import datetime
from Main_Clientes import costumer_menu
from Bodega import *
from Envios import shipping

# Create a dictionary of users/customers info.
users = {'Tamara': 
                {'name': 'Tamara', 
                'surname': 'Neira', 
                "age": 35, 
                "gender": "F", 
                "password": "LocaLoca15", 
                "email": "tam@presentes.com", 
                "contact": 987654321, 
                "joinDate": "15/11/1986"},
        'Pau': 
                {'name': 'Paula', 
                'surname': 'Ramirez', 
                "age": 24, 
                "gender": "F", 
                "password": "laliR820", 
                "email": "pau@presentes.com", 
                "contact": 912345678, 
                "joinDate": "08/01/1998"},
        'Flo': 
                {'name': 'Florencia', 
                'surname': 'Miralla', 
                "age": 28, 
                "gender": "F", 
                "password": "Flor3c3r", 
                "email": "flo@presentes.com", 
                "contact": 923456789, 
                "joinDate": "31/01/1994"},
        'Marete': 
                {'name': 'Mario', 
                'surname': 'Sonrisa', 
                "age": 35, 
                "gender": "M", 
                "password": "Marete1135", 
                "email": "marete@presentes.com", 
                "contact": 934567891, 
                "joinDate": "06/11/1984"},
        'Dany': 
                {'name': 'Daniel', 
                'surname': 'Vargas', 
                "age": 24, 
                "gender": "M", 
                "password": "Gemini33", 
                "email": "dany@presentes.com", 
                "contact": 945678912, 
                "joinDate": "19/07/1999"},
        'Ama': 
                {'name': 'Amanel', 
                'surname': 'LaVida', 
                "age": 35, 
                "gender": "F", 
                "password": "AmaVida11", 
                "email": "ama@presentes.com", 
                "contact": 956789123, 
                "joinDate": "11/11/1986"},
        'Upek': 
                {'name': 'Sam', 
                'surname': 'Ecuánime', 
                "age": 35, 
                "gender": "M", 
                "password": "Upekkha33", 
                "email": "sam@presentes.com", 
                "contact": 967891234, 
                "joinDate": "22/11/1986"},
        }


# Program to add new customers.
# Step 1: Add user full name.
def sign_in():
    print("\n Registro de Usuarios: \n")
    user_name = input('> Cree su Nombre de Usuario:  ').capitalize()
    print(f'\n\t ¡Bienvenid@ {user_name}!')
    # Spacing sentences so my teacher doesn't go into OCD. LOL
    print('')
    return user_name


def user_name():
    print('\n> Ahora ingresa tu:')
    name = input("   Nombre: ").capitalize()
    return name


def user_surname():
    print('\n> Ahora ingresa tu:')
    surname = input("   Apellido: ").capitalize()
    return surname

# Step 2: Add and validate numbers.
def check_int(number):
    i = 0
    # Start a loop with 3 chances to write their contact following instructions.
    while i < 3:
        i += 1
        # The try block lets you test a block of code for errors.
        try:
            # Convert it into integer
            val = int(number)
            print(f'Ingresado correctamente: {val}')
            return number
        # The except block lets you handle the error.
        # Execute a special block of code for a special kind of error: "ValueError".
        except ValueError:
            print("Debes ingresar sólo números. \n")
        if i == 3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte. \n")
            costumer_menu()

# Step 3: Add and validate password.
def password_validation():
    i = 0
    print('\n> Crea tu contraseña.')
    print('   Debe contener entre 8 y 11 caracteres incluyendo mayúsculas, minúsculas y números.')
    # Start a loop with 3 chances to write their password following instructions.
    while i < 3:
        i += 1
        password = input('Crear Contraseña:  ')
        val = True
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
        # Leave the loop.
        elif val:
            print('\n ¡Usuario creado con éxito! \n')
            return password
        if i == 3:
            print("Se acabaron tu número de intentos.")
            print("Vuelve a registrarte.\n")
            costumer_menu()

def save_user():
        user_nickname = sign_in()
        name=user_name()
        surname=user_surname()
        print('\n> Ingrese tu número de contacto (Sólo dígitos):')
        contact = input()
        contact=check_int(contact)
        print('\n> Ingrese su edad (Sólo dígitos):')
        age = input()
        age= check_int(age)
        password=password_validation()
        join_date =datetime.datetime.now().strftime("%d/%m/%Y")
        # Save user info in users dict.
        users[user_nickname]= {'name': name, 'surname': surname, 
                                'age': age, 'password': password,
                                'contact': contact, 'joinDate': join_date}
        print(f'\t¡Bienvenido a la familia Presente, {user_nickname}! ')
        print(f'\n Los datos ingresados son: {users[user_nickname]} \n')
        return users, costumer_menu()

# Delete user by username/id.
def delete_user():
    print("\nEliminacón de Usuarios: \n")
    print("\t Ingrese nombre de usuario de la cuenta a eliminar:")
    d_user = input().capitalize()
    if d_user in users.keys():
        i=0
        while i < 3:
            i += 1
            password= input('> Ingrese su contraseña:')
            if password == users[d_user]['password']:
                remove = users.pop(d_user)
                print(f"\n>  {d_user}:{remove} ha sido eliminado. \n")
                return users, costumer_menu()
            else:
                print('Contraseña Incorrecta \n')
            if i == 3:
                print("Se acabaron tu número de intentos.")
                print("Vuelve a registrarte.\n")
                costumer_menu()
    else:
        print(f"\n{d_user} no está registrado. \n")
        costumer_menu()

# Updated Users info available only to employees.
# Display registered users using employee ID.
def updated_users():
    i=0
    while i < 3:
        i += 1
        employeeId = input("Ingrese su ID:")
        print(f"\n ¡Bienvenido {employees[employeeId]['name']}!")
        if employeeId in employees.keys():
            print("\n Los usuarios registrados son: \n")
            for user in users.keys():
                print(f"\t {user}: Nombre y Apellido: {users[user]['name']} {users[user]['surname']} \n      \t\t| Edad: {users[user]['age']} | Contraseña: {users[user]['password']}\n      \t\t| Contacto: {users[user]['contact']} \n      \t\t| Fecha de Registro: {users[user]['joinDate']} \n")
            return 
        else:
            print(f"\n{employeeId} no está registrado.")
        if i == 3:
            print("Se acabaron tu número de intentos. \n")
    

Bag={}
#Initiating shopping program.
#Step 2: Request purchase by customer id, product id and the units (1 by default) to buy.
#Identify customer.
def log_in():
    username= input('> Ingrese su Nombre de Usuario/ID:  ').capitalize()
    if username in users.keys():
        print(f'\n\t\t!Bienvenid@ {username}!\n')
        return username
    elif username not in users.keys():
        print("Aún no estás registrad@.")           
        print("Lo dirigiremos a sección Registro.\n")
        return save_user()

def fill_bag(user):
    #Display on terminal store products available.
    print("Nuestros productos disponibles son: ")
    for name in productos.keys():
        print(f'>{name}')
    print('> Ingresa el producto a comprar: ')
    to_bag= input().capitalize()
    print('\n> Ingresa unidades a comprar: (Sólo dígitos) ')
    units= int(input())
    Bag[user]= {'product': to_bag , 'units': units} 
    return Bag


#Step 3: Confirm if required product has stock.
def check_stock(bag):
    #Iterate through dict.
    for user in bag.keys():   
        product=bag[user]['product']
        if product in productos.keys():
            if productos[product]['units'] >= bag[user]['units']: 
                print(f'\nTu producto {product} a sido agregado a tu carrito de compras.\n')
                return bag, True
            elif  productos[product]['units'] < bag[user]['units']:
                print('\n Compra cancelada')
                print(f'Lo sentimos, no contamos con stock de {product} por el momento.\n')
                return costumer_menu()
        elif product not in productos:
            print('\n Compra cancelada')
            print(f'Lo sentimos, no contamos con stock de {product} por el momento.\n')
            return bag, False


#Step 4: Confirm if product in bag is product customer wants.
def confirm_purchase(final_bag):
    for item in final_bag.keys():
        print(f'{item}, su compra es: ')
        print(f'\t{final_bag[item]["product"]}: {final_bag[item]["units"]} unidades ')
        print('')
        answer= input('Si/No:  ').capitalize()
        if answer == "Sí" or "Si":
            print('\n¡Compra aprobada!')
            print(f'{item}, compruebe detalle de compra y boleta en su cuenta. \n')
            return final_bag,shipping(final_bag)
        elif answer == "No":
            print('Lo sentimos. Por favor, vuelve a realizar tu compra.')
            return costumer_menu()
        else:
            print("Respuesta inválida \n")

#Step 1/5: Start/end the whole program.
def main():
    user=log_in()
    i=0
    val=False
    while val==False:
        Bag = fill_bag(user)
        Bag, val = check_stock(Bag)
        i=i+1
        if i==3:
            print('Se agotaron sus intentos.')
            break
    if val==True:
        confirm_purchase(Bag)

