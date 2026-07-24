import random
import time
import os


def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')


def demarrer():
    effacer_ecran()
    print("Bienvenue dans le jeu du Simon !")
    time.sleep(0.7)
    print("Le but du jeu est de répéter la séquence de chiffres affichée.")
    time.sleep(0.7)
    print("Tu peux choisir un niveau de difficulté avant de commencer.")
    time.sleep(0.7)
    print("Appuyez sur Entrée pour commencer...")
    input()


def choisir_difficulte():
    print("\nChoisis un niveau de difficulté :")
    print("1 - Facile")
    print("2 - Moyen")
    print("3 - Difficile")

    while True:
        choix = input("Ton choix (1/2/3) : ").strip()
        if choix == "1":
            return "Facile", 0.7
        elif choix == "2":
            return "Moyen", 0.5
        elif choix == "3":
            return "Difficile", 0.3
        else:
            print("Choix invalide. Réessaie.")


def afficher_sequence(sequence, delai):
    print("Séquence : ", end="", flush=True)
    for num in sequence:
        print(num, end="", flush=True)
        time.sleep(delai)
    print()
    time.sleep(1)


def saisir_sequence():
    while True:
        user_input = input("Entrez la séquence (sans espaces) : ").strip()
        if not user_input:
            print("La saisie ne peut pas être vide.")
            continue
        if not user_input.isdigit():
            print("Entrez uniquement des chiffres.")
            continue
        return [int(ch) for ch in user_input]


def jouer_partie(difficulte, delai):
    sequence = []
    score = 0

    while True:
        effacer_ecran()
        print(f"Score actuel : {score}")
        print(f"Niveau : {difficulte}")
        time.sleep(0.7)

        next_number = random.randint(0, 9)
        sequence.append(next_number)
        afficher_sequence(sequence, delai)

        effacer_ecran()
        print(f"Score actuel : {score}")
        print(f"Niveau : {difficulte}")
        user_sequence = saisir_sequence()

        if len(user_sequence) != len(sequence):
            print("Séquence incorrecte : la longueur ne correspond pas.")
            print(f"La séquence était : {sequence}")
            print(f"Votre score final est : {score}")
            return score

        if user_sequence == sequence:
            score += 1
            print("Correct !")
            time.sleep(1)
        else:
            print("Incorrect !")
            print(f"La séquence était : {sequence}")
            print(f"Votre score final est : {score}")
            return score


def main():
    meilleur_score = 0

    while True:
        demarrer()
        difficulte, delai = choisir_difficulte()
        score = jouer_partie(difficulte, delai)

        if score > meilleur_score:
            meilleur_score = score
            print(f"Nouveau meilleur score : {meilleur_score}")
        else:
            print(f"Meilleur score actuel : {meilleur_score}")

        replay = input("Voulez-vous rejouer ? (o/n) : ").strip().lower()
        if replay != "o":
            print("Merci d'avoir joué !")
            break


if __name__ == "__main__":
    main()

