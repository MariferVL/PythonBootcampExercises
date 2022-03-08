
#Iniciar sesión con un perfil individual: #saluda y te reconoce
            #Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
            #Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
            #¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente 
            #su nombre? ¿Cómo solucionarías este problema?
            #Convierte tu string en una lista, en la cual cada elemento es un usuario.
            #Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
            #Imprima en pantalla un mensaje de saludo a los diferentes usuarios. 
            # ¿Qué técnica puedes utilizar para realizar esto?

Users = "Tam, Mario, Pau, Dany, Flo, Marifer, Amanel, Sam"

if 'Tam'and 'Pau' and 'Flo' in Users:
    print("Los usuarios buscados están presentes.")

print(f"{Users.split(',')}. En total son {len(Users.split(','))} usuarios.")

users =["Tam", "Mario", "Pau", "Dany", "Flo", "Marifer", "Amanel", "Sam"]
i=0
while i<3:
    i+=1
    print("Introduce tu nombre:")
    logIn = input().capitalize()
    if logIn in users:
        print(f"¡Bienvenida {logIn}!. Tomate 10 segundos para cerrar los ojos y respirar")  
        break
    elif i==3:
        print("No estás registrado")
        print("Se acabaron tu número de intentos. Actualiza la página para ingresar.")
    else:
        print("No estás registrado")
        