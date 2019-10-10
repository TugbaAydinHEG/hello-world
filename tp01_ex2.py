"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables

compteur :  float
item : int
creditFinal: float
###Initialisation des variables
SANDWICH = 1
CHIPS = 2
CHOCOLAT = 3
BONBONS = 4
ICE_TEA = 5
LIMONADE = 6
compteur = 0.0
creditFinal = 0.0

SANDWICH_PRIX = 4.90
CHIPS_PRIX = 2.50
CHOCOLAT_PRIX = 2.00
BONBONS_PRIX = 3.30
ICE_TEA_PRIX = 2.20
LIMONADE_PRIX = 1.90


### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")




numPiece = int (input("veuillez introduire votre monnai "))

    #piece = float(input("Entrer la monnaie: CHF"))"
    #numPiece = numPiece +1
    #print ("Vous avez CHF {0} dans la distributeur.".format(round(numPiece,2)))
print("")
print(" Veillez sélectionner un produit:")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")
print("")
round (creditFinal, 2)
item = int (input("Veuillez selectionner un produit:"))
if item == SANDWICH :
    if numPiece > SANDWICH_PRIX:
        creditFinal = numPiece - SANDWICH_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Sandwich au poulet servie! Bon appetit !")
    else:
        print("pas assez de l'argent'")

elif item == CHIPS :
    if numPiece > CHIPS_PRIX:
        creditFinal = numPiece - CHIPS_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Chips Paprika servies! Bon appetit !")
    else:
        print("pas assez de l'argent")

elif item == CHOCOLAT :
    if numPiece > CHOCOLAT_PRIX:
        creditFinal = numPiece - CHOCOLAT_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Barre chocolatée ! Bon appetit!")
    else:
        print("pas assez de l'argent")

elif item == BONBONS :
    if numPiece > BONBONS_PRIX:
        creditFinal = numPiece - BONBONS_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Bonbons! Bon appetit !")
    else:
        print("pas assez de l'argent")

elif item == ICE_TEA :
    if numPiece > ICE_TEA:
        creditFinal = numPiece - ICE_TEA_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Ice Tea! Santé !")
    else:
        print("pas assez de l'argent")

elif item == LIMONADE :
    if numPiece > LIMONADE_PRIX:
        creditFinal = numPiece - LIMONADE_PRIX
        print ("Monnai à rendre {0}:".format(round(creditFinal, 2)))
        print ("Limonade! Santé !")
    else:
        print("pas assez de l'argent")


else:
    print ("Ce n'est pas une option")






