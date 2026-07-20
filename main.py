#exercice de pratique du site udemy 

    # programme qui demande le nom et l'age et le genre de quelqu'un 
    # definition des fonctions, grace à ça, possibilité de poser des questions à plusieurs personne avc la meme fonction
    # creation de condition pour forcer à entrer un nom, un age defini et un genre défini
    # utilisation de not in () dans la boucle while pour forcer le choix entre certaine reponse possible ( dans ce cas "F" ou "M")
    # la fonction upper() permet de convertir les majuscules et minuscules

def presentation_profil(Genre, Nom, Age) :

    print()
    print(" Bonjour " + Genre + " " + Nom + " vous avez " + str(Age) + " ans. ")
    print(" l'année prochaine, vous aurez " + str(Age+1) + " ans. ")
    print()


def demander_age(nom_personne) :
    age = 0
    while age == 0 :
        Age_str = input( nom_personne + " Quel est votre age ")  
        try:
            age = int(Age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre valide pour l'age")
    
    return age


def demander_nom(numero_personne) :
    nom = ""
    while nom == "" :
        nom = input( numero_personne + " Quel est votre nom : ")
    return nom


def demander_le_genre(nom_personne) :
    genre = ""
    while genre not in ("F", "M") :
        genre = input( nom_personne + " Quel est votre genre M or F ? ").upper()
    if genre not in ("F", "M") :
        print("ATTENTION, choisir entre F ou M ")
    if genre == "F" :
        genre = "madame"
    else :
        genre = "monsieur"
    return genre
         

# appel de la fonction pour demander le nom de la personne
Nom1 = demander_nom("1ère personne")
Nom2 = demander_nom("2ème personne")


# appel de la fonction pour demander l'age de la personne
Age1 = demander_age(Nom1)
Age2 = demander_age(Nom2)

# appel de la fonction pour demander le genre de la personne
Genre1 = demander_le_genre(Nom1)
Genre2 = demander_le_genre(Nom2)


# appel de la fonction pour afficher le profil de la personne
presentation1 = presentation_profil(Genre1, Nom1, Age1)
presentation2 = presentation_profil(Genre2, Nom2, Age2)


