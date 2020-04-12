"""
les boucles: moyen de répéter un certain nbr de fois des instructions de notre
programme

"""
# Boucle :
# Programmer la table de multiplication par 7
nb = 10
print("1 *", nb , "=" , 1 * nb)
print("2 *", nb , "=" , 2 * nb)
print("3 *", nb , "=" , 3 * nb)
print("4 *", nb , "=" , 4 * nb)
print("5 *", nb , "=" , 5 * nb)
print("6 *", nb , "=" , 6 * nb)
print("7 *", nb , "=" , 7 * nb)
print("8 *", nb , "=" , 8 * nb)
print("9 *", nb , "=" , 9 * nb)
print("10 *", nb , "=" , 10 * nb)

# bloc d'instructions "while :
nb = input("Saisissez le nombre")
i = 0 #notre variable compteur

while i < 10:
    print(i + 1, "*", nb, "=",(i + 1) * nb)
    i += 1 #incrémente i de 1 à chaque tour de boucle

""" ne pas oublier d'incrémenter i sinon boucle infinie
puisque la valeur de i n'est (dans cet exemple jamais supérieure à 10
et la condition du while toujours vraie"""

# Pour arrêter une boucle ctrl + C

# Boucle for : travaille sur des séquences, les chaines de caractères sont des séquences de caractères
# construction : for element in sequence:
# element est une variable créee par le for
# exemple :
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    print(lettre)
# pas besoin d'incrémenter la variable lettre. Python se charge de l'incrémentation
# un grand avantage de l'instruction for
# in ne peut fonctionner qu'avec for
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne
        print("*")

# mot-clé : break --> interrompt une boucle
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input (" Tapez 'Q' pour quitter : ")
    if lettre =="Q":
        print("Fin de la boucle")
        break

# mot-clé : continue --> continue une boucle en repartant du while ou for
i = 1
while i < 20:
    if i % 3 == 0:
        i += 4
        print ("On incrémente i de 4. i est maintenant égale à", i)
        continue # on retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute 1 à i