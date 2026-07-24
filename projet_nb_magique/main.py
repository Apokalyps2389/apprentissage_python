#creation dune application : le nombre magique
import random
def demander_nombre(nb_min, nb_max):
   question = 0
   while question == 0:
       question = input(f"Quel le nombre magique entre {nb_min} et {nb_max} : ")
       try:
           question_int = int(question)
           if nb_min <= question_int <= nb_max:
               return question_int
           else:
               print(f"Veuillez entrer un nombre entre {nb_min} et {nb_max}.")
               question = 0
       except ValueError:
           print("Veuillez entrer un nombre valide.")
           question = 0



NB_REPONSE= 0
NB_MIN = 1
NB_MAX = 10
NB_VIES = 4
NOMBRE_MAGIQUE = random.randint(NB_MIN, NB_MAX)


while NB_REPONSE != NOMBRE_MAGIQUE and NB_VIES > 0:

    NB_REPONSE = demander_nombre(NB_MIN, NB_MAX)


    if NB_REPONSE < NOMBRE_MAGIQUE:
        print("")
        print("Le nombre magique est plus grand.")
        NB_VIES = NB_VIES - 1
        print(f"Il vous reste {NB_VIES} vies.")
        
    elif NB_REPONSE > NOMBRE_MAGIQUE:
        print("")
        print("Le nombre magique est plus petit.")
        NB_VIES = NB_VIES - 1
        print(f"Il vous reste {NB_VIES} vies.")
        
    else:
        print("")
        print("Félicitations ! Vous avez trouvé le nombre magique !")

    if NB_VIES == 0:
        print("")
        print("Vous avez perdu ! Le nombre magique était :", NOMBRE_MAGIQUE)
        



