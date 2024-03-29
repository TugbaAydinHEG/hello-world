"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
### Déclaration des variables
fumeur : str
sexe : str
age : float
sport: str
risque: int


### Initialisation des variables
risque = 0
fumeur = input("Etes-vous fumeur ? (oui ou non) ")


sport = input ("faites vous du sport? (oui ou non)")


sexe = input ("Quel est votre sexe? (h ou f)")


age = float(input("Quel est votre age ?"))



### Séquence d'opération

if fumeur == "oui":
    risque += 2

if sport == "oui":
    risque += -1
if sexe == "h" and age > 50:
    risque += +1

if sexe == "f" and age > 60:
    risque += +1

if risque <= 1:
    print("le niveau du risque est faible (" + str(risque) + ")")
else:
    print("le niveau du risque est élévé (" + str(risque) + ")")





