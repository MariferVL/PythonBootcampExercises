import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
  
if flag ==-1:
    print("Not a Valid Password")


    # def password_val(password):
    # for password in sign_in():
    #     while True:  
    #         if (len(password)<8):
    #             print('Recuerda que son mínimo 8 caracteres')
    #         elif (len(password)>11):
    #             print('Recuerda que son máximo 11 caracteres')
                
    #         elif re.search(" ", password):
    #             print('No uses espacios en tu clave')
                
    #         elif not re.search("[a-z]", password):
    #             print('No olvides incluir al menos una letra en minúscula.')
                
    #         elif not re.search("[A-Z]", password):
    #             print('No olvides incluir al menos una letra en Mayúscula.')
                
    #         elif not re.search("[0-9]", password):
    #             print('No olvides incluir al menos un número.')