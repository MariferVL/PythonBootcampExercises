# DESARROLLO:
    # Elaborar un programa que tiene la funcionalidad de enviar cuestionarios a grupos particulares de personas.
        # ● Los formularios según:edad, lugar de origen y  afinidad con deportes. 
        # Usuarios ingresar por consola sus características (lugar de origen, edad y afinidad por los 
        # deportes). 
        # ● Máximo de cuestionarios a responder: 3
            # users América Latina:  nutrition_q  
            #     (30 -59 años):  workexperience_q
            #     >= 60 años + afinidad : swimming_q
            #     >=60 años: hobbies_q   
            # # users (18 - 29 años): employability_q
            # <= 60 años + afinidad: athletics_q 
            # +No Afinidad por deportes: sports_q
            # print ( número de cuestionarios a responder y cuáles son.)


quiz=('nutrition_q','workexperience_q', 'employability_q', 
    'hobbies_q', 'athletics_q', 'swimming_q', 'sports_q')

while True:
    groups={'age': int(input('Ingrese su edad: ')), 
            'nationality': input('Es originaria/o de América Latina (Si/No): ').lower(),
            'sports': input('Le interesan los deportes? (Si/No): ').lower()}
    q_to_do=[]
    if (groups['age'] >4 ) & (groups['nationality']=='si'):
        q_to_do.append(quiz[0])
        if groups['age'] >= 60:
            q_to_do.append(quiz[3])
            if  groups['sports']=='si':
                q_to_do.append(quiz[5]) 
                print(f'Estimado usuario, tenemos {len(q_to_do)} cuestionarios escogidos especialmente para usted.')
                print(f'Lo invitamos a realizar los cuestionarios {q_to_do}.')
                break
        if groups['age'] in range(30,60):
            q_to_do.append(quiz[1])
    if groups['age'] in range(18,30):
        q_to_do.append(quiz[2])
    if (groups['age'] <= 60) & (groups['sports']=='si'):
        q_to_do.append(quiz[4])
        print(f'Estimado usuario, tenemos {len(q_to_do)} cuestionarios escogidos especialmente para usted.')
        print(f'Lo invitamos a realizar los cuestionarios {q_to_do}.')
        break
    if groups['sports']=='no':
        q_to_do.append(quiz[6])
        print(f'Estimado usuario, tenemos {len(q_to_do)} cuestionarios escogidos especialmente para usted.')
        print(f'Lo invitamos a realizar los cuestionarios {q_to_do}.')
        break
    else:
        print('Estamos creando un questionario que se adapte a tus necesidades.')
        continue

