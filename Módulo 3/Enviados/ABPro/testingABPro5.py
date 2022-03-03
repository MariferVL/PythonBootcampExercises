""" DESARROLLO"""
# Guarde en una variable la siguiente información: 
#     ● Información de clientes: nombre, edad, identificador único. 
#     ● Información de productos: nombre, precio, identificador único y color.
"""   ● Información de la compra de cada cliente.  > No entender <
 """
# Debe crear 10 clientes y 5 productos.
#     Ustedes definen el número de variables y tipo de datos.
# Sin definir funciones, utilice métodos necesarios para: 
#     ● Agregar Cliente. 
#         clients["Franco"]= {"edad": 35, idUnico:1111 }
#     ● Agregar Producto
#         products["Little Prince"]= {"precio": 22000, "idUnico": 2222 }
#     ● Mostrar Clientes: Muestra el listado de clientes.  
#                 for key in clients:
#                     print(key)
#     ● Mostrar Producto: Muestra el listado de productos.
#                 for key in products:
#                     print(key)
#       ● Elimine clientes. ¿Qué información requiere para eliminar un cliente al >azar<?  
#       ● Elimine productos. ¿Qué información requiere para eliminar el >último producto< agregado? 
                # products.pop(key,-1)    
                # print(products.pop(key,-1)) para saber el elemento eliminado
# En el caso que la información se esté guardando en un diccionario. 
# - Imprima todas las >claves< con un delay de 2 segundos.  
# - Luego imprima los >valores< con un delay de 3 segundos.   >De a uno  :/ <
""" 
Código debidamente comentado.  """
""" 
Imprima en pantalla un listado que contenga los ID de los usuarios.  
    Modifique todos los ID. 
    Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
    Imprima en pantalla los nuevos ID.
    Elimine los últimos cuatro ID_clientes en el listado. """

#Created by María-Fernanda Villalobos

#To import 'random' library tools.
import random
#To import 'time' library tools.
import time
from unicodedata import name

#Dictionary with clients info requested in the assignment.

clients={"Jim Sturgess": {"edad": 35, "idUnico":1112 },
        "Ryan Gosling": {"edad": 35, "idUnico":1113 },
        "Violeta Parra ": {"edad": 49, "idUnico":1114 },
        "Gato Alquinta": {"edad": 35, "idUnico":1115 },
        "Anne Hathaway": {"edad": 39, "idUnico":1116 },
        "Hae-Jo Chang": {"edad": 35, "idUnico":1117 },
        "Willy Rodríguez": {"edad": 44, "idUnico":1118 },
        "Adele Blue": {"edad": 33, "idUnico":1119 },
        "Jhon Lennon": {"edad": 40, "idUnico":1120 },
        "Ed Sheeran": {"edad": 31, "idUnico":1121 }} 

#Dictionary with products info requested in the assignment.
products= {"Zero Limits": {"precio": 22000  , "idUnico": 2220 },
        "Mafalda": {"precio": 33000  , "idUnico": 2221 },
        "La quinta montaña": {"precio": 11000  , "idUnico": 2222 },
        "Brida": {"precio": 15000  , "idUnico": 2223 },
        "Curso de Milagros": {"precio": 60000  , "idUnico": 2224 },
        }

#To add a new client to the clients dictionary.
clients["Franco"]= {"edad": 35, "idUnico":1111 }

#To add a new product to the products dictionary.
products["Little Prince"]= {"precio": 11000, "idUnico": 2225 }

#To create a list with the dictionary keys called client_keys.
client_keys= list(clients.keys())
# #To iterate through keys in the clients dictionary.
# for key in client_keys:
    #To display on screen a list with the clients dictionary keys.
print(f'1. La lista de clientes actualizada es: {client_keys}')

#To create a list with the dictionary keys called prod_keys.
prod_keys= list(products.keys())
# #To iterate through keys in the products dictionary.
# for key in prod_keys:
    #To display on screen a list with the products dictionary keys.
print(f'2. La lista de productos actualizada es: {prod_keys}')
    

#To randomly select a key from clients dictionary.
d_key= random.choice(list(clients))
#To display on screen the deleted key from clients dictionary.
print(f'3. El item eliminado es {clients.pop(d_key)}')
#To display on screen the updated clients dictionary.
print(f'4. La lista de clientes actualizada es: {clients}')

#To remove the last item in clients dictionary.
for key in products.keys():
    # products.popitem(key,-1)
    print(f'5. El item eliminado es {products.pop(key,-1)}')
    #To display on screen the updated products dictionary.
    print(f'6. La lista de productos actualizada es:{products}')

for key in products.keys():
    #To create a list with the dictionary keys called prod_keys.
    prod_keys= list(products.keys())
    # #To iterate through keys in the products dictionary.
    # for key in prod_keys:
        #To display on screen a list with the products dictionary keys.
    print(f'7. Mostrando cada 2 seg. la lista de productos:{prod_keys}')
        #To do this process every 2 seconds.
    time.sleep(2)
         

#To create a list with the products dictionary values called prod_values.
prod_values= list(products.values())
# #To iterate through values in the products dictionary.
# for value in prod_values:
    #To display on screen a list with the products dictionary keys.
print(f'8. Mostrando cada 3 seg. las características de cada producto: {prod_values}')   #CHANGE TO LIST
    #To do this process every 3 seconds.
time.sleep(3)





# for key in client_keys():
#     print(clients[key].get('nombre'))

# To get each ID:
# for id, info in clients.items():
#     print("Personal ID:", id)