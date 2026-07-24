#creer un jeu de multiplication pour apprendre les tables de multiplication
#creer une fonction pour poser la question et gerer les erreurs de saisie    
#creer une fonction reponse pour verifier si la reponse est correcte ou non   
#creer une fonction pour afficher le score final
#choisir de nombre aleatoire entre 1 et 10     
#choisir le nombre de questions a poser      


import random

NB_QUESTIONS = 5


def poser_question(premier_nombre, deuxieme_nombre):
    while True:
        try:
            reponse = int(input(f"Combien font {premier_nombre} x {deuxieme_nombre} ? "))
            return reponse
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre valide pour la réponse")


def verifier_reponse(premier_nombre, deuxieme_nombre, reponse):
    bonne = premier_nombre * deuxieme_nombre
    if reponse == bonne:
        print("Bonne réponse !")
        return True
    else:
        print(f"Mauvaise réponse ! La bonne réponse était {bonne}.")
        return False


def run_game(nb_questions: int = NB_QUESTIONS):
    score = 0
    for i in range(1, nb_questions + 1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"\nQuestion {i}/{nb_questions}")
        reponse = poser_question(a, b)
        if verifier_reponse(a, b, reponse):
            score += 1
    print(f"\nFin du jeu ! Score: {score}/{nb_questions}")


if __name__ == "__main__":
    run_game()