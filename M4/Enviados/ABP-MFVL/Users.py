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

# class Users is declared.
class Users: 
    # instance attributes.
    def __init__(self,firstname,surname,username,password,birthDay,birthMonth,birthYear, email,phone ):
        # keys are initialized with their respective values
        self._firstname= firstname
        self._surname= surname
        self.username= username
        self.__password = password
        self.email= email
        self.phone = phone
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear 
        # self.birthDate= birthDate

    
    # instance method
    def sign_up(self):
        self._firstname= input('Ingresa tu nombre: ')
        self._surname= input('Ingresa tu apellido: ')
        self.username= input('Ingresa tu nombre de usuario: ')
        password = input('Ingresa tu nombre de usuario: ')
        UserCheck.password_validation(password)
        birthDay = input('Ingresa tu día de nacimiento: ')
        print('Ingresa sólo dígitos de lo solicitado:')
        UserCheck.check_int(birthDay)
        birthMonth = input('Ingresa tu mes de nacimiento: ') 
        UserCheck.check_int(birthMonth)
        birthYear = input('Ingresa tu año de nacimiento: ') 
        UserCheck.check_int(birthYear)
        self.email = input('Ingresa tu correo electrónico: ') 
        self.phone = input('Ingresa tu número de contacto: ')
        UserCheck.check_int(birthDay)

    def save_users(self):
        # calling attribute __dict__ on user object
        users.append(self)   #Duda existencial dict/lista al borrar
        users[self.username]= self.__dict__
        #  and printing it.
        print(users)
        return users

    def age_group(self):
        contact_info=(self.username,self._firstname,self._surname,self.email)   # com
        for info in users.values():
                if info["birthYear"] in range (1901,1926):
                    mktg ["greatest"].append(contact_info)
                elif info["birthYear"] in range (1927,1945):
                    mktg ["silent"].append(contact_info)
                elif info["birthYear"] in range (1946,1964):
                    mktg ["baby_Boomers"].append(contact_info)
                elif info["birthYear"] in range (1965,1976):
                    mktg ["gen_X"].append(contact_info)
                elif info["birthYear"] in range (1977,1983):
                    mktg ["xennials"].append(contact_info)
                elif info["birthYear"] in range (1983,2000):
                    mktg ["gen_Y"].append(contact_info)
                elif info["birthYear"] >= 2000:
                    mktg ["gen_Z"].append(contact_info)

    def log_in(self):
        print ("Ingrese su nombre de usuario")
        user_name= input()
        print ("Ingrese su contraseña")
        user_pass=input()
        users= self.__dict__
        if user_name in users.keys():
            if users[user_name]["password"]== user_pass:
                print(f'Bienvenid@ {user_name}')
        else:
            print("El usuario/contraseña no está registrada")
            print("Vuelve a ingresar o Registrate.")
            return main()
    
    def delete_user(self):
        users[self.username]= self.__dict__
        print (users)
        user2del= input("Ingrese el nombre de usuario de la cuenta a eliminar: ")
        if user2del in users.keys():
            del users[user2del]  #duda 2
            return users 
        
    def contact_us():
        pass

class Shipping_info():
    def __init__(self, street,city, postalCode, province, country ):
        self.street = street 
        self.city = city
        self.postalCode= postalCode
        self.province= province
        self.country= country

# super() builtin returns a proxy object (temporary object of the superclass)
# allows us to access methods of the base class.

#Child class (Multiple Inheritance)
class Greatest(Users, Shipping_info):

    def __init__(self):
        # call super() function to run the __init__() method 
        # of the parent class inside the child class
        super().__init__()


class Silent(Users, Shipping_info):

    def __init__(self):
        # call super() function
        super().__init__()

class BabyBoomers(Users, Shipping_info):

    def __init__(self):
        # call super() function
        super().__init__()

class GenX(Users, Shipping_info):

    def __init__(self):
        # call super() function
        super().__init__()

class Xennials(Users, Shipping_info):

    def __init__(self):
        # call super() function
        super().__init__()

class GenY(Users, Shipping_info):

    def __init__(self):
        # call super() function
        super().__init__()

class GenZ(Users, Shipping_info):

    def __init__(self):
        # call super() function.
        super().__init__()

















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

