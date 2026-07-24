import turtle


def dessiner_escalier(taille, nb_marches):
    for i in range(nb_marches):
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)


def dessiner_carre(taille):
    for i in range(4):
        t.forward(taille)
        t.right(90) 


def carres(taille_depart, nb_carres):
    for i in range(nb_carres):
        taille = (i+1) * taille_depart
        dessiner_carre(taille)  
       
       
t = turtle.Turtle()



carres(20, 5)

turtle.done()