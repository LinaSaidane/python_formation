"""Les modules permettent de regrouper plusieurs fonction selon le même principe

Modularité : regrouper dans des fonctions des parties de code que nous serons amenés à réutiliser

"""
# créer une fonction selon schéma suivant :
# def nom_de_la_fonction(parametre1, parametre2,parametreN): # bloc d'insctuction
# nom de la fonction se nomme comme une variable
# les paramètres sont séparés par des virgules et la liste encadrée par des parenthèses
# les deux points cloturent la ligne

# multiplication par 7 :
def table(7):
    i = 0
    while i < 10: # tant que i est strictement inférieure à 10
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
