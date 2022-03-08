""" 
OPCIÓN 2:
    Elaborar un programa que:
        Enviar cuestionarios a grupos particulares de personas.
        Distribuir cuestionarios de forma aleatoria (sin considerar información personal.
        Solo 7 personas responderán cuestionarios.
        Mismos cuestionarios del ejercicio anterior:
            Hábitos alimenticios, experiencia laboral, actividades recreativas, atletismo, natación y deportes
            general.
        Se envían uno después del otro con 3 segundos de desfase.
        Máximo de formularios/persona = 5.
        Almacene nombre de formulario que va a contestar c/persona.
        Programa un mensaje:
            número de cuestionarios a responder por cada persona y cuáles son. """

#Created by María-Fernanda Villalobos (feat.Javier 'Python Master' Espinoza)

#To import 'random' library tools.
import random
#To import 'time' library tools.
import time
#List with quizzes topics given by the task.
quiz = ('nutrition_q', 'workexperience_q', 'employability_q',
    'hobbies_q', 'athletics_q', 'swimming_q', 'sports_q')
#Dictionary with usernames as keys and empty values to fill with the running code.
quiz_dict={'Tam': [] , 'Mario': [], 'Pau': [], 'Dany':[], 'Flo':[], 'Amanel':[], 'Sam':[]}

while True:
    #randomly select user from dictionary (quiz_dict).
    r_user= random.choice(list(quiz_dict.keys()))
    #randomly select quiz from list (quiz).
    r_quiz= random.choice(quiz)
    #create var to break the loop.
    exit_quiz=False
    #To iterate through keys in the dictionary quiz_dict.
    for key in quiz_dict.keys():
        #Condition to set maximum values per key/users.
        if len(quiz_dict[key]) ==5:
            #To iterate through keys in the dictionary quiz_dict.
            for user in quiz_dict.keys():
                #Display message with number of quizzes to be answered by each person and which ones.
                print(f'El usuario {user} recibió {len(quiz_dict[user])}: {quiz_dict[user]} ')
            #To break the loop.
            exit_quiz=True
            break 
    #To check condition.
    if exit_quiz:
        break
    #Aother condition that occurs if the above doesn't happen.
    else: 
        #if r_quiz isn't in the users list execute to not repeat quiz.
        if r_quiz not in quiz_dict[r_user]:
            #Condition to set action when values are = 5.
            if len(quiz_dict[r_user])==5:
                #Do nothing.
                pass
            #If the above doesn't happen.
            else:
                #Display quiz (r_quiz) sent to a user(r_user).
                print(f'Se ha enviado {r_quiz} a {r_user}.')
                #Add quiz randomly selected(r_quiz) to the list r_user.
                quiz_dict[r_user].append(r_quiz)
        #If the above doesn't happen.
        else:
            #Do nothing.
            pass
    #Do this whole process every 3 seconds.
    time.sleep(3)    