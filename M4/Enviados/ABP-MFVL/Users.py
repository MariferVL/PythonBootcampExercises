from UserMain import main
from UserCheck import UserCheck

# n_users=0
#Empty list to add users info.
users={}
#Empty dict to add users info by age group for marketing purposes.
mktg={"greatest":[],
        "silent":[],
        "baby_Boomers":[],
        "gen_X": [],
        "xennials":[],
        "gen_Y":[],
        "gen_Z":[]}
                

# Parent class Users is declared.
class Users: 
    # instance attributes.
    def __init__(self,firstname,surname,ID,password,birthDay,birthMonth,birthYear, email, contact):
        # keys are initialized with their respective values
        self.firstname= firstname
        self.surname= surname
        self.ID= ID
        self.__password = password
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear 
        self.email= email
        self.contact = contact 

    # instance method
    def log_in(users):
        username= input('> Ingrese su Nombre de Usuario/ID:  ').capitalize()
        if username in users.keys():
            print(f'\n\t\t!Bienvenid@ {username}!\n')
            return username
        elif username not in users.keys():
            print("Aún no estás registrad@.")           
            print("Lo dirigiremos a sección Registro.\n")
            return 

    def get_password(self):
        return self.__password

    def sign_up(self):
        self.firstname= input('Ingresa tu nombre: ')
        self.surname= input('Ingresa tu apellido: ')
        self.ID= input('Ingresa tu nombre de usuario: ')
        self.__password = input('Ingresa tu nombre de usuario: ')
        UserCheck.password_validation(self.__password)
        print('Ingresa sólo dígitos de la fecha solicitada')
        self.birthDay = input('Ingresa tu día de nacimiento: ')
        UserCheck.check_int(self.birthDay)
        self.birthMonth = input('Ingresa tu mes de nacimiento: ') 
        UserCheck.check_int(self.birthMonth)
        self.birthYear = input('Ingresa tu año de nacimiento: ') 
        UserCheck.check_int(self.birthYear)
        self.email = input('Ingresa tu correo electrónico: ') 
        self.contact = input('Ingresa tu número de contacto: ')
        UserCheck.check_int(self.contact)

    # instance method to save users info.
    def save_user(self,users):
        dob= '{self.birthDay}/{self.birthMonth}/{self.birthYear}'
        users[self.ID]= {self.firstname,self.surname,
                        self.__password,dob,self.email,self.contact}
        return users
        
    def delete_user(self,users):
        print("\nEliminacón de Usuarios: \n")
        print("\t Ingrese nombre de usuario/ID de la cuenta a eliminar:")
        d_user = input().capitalize()
        if d_user in users.keys():
            i=0
            while i < 3:
                i += 1
                password= input('> Ingrese su contraseña:')
                if password == users[d_user][self.__password]:
                    remove = users.pop(d_user)
                    print(f"\n>  {d_user}:{remove} ha sido eliminado. \n")
                    return users
                else:
                    print('Contraseña Incorrecta \n')
                if i == 3:
                    print("Se acabaron tu número de intentos. \n")
                    return
        else:
            print(f"\n{d_user} no está registrado. \n")
            # menu()
        
class Employee(Users):
    def __init__(self, firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact):
        # call super() function to run the __init__() method 
        # of the parent class inside the child class
        super().__init__(firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact)
        #GBP
        self.base_salary= 800

class Seller(Employee):
    def __init__(self, firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact, customer):
        super().__init__(firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact)
        self.customer=customer
        self.sales_balance=[]
        self.profit_percent= 11

    def save_user(self,users):
        dob= '{self.birthDay}/{self.birthMonth}/{self.birthYear}'
        users[self.ID]= {self.firstname,self.surname,
                        self.__password,dob,self.email,self.contact,self.sales_balance}
        return users

    def assisted_user(self):
        print (f"{self.firstname} {self.surname} atendió a {self.customer._username}.")

    # Updated Users info available only to Sellers.
    # Display registered users available only w/employee ID.
    def customer_register(employees):
        i=0
        while i < 3:
            i += 1
            employeeId = input("Ingrese su ID:")
            if employeeId in employees.keys():
                print(f"\n {employees[employeeId]['name']} Los usuarios registrados son: \n")
                for user in users.keys():
                    print(f"\t {user}: Nombre y Apellido: {users[user]['name']} {users[user]['surname']} \n      \t\t| Edad: {users[user]['age']} | Contraseña: {users[user]['password']}\n      \t\t| Contacto: {users[user]['contact']} \n      \t\t| Fecha de Registro: {users[user]['joinDate']} \n")
                return 
            else:
                print(f"\n{employeeId} no está registrado.")
            if i == 3:
                print("Se acabaron tu número de intentos. \n")
                return


class Customer(Users):
    def __init__(self, firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact,balance):
        super().__init__(firstname, surname, ID, password, birthDay, birthMonth, birthYear, email, contact)
        self.balance=balance
        self.shoppings=[]

    def age_group(self):
        contact_info=(self.ID,self.firstname,self.surname,self.email)   
        for info in users.values():
                if self.birthYear in range (1901,1926):
                    mktg ["greatest"].append(contact_info)
                elif self.birthYear in range (1927,1945):
                    mktg ["silent"].append(contact_info)
                elif self.birthYear in range (1946,1964):
                    mktg ["baby_Boomers"].append(contact_info)
                elif self.birthYear in range (1965,1976):
                    mktg ["gen_X"].append(contact_info)
                elif self.birthYear in range (1977,1983):
                    mktg ["xennials"].append(contact_info)
                elif self.birthYear in range (1983,2000):
                    mktg ["gen_Y"].append(contact_info)
                elif self.birthYear >= 2000:
                        mktg ["gen_Z"].append(contact_info)

        
    # instance method to save users info.
    def save_user(self,users):
        dob= '{self.birthDay}/{self.birthMonth}/{self.birthYear}'
        users[self.ID]= {self.firstname,self.surname,
                        self.__password,dob,self.email,self.contact,
                        self.balance,self.shoppings}
        return users

    def contact_us(self):
        pass

class Shipping_info():
    def __init__(self, street,city, postalCode, province, country ):
        self.street = street 
        self.city = city
        self.postalCode= postalCode
        self.province= province
        self.country= country

#Child class (Multiple Inheritance)
class Greatest(Customer, Shipping_info):
    def advertising(self,dict,A):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {A} a {self.firstname} {self.surname}, {adrress} ')

class Silent(Customer, Shipping_info):
    def advertising(self,dict,B):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {B} a {self.firstname} {self.surname} ')

class BabyBoomers(Customer, Shipping_info):
    def advertising(self,dict,C):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {C} a {self.firstname} {self.surname} ')

class GenX(Customer, Shipping_info):
    def advertising(self,dict,D):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {D} a {self.firstname} {self.surname} ')

class Xennials(Customer, Shipping_info):
    def advertising(self,dict,E):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {E} a {self.firstname} {self.surname} ')

class GenY(Customer, Shipping_info):
    def advertising(self,dict,F):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {F} a {self.firstname} {self.surname} ')

class GenZ(Customer, Shipping_info):
    def advertising(self,dict,G):
        adrress= {self.street,self.city, self.postalCode, self.province,self.country}
        if self.ID in dict.keys:
            print(f'> Enviando contenido {G} a {self.firstname} {self.surname} ')















# # Driver Code
# if __name__ == "__main__":
#     # object user of class Users.
#     user= Users()
#     user.save_dict()
#     user.age_group()
#     user.shopping()


    
    # #details
    #     street: str 
    #     city: str
    #     postalCode: str
    #     province: str
    #     country: str

