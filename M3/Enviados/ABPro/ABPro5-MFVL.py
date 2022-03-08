
#Created by María-Fernanda Villalobos

#To import 'random' library tools.
import random
#To import 'time' library tools.
import time
from tkinter.font import names

#Dictionary of clients info requested in the assignment.
clients={"user1" : {"nombre": "Jim Sturgess","edad": 35},
        "user2" :{"nombre": "Ryan Gosling", "edad": 35},
        "user3" :{"nombre": "Violeta Parra ", "edad": 49},
        "user4" :{"nombre": "Gato Alquinta", "edad": 35},
        "user5" :{"nombre": "Anne Hathaway", "edad": 39},
        "user6" :{"nombre": "Hae-Jo Chang", "edad": 35},
        "user7" :{"nombre": "Willy Rodríguez", "edad": 44},
        "user8" :{"nombre": "Adele Blue", "edad": 33},
        "user9" :{"nombre": "Jhon Lennon","edad": 40},
        "user10" :{"nombre": "Ed Sheeran","edad": 31}}

#Dictionary with products info requested in the assignment. I changed color by origen and autor.
products= {"prod1":{ "nombre": "Zero Limits", "precio": 22000, "autor": "Joe Vitale","origen": "U.S." },
        "prod2":{ "nombre":"Mafalda","precio": 33000, "autor": "Quino", "origen": "Arg." },
        "prod3":{ "nombre":"La quinta montaña","precio": 11000, "autor": "Paulo Coelho", "origen": "Bra." },
        "prod4":{ "nombre":"Brida","precio": 15000, "autor": "Paulo Coelho", "origen": "Bra."},
        "prod5":{ "nombre":"Curso de Milagros", "precio": 60000, "autor": " Helen Schucman", "origen": "U.S." },
        }

#Add a new client to the clients dictionary.
clients["user11"]= {"nombre": "Franco","edad": 35}
#Add a new product to the products dictionary.
products["prod6"]= {"nombre":"Little Prince","precio": 11000}

# 1st Option: Displaying all the info in the dictionary.
#Display on screen updated clients dictionary.
print(f'1. Diccionario de clientes actualizada con nuevo cliente: {clients}')
#To display on screen a list of products dictionary keys.
print(f'2. Diccionario de productos actualizada con nuevo producto: {products}')

# 2nd Option: Displaying only the keys.
#Create a list of clients dictionary keys called client_keys.
# client_keys= list(clients.keys())
# print(f'1. Lista de clientes actualizada: {client_keys}')
#To create a list of dictionary keys called prod_keys.
# prod_keys= list(products.keys())
# print(f'2. Lista de productos actualizada: {prod_keys}')

#Create a list of clients dictionary keys called client_keys.
client_keys= list(clients.keys())
#Display on screen a list of clients dictionary keys.
print(f'3. Lista de ID de los clientes: {client_keys}')

#Assign a new key to the popped old key following assignment instructions.
clients["u1_piloto"] = clients.pop("user1")
clients["u2_piloto"] = clients.pop("user2")
clients["u3_piloto"] = clients.pop("user3")
clients["u4_piloto"] = clients.pop("user4")
clients["u5_piloto"] = clients.pop("user5")
clients["u6_piloto"] = clients.pop("user6")
clients["u7_piloto"] = clients.pop("user7")
clients["u8_piloto"] = clients.pop("user8")
clients["u9_piloto"] = clients.pop("user9")
clients["u10_piloto"] = clients.pop("user10")
clients["u11_piloto"] = clients.pop("user11")

#Create a list of updated clients dictionary keys called updated_keys.
updated_keys= list(clients.keys())
#Display on screen updated list.
print(f'4. Lista de ID de clientes actualizada: {updated_keys}')


for i in range(4):
    #Starting an empty list called r_idList.
    r_idList= []
    #To give a var the value of the last added client item which will be removed.
    r_id= clients.popitem()
    # #To add each removed item to the new list.
    # r_idList.append(r_id)
#Display on screen the updated clients dictionary.
print(f'5. Han sido eliminados últimos cuatro ID en diccionario: {clients}') 
        

#To randomly select a key from clients dictionary.
r_key= random.choice(list(clients))
r_client=clients.pop(r_key)
#To display on screen the deleted key from clients dictionary.
print(f'7. Se ha eliminado cliente: {r_client}')
#To display on screen updated clients dictionary.
print(f'8. Diccionario de clientes actualizado: {clients}')

#To give a var the value of the last added product item which will be removed.
r_product= products.popitem()
print(f'9. Item de productos eliminado:{r_product}')
#Display on screen updated products dictionary.
print(f'10. Diccionario de productos actualizado:{products}')

#To set a number of repetitions.
for i in range(3):
    #To create a list of dictionary keys called prod_keys.
    prod_keys= list(products.keys())
    #To display on screen a list of products dictionary keys.
    print(f'11. Mostrando cada 2 seg. lista de productos:{prod_keys}')
    #To do this process every 2 seconds.
    time.sleep(2)


#To set a number of repetitions.
for i in range(3):
    #To create a list of the products dictionary values called prod_values.
    prod_values= list(products.values())
    #To display on screen a list of products dictionary keys.
    print(f'12. Mostrando cada 3 seg. características de cada producto: {prod_values}') 
    #To do this process every 3 seconds.
    time.sleep(3)


# for user, info in clients.items():
#     #Iterate the items in the nested dictionary.
#     for key,value in info.items():
#         print(info["nombre"])

# for key in clients.keys():
#     print(clients[key].get("nombre"))