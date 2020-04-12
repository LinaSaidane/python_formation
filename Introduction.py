#coding : utf-8

#Initiation Openclassroom

"""
Une variable est un code alphanumérique que l'on lie à une donnée
de notre programme pour pouvoir l'utiliser à plusieurs reprises

 Une variable  : - composée de lettres, maj ou minu, chiffres et du symbole _ ou underscore
                 -  elle ne peut commencer par un chiffre
                 - les maj et les minu ne constituent pas la même variable AGE # age

 il existe certains mots-clés de python sont réservés : on ne peut pas créer des variables portant le nom
and, as, assert, else, if, not , while, break, except etc...

 Différents types de données  : - Le type entier se nomme int
                                - les nombres à virgule float
                                - les chaines de caractères : s'écrit de plusieurs manières :
                                - entre guillemets "blablabla "
                                - entre apostrophes 'blablabla'
                                - entre triples guillemets

 les fonctions : exécute un certain nombre d'instructions déjà enregistrées
 Elles s'utilisent en respectant la syntaxe suivante :

 nom_de_la_fonction(parametre_1,parametre_2,....,parametre_n)

                - commence par ecrire le nom de la fonction
                - place entre parenthèse les paramètres de la fonction si pas de paramètres quand même mettre les parenthèses



"""
mon_age = 24
mon_age
mon_age = mon_age + 2
# print au niveau du script pas dans la console python
print(mon_age)
mon_age_x2 = mon_age * 2
print(mon_age_x2)

# stocker une chaine de caractère dans une variable
ma_chaine = "Bonjour, la foule ! "

# préférable d'utiliser les guillemets "" pour ne pas confondre avec des mots comme j'aime.
# Pour palier au problème ' il faut \ avant apostrophes contenus dans le messag
chaine = 'j\'aime le Python ! '

# \n symbolise saut de ligne ou """
chaine3 = """ceci est un nouvel 
essai sur plusieurs 
lignes """
print(chaine3)

# possibilité de faire des opération comme suit
mon_age = mon_age + 1
# ou plus court (pareil pour -= , /= , *=)
mon_age += 1

a = 5
b = 32
a,b = b,a # permutation

# affectation valeurs à plusieurs variables
x = y = 3

# \ = saut à la ligne
1 + 4 - 3 * 19 + 33 \
    -45 * 2 + (8-3)

# fonction type : renvoie le type de la variable
# type(nom_de_la_variable)
a = 3
type(a)
type(3.4)
type ("un essai ") # str = string chaine de caractère

# fonction print : affiche la valeur
a = 3
print(a)
a = a + 3
b = a - 2
print("a = ", a, "et b = ", b) # 2 chaines de caractères et 2 variables a et b
print("Hello World !")
