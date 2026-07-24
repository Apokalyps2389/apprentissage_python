#creation d'une appplication pour convertir des centimètres en pouces
#1 pouce = 2.54 cm  
#1 cm = 0.3937 pouce
#demander à l'utilisateur le sens de la conversion (cm vers pouce ou pouce vers cm)
#demander à l'utilisateur la valeur à convertir
#demander à l'utilisateur sil veut faire une autre conversion ou quitter l'application



A = 2.54
B = 0.3937


def demander_valeur(message):
    while True:
        texte = input(message)
        try:
            return float(texte)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre valide.")


while True:
    demander_choix = input(
        "Voulez-vous convertir des centimètres en pouces (1), des pouces en centimètres (2) ou quitter (3) ? "
    )

    if demander_choix == "1":
        valeur = demander_valeur("Entrez la valeur en centimètres : ")
        resultat = valeur * B
        print(f"{valeur} cm = {resultat:.2f} pouces")

    elif demander_choix == "2":
        valeur = demander_valeur("Entrez la valeur en pouces : ")
        resultat = valeur * A
        print(f"{valeur} pouces = {resultat:.2f} cm")

    elif demander_choix == "3":
        print("Merci d'avoir utilisé notre application !")
        break

    else:
        print("ERREUR: Vous devez choisir entre 1, 2 ou 3.")




