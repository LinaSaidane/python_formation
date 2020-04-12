 """ Bloc d'instructions : une série d'instructions qui s'éxécutent dans un cas précis
                      ( par condition, par répétition)
                      les conditions vont de pair avec des opérateurs <, > , <=, >=, ==, !=
                      les conditions entre "if" et les : sont appelés des prédicats

  Indentation : un certain décalage vers la droite obtenu par un
ou plusieurs espaces ou tabulations.
"""
# premier exemple de condition
a = 5
if a > 0: # les : terminent la condition
    print("a est supérieur à 0.")

a = 5
b = 8
if a > 0:
    b += 1
    print ("a =", a, "et b = ",b)

# limites de la condition "if"
a = 0 # Si a = 0 rien ne ressort car rien n'est prévu pour ce cas
if a > 0:
    print ("a est positif.")
if a < 0:
    print("a est négatif.")

# instruction "else" : doit se trouver au même niveau que le if et se termine aussi par :
age = 21
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.") # ici Python n'exécute soit l'un ou soit l'autre jamais les deux

a = 0
if a > 0:
    print("a est supérieur à 0.")
else:
    print("a est inférieur ou égal à 0.")

# Instruction "elif" : contraction de "else if"
if a > 0:
    print("a est positif.")
elif a < 0:  # nouvelle condition
    print("a est négatif.")
else: # ne peut figurer qu'une fois à la fin pour cloturer la condition
    print("a est nul.")

# prédicats et booléens
a = 0
a == 5
a > -8
a != 33.19

# True et False sont les deux résultats du type booléen (commencent par des maj obligatoirement)
age = 21
majeur = False
if age >= 18:
    majeur = True

# mot-clés and, or et not
a = 5
if a >= 2:
    if a <= 8:
        print("a est dans l'intervalle.")
    else:
        print ("a n'est pas dans l'intervalle.")

# Sinon faire comme ceci and :

a = 5
if a >= 2 and a<= 8:
    print("a est dans l'intervalle.")
else:
    print ("a n'est pas dans l'intervalle.")

# or
a = 5
if a < 2 or a > 8:
    print(" a n'est pas dans l'intervalle.")
else:
    print("a est dans l'intervalle.")

# not not a == 5 equivaut à a != 5
majeur = False
if majeur is not True:
    print("vous n'êtes pas encore majeur.")

# fonction input() caractèrise une intéraction avec l'utilisateur
# test
annee = input("Saisissez une année : ")
print(annee)

# Pour convertir une variable vers un autre type : utilisez le nom du type comme une fonction
type(annee)
annee = int(annee)
type(annee)
print(annee)

# Test de multiples : tester le rest de la division entière de b par a
# # si le reste est nul alors a est un multiple de b
5 % 2 # 5 n'est pas multiple de 2
8 % 2
