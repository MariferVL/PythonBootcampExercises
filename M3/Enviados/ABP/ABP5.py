#Created by María-Fernanda Villalobos

#Dictionary of each user with info requested in the assignment.
Tamara={"edad": 35, "genero": "F", "email": "tam@presentes.com", "contacto": 987654321,"fechadenac": "15/11/1986" }
Paula={"edad": 24, "genero": "F", "email": "pau@presentes.com", "contacto": 912345678, "fechadenac": "08/01/1998"}
Florencia={"edad": 28, "genero": "F", "email": "flo@presentes.com", "contacto":923456789, "fechadenac":"31/01/1994" }
Mario={"edad": 35, "genero": "M", "email": "marete@presentes.com", "contacto":934567891, "Mechadenac": "06/11/1984" }
Daniel={"edad": 24, "genero": "M", "email": "dany@presentes.com", "contacto":945678912, "fechadenac": "19/07/1999"}
Amanel={"edad": 35, "genero": "F", "email": "ama@presentes.com", "contacto":956789123, "fechadenac": "11/11/1986"}
Sam={"edad": 35, "genero": "M", "email": "sam@presentes.com", "contacto":967891234, "fechadenac": "22/11/1986"}

#Create an empty list.
usuarios=[]
#Add a shallow copy to usuarios list.
usuarios.append(Tamara.copy())
usuarios.append(Paula.copy())
usuarios.append(Florencia.copy())
usuarios.append(Mario.copy())
usuarios.append(Daniel.copy())
usuarios.append(Amanel.copy())
usuarios.append(Sam.copy())
#Display list with all the users dicts.
print(f'1. Lista con diccionarios: {usuarios}')

# Opción2: 
# for i in range(0,len(usuarios)):
#     print(usuarios[i])


#Create an empty dict.
users = {}
#Add users info to an empty dict.

users["Tamara"]= {"edad": 35, "genero": "F", "email": "tam@presentes.com", "contacto": 987654321,"fechadenac": "15/11/1986" }
users["Paula"]= {"edad": 24, "genero": "F", "email": "pau@presentes.com", "contacto": 912345678, "fechadenac": "08/01/1998"}
users["Florencia"]= {"edad": 28, "genero": "F", "email": "flo@presentes.com", "contacto":923456789, "fechadenac":"31/01/1994" }
users["Mario"]= {"edad": 35, "genero": "M", "email": "marete@presentes.com", "contacto":934567891, "Mechadenac": "06/11/1984" }
users["Daniel"]= {"edad": 24, "genero": "M", "email": "dany@presentes.com", "contacto":945678912, "fechadenac": "19/07/1999"}
users["Amanel"]= {"edad": 35, "genero": "F", "email": "ama@presentes.com", "contacto":956789123, "fechadenac": "11/11/1986"}
users["Sam"]= {"edad": 35, "genero": "M", "email": "sam@presentes.com", "contacto":967891234, "fechadenac": "22/11/1986"}
#Display dictionary with all users info.
print(f'2. Información de los usuarios en un diccionario: {users}')

#Add username, unique ID, seniority, and incorporation date fields for each user, as required by the assignment.
users["Tamara"] |= {"nombre_usuario": "Tam", "id_unico": 15,"antigüedad": "18 años" , "fechadeincorporación": "15/11/2004" }
users["Paula"] |= {"nombre_usuario": "Paula", "id_unico":8,"antigüedad": "3 años" , "fechadeincorporación": "08/01/2020" }
users["Florencia"] |= {"nombre_usuario": "Florencia", "id_unico":31,"antigüedad": "2 años" , "fechadeincorporación":"31/01/2020" }
users["Mario"] |= {"nombre_usuario": "Mario" , "id_unico": 6,"antigüedad": "3 años" , "fechadeincorporación": "06/11/2019" }
users["Daniel"] |= {"nombre_usuario": "Daniel", "id_unico":19,"antigüedad": "2 años" , "fechadeincorporación":"19/07/2019" }
users["Amanel"] |= {"nombre_usuario": "Amanel" , "id_unico":11,"antigüedad": "7 años" , "fechadeincorporación": "11/11/2015" }
users["Sam"] |= {"nombre_usuario": "Sam" , "id_unico":22,"antigüedad": "1 años" , "fechadeincorporación": "22/11/2021"}
#Display on the screen updated dictionary.
print(f'3. Diccionario actualizado con info agregada: {users}')

#Iterate the items in dictionary.
for user, info in users.items():
    #Iterate the items in the nested dictionary.
    for key,value in info.items():
        # Display on the screen the incorporation dates of all users.
        print(f'4A. Las fechas de incorporación de {user} es: {info["fechadeincorporación"]}')
        break

# print('4B.  Las fechas de incorporación de los usuarios es: Tamara:' ,users['Tamara']['fechadeincorporación'],', Paula:',
# users['Paula']['fechadeincorporación'], ', Florencia:' ,
#     users['Florencia']['fechadeincorporación'], ', Mario:' ,users['Mario']['fechadeincorporación'], 
#     ', Daniel:' ,users['Daniel']['fechadeincorporación'], ', Amanel:' ,
#     users['Amanel']['fechadeincorporación'], 'y Sam:' ,users['Sam']['fechadeincorporación'])
