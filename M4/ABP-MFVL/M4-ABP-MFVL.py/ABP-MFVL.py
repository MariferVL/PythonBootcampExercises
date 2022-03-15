#Empty list to add users info.
users={}

# class Users is declared.
class Users():
    # constructor: instance Users attributes.
    def __init__(self, firstName, surname, username,password,email,pronouns,ageGroup, balance):
        # keys are initialized with their respective values
        self.firstName= firstName
        self.surname=surname
        self._username = username
        self.__password=password
        self.email= email
        self.pronouns=pronouns
        self.ageGroup=ageGroup
        self.balance = balance

    # instance method to save users info.
    def save_user(self):
        users[self._username]= {self.firstName,self.surname,
                        self.__password,self.email,self.pronouns,self.ageGroup,
                        self.balance}
        return users

    # getter method to display protected info.
    def get_password(self):
        return self.__password

    # setter method to change protected info.
    def set_username(self,x):
        print(f"Su nombre de usuario es {self._username}")
        old=self._username
        self._username=x
        #change the old key for the new one.
        users[x] = users.pop(old)
        print(f"Cambio de nombre de usuario a: {self._username}")
        return users

class Sellers():    
    # constructor: instance Sellers attributes.
    def __init__(self, firstName,surname,id, category, initialProfit,customer):
        self.firstName= firstName
        self.surname=surname
        self.id=id
        self.category=category
        self.initialProfit = initialProfit
        self.customer=customer
        self.profits=[]
        self.__profitPercent=0.11

    # display the customer username assisted by the seller.
    def assisted_user(self):
        print (f"{self.firstName} {self.surname} atendió a {self.customer._username}.")

    # instance method to sell the products.
    def sell(self,user, product):
        print("Cuántos Zafu desea comprar?")
        bag=int(input(f"Máx {product.stock} unid.:  "))
        user.balance = user.balance - (bag * product.price)
        product.stock = product.stock - bag
        profit = int(bag* product.price * self.__profitPercent)
        self.profits.append(profit)
        print("¡Venta Exitosa!")
        print(f"La ganancia del vendedor es: $ {profit}")

    # To check the employee's business skills.
    def seller_quality(self):
        return False

    # To check employee's monthly sales.
    def seller_balance(self):
        total= sum(self.profits) + self.initialProfit
        print(f"Ventas Mensuales: {total}")
        if total < 1100000:
            return "De inmediato!"
        elif total in range(1100000,2200000):
            return f"{self.firstName} o chicotea o aprende a pescar."
        elif total >2200000:
            return f"{self.firstName} es de los nuestros!. Hazle una chapita de 'Buen Vendedor' para motivarlo ;) ."
        else:
            return f"{self.firstName} no es inútil, sirve de mal ejemplo. Y...FUERA!"
    
# constructor: instance Warehouse attributes.
class Warehouse():
    def __init__(self, SKU, name,model,description,stock, price):
        self.SKU = SKU
        self.name = name        
        self.model = model  
        self.description=description
        self.stock= stock
        self.price= price

    #Display product info.
    def show_details(self):
        print(f"Producto:{self.name} \n          Modelo:{self.model}, Descripción: {self.description}, Stock:{self.stock}")

# class Store():
#     type= "retail"
#     name= "Comprando Presente"
#     team= Sellers
#     customers= Users

# Driver code
# An Object of Users.
user1 = Users("Amanel", "Upekkha", "Ama","fg54gdgGs", "amanel@gmail.com", "she", "genY", 880000)
user1.save_user()
print("")
#Display users dictionary.
print (users)
print("")
# An Object of Sellers.
seller1 = Sellers("Marck", "Scott","IS-1133", "Vendedor Integral", 1111111, user1)
# seller1.seller_balance()
# An Object of Warehouse.
product1 = Warehouse("Z11-BLN-P-22","Zafu", "Foccus", "Zafu color blanco, 40cm de diam x 20cm de alto. Nueva Temporada.",1111,33000,)
print("Información cliente:")
# Retrieving password using getter.
print(f"Su contraseña es: {user1.get_password()}")
# Setting the username using setter.
user1.set_username("conTodo")
print (users)
print(f"El usuario cuenta con ${user1.balance} de saldo.")
print("")
print(f"Stock actualizado: {product1.model} = {product1.stock} unidades.")
product1.show_details()
print("")
seller1.sell(user1,product1)
seller1.assisted_user()
print(f"El saldo actualizado del cliente es: ${user1.balance}")
print(f"Stock actualizado: {product1.model} = {product1.stock} unidades.")
print("")
print(f"Es {seller1.firstName} {seller1.surname} un vendedor eficiente?: {seller1.seller_quality()}")
print(f"Hay que desvincular a {seller1.firstName} {seller1.surname}?:\n      Resolución: {seller1.seller_balance()}")
