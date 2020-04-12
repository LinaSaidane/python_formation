# Mon premier programme : savoir si une année est bissextile ou non
annee = input("Saisissez une année : ")
annee =int(annee)

if annee != % 4:
   print ("année non bissextile.")
else:
   print( "année bissextile.")

if annee == % 4 and annee == % 100:
if annee == % 400:
 print("l'année est bissextile.")
     else:
    print( "l'année n'est pas bissextile.")
          else:
            print(l'année est bissextile.")

#correction

annee = input("Saisissez une année : ")
annee =int(annee)
bissextile = False #selon que l'annee est bissextile ou non

#commencer par vérifier si ce sont des multiples :
if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissectile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print("L'année saisie est bissextile.")
else:
    print( "L'année saisie n'est pas bissextile.")

#optimisation du programme
annee = input("Saisissez une année : ")
annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")



