""" 
DESARROLLO
Crear clases con sintaxis Python
Actualizando módulo anterior, Python básico:  
        + Identifica 3 tipos de usuarios de su aplicación.
        + Acciones  se ejecutan de forma interna en nuestra aplicación:
            Ej: acceder a datos sensibles, registrar nuevos usuarios, 
                enviar solicitudes de información adicional. 
        + Nuevos atributos y acciones que pueden realizar los objetos. 
        + Graficar relaciones entre diferentes clases.
        + Desarrollen el ejercicio de forma intuitiva. 
        """


# n_users=0
users={}

# class Users is declared.
class Users: 
    # constructor
    def __init__(self):
        # keys are initialized with their respective values
        self._firstname= input('Ingresa tu nombre: ')
        self._surname= input('Ingresa tu apellido: ')
        self.username= input('Ingresa tu nombre de usuario: ')
        self.password = input('Crea tu contraseña: ')
        self.birthDay = int(input('Ingresa tu día de nacimiento: '))
        self.birthMonth = int(input('Ingresa tu mes de nacimiento: ')) 
        self.birthYear = int(input('Ingresa tu año de nacimiento: ')) 
        self.phone = input('Ingresa tu número de contacto: ')
        # self.age_group= 


    def save_dict(self):
        # calling attribute __dict__ on user object
        users[self.username]= self.__dict__
        #  and printing it.
        print(users)
        return users

    def age_group(self):
        for user, info in users.items():
                if info["birthYear"] in range (1901,1926):
                    print( "greatest")
                elif info["birthYear"] in range (1927,1945):
                    print( "silent")
                elif info["birthYear"] in range (1946,1964):
                    print( "baby_Boomers" )
                elif info["birthYear"] in range (1965,1976):
                    print( "gen_X")
                elif info["birthYear"] in range (1977,1983):
                    print( "xennials" )
                elif info["birthYear"] in range (1983,2000):
                    print( "gen_Y")
                elif info["birthYear"] >= 2000:
                    print( "gen_Z")

    def shopping(self):
        print ("Ingrese su nombre de usuario")
        user_name= input()
        print ("Ingrese su contraseña")
        user_pass=input()
        if user_name in users.keys():
            if users[user_name]["password"]== user_pass:
                print(f'Bienvenid@ {user_name}')
                print('Vamos a comprar!')


# object user of class Users.
user= Users()
user.save_dict()
user.age_group()
user.shopping()







    

    # 

    
    # #details
    #     street: str 
    #     city: str
    #     postalCode: str
    #     province: str
    #     country: str

        # self._firstname= firstname
        # self._surname= surname
        # self.username= username
        # self.__password = password
        # self.birthDay = birthDay
        # self.birthMonth = birthMonth
        # self.birthYear = birthYear 
        # self.phone = phone