# exercice de pratique du site udemy

# programme simplifié qui demande le nom, l'âge et le genre de deux personnes
# chaque entrée est validée et le profil est affiché ensuite

def presentation_profil(genre, nom, age):
    print()
    print(f"Bonjour {genre} {nom}, vous avez {age} ans.")
    print(f"L'année prochaine, vous aurez {age + 1} ans.")
    print()


def demander_age(nom_personne):
    while True:
        age_str = input(f"{nom_personne} Quel est votre âge ? ")
        try:
            return int(age_str)
        except ValueError:
            print("ERREUR: Vous devez entrer un nombre valide pour l'âge.")


def demander_nom(numero_personne):
    while True:
        nom = input(f"{numero_personne} Quel est votre nom : ").strip()
        if nom:
            return nom
        print("ERREUR: Le nom ne peut pas être vide.")


def demander_le_genre(nom_personne):
    while True:
        genre = input(f"{nom_personne} Quel est votre genre (M ou F) ? ").strip().upper()
        if genre in ("F", "M"):
            return "madame" if genre == "F" else "monsieur"
        print("ATTENTION: choisir entre F ou M.")


def demander_nombre_personnes():
    while True:
        nombre_str = input("Combien de personnes voulez-vous enregistrer ? ")
        try:
            nombre = int(nombre_str)
            if nombre > 0:
                return nombre
            print("ERREUR: Le nombre doit être supérieur à zéro.")
        except ValueError:
            print("ERREUR: Vous devez entrer un nombre entier valide.")


def main():
    nombre_personnes = demander_nombre_personnes()

    for i in range(1, nombre_personnes + 1):
        numero = f"Personne {i}"
        nom = demander_nom(numero)
        age = demander_age(nom)
        genre = demander_le_genre(nom)
        presentation_profil(genre, nom, age)


if __name__ == "__main__":
    main()
