import requests
import os
import json
from usuario import Usuario

get_lambda = lambda url: requests.get(url)


url = 'https://randomuser.me/api/?results=2&nat=gb&password=upper,lower,number,8-10&inc=id,name,dob,gender,login,cell,email,location,registered&noinfo'
db ='Json\costumer.json'
def get_def_function(url):
    return requests.get(url)

def run():
    data = get_lambda(url).json()["results"]
    costumers = []
    for user in data:
        name = user['name']['first']
        apellido = user['name']['last']
        edad = user['dob']['age']
        costumer = Usuario(name, apellido, edad)
        costumers.append(costumer.get())
    print(costumers, 'listado completo')

def get(costumers):
    if os.path.exists(db):
        with open(db) as file:
            data = json.load(file)
        return data
    else:
        with open(db, 'w') as file:
            json.dump(costumers, file, indent=4)
        return costumers

# def post(clients):
#     with open(db, 'w') as file:
#             json.dump(clients, file, indent=4)




    # buscar = [user for user in costumers if 'al' in user['nombre']]
    # print(buscar[0])
    # usuarios.pop(buscar[0])

if __name__ == '__main__':
    run()