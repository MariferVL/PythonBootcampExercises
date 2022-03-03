# Formulen un programa que: 
# i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los integrantes. 
# ii. Se asegure que todos su caracteres estén en mayúscula. 
# iii. Elabore una lista con cada palabra del string. 
# iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.
#  v. Indique cuántas palabras tenía el string. 
# vi. Imprima una tupla con todas las palabras del string. 
# vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa? Implementarlo!. - 

message= "Life is Impermanence. This will also change. María-Fernanda Villalobos López"
message_up= message.upper()
print(f'1. Caracteres en mayúscula: {message_up}')
words= message_up.split(' ') 
print(f'2.Lista con palabras del string:{words}')

if "MARÍA-FERNANDA" in words:
        print(f"3.Tu nombre está en el índice {words.index('MARÍA-FERNANDA')}")

print(f"4. El mensaje contiene {len(words)} palabras.")
stringTotuple= tuple(message_up.split(' '))
print(f"5. Tupla con palabras del string: {stringTotuple}")
jointuple=" ".join(stringTotuple[0:7]).title()

print(f'¿Deseas leer nuestro mensaje?  (Si/No)')
answer= input().capitalize()
if answer== "Si" or "Sí":
        print(f'6. Mensaje: {jointuple}')
else:
        print('Que tengas un buen día.')

#optionB:
# print("5. Escriba su mensaje y dejenos su nombre o alias")
# username= input('Escriba su nombre de usuario/alias: ').capitalize
# visitor_msg=input('Escriba su mensaje: ')
# print(visitor_msg)
# print(f'Agradecemos su mensaje {username} y sabemos que sus palabras son fiel reflejo de su esencia.')
