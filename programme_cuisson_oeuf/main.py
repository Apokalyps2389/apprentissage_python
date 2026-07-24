#creation d'une application de minuterie pour cuire un oeuf
#plusieurs types de programmes (oeuf à la coque 3min, oeuf mollet 5min, oeuf dur 7min) ok
#demander à l'utilisateur le type de programme qu'il veut utiliser
#demander la validation du choix
#creation d'une fonction comptage pour afficher le temps restant
#fonction compte à rebours pour le temps de cuisson

import time


OEUF_A_LA_COQUE = 3
OEUF_MOLLET = 5
OEUF_DUR = 7


def demander_type_programme():
    while True:
        choix = input(
            "Choisissez le type de cuisson pour votre oeuf :\n"
            "\n"
            "1. Oeuf à la coque (3 minutes)\n"
            "2. Oeuf mollet (5 minutes)\n"
            "3. Oeuf dur (7 minutes)\n"
            "\n"
            "Entrez le numéro correspondant à votre choix : "
        )
        if choix in ("1", "2", "3"):
            return int(choix)
        print("ERREUR: Vous devez choisir entre 1, 2 ou 3.")


def calculer_temps_cuisson(choix):
    if choix == 1:
        return OEUF_A_LA_COQUE
    if choix == 2:
        return OEUF_MOLLET
    return OEUF_DUR


def validation_choix(choix):
    print(f"Vous avez choisi le programme {choix}.")
    while True:
        choix_final = input(
            "Appuyez sur O pour valider et lancer le compte à rebours, N pour relancer : "
        ).lower()
        if choix_final == "o":
            print("Compte à rebours lancé !")
            return True
        if choix_final == "n":
            print("Relance du programme...\n")
            return False
        print("ERREUR: Vous devez répondre par O ou N.")


def temps_restant(minutes):
    total_secondes = minutes * 60
    for seconde in range(total_secondes, 0, -1):
        if seconde % 10 == 0:
            minutes_restantes = seconde // 60
            secondes_restantes = seconde % 60
            print(f"\nTemps restant : {minutes_restantes:02d}:{secondes_restantes:02d}")
        else:
            print(".", end="", flush=True)
        time.sleep(1)
    print("\nLe temps de cuisson est terminé ! Votre oeuf est prêt à être dégusté.")


def afficher_information_cuisson(temps):
    if temps == OEUF_A_LA_COQUE:
        print("Vous avez choisi l'oeuf à la coque. Le temps de cuisson est de 3 minutes.")
    elif temps == OEUF_MOLLET:
        print("Vous avez choisi l'oeuf mollet. Le temps de cuisson est de 5 minutes.")
    else:
        print("Vous avez choisi l'oeuf dur. Le temps de cuisson est de 7 minutes.")


def main():
    while True:
        choix = demander_type_programme()
        temps = calculer_temps_cuisson(choix)
        if validation_choix(choix):
            afficher_information_cuisson(temps)
            temps_restant(temps)
            break


if __name__ == "__main__":
    main()
