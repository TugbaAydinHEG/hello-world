"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration des variables



### Initialisation des variables
PRIX_BILLET: int = 10
CARTE_MENSUELLE:int = 0


rabais_etudiant: int = 2
rabais_membre: int = 3
forfait_famille: int = 1
prix_a_payer: int = 0

carte_etudiant:int
carte_membre: int
carte_famille:int

### Séquence d'opération



CARTE_MENSUELLE = input("Possédez- vous la carte mensuelle ? (oui ou non) ")

if CARTE_MENSUELLE == "oui":
   print("Prix a payer: 0")
else:

    carte_membre = input("Possédez-vous la carte membre ? (oui ou non) ")
    carte_etudiant = input("Possédez-vous la carte etudiant ? (oui ou non) ")
    carte_famille = input("Possédez-vous forfait famille? (oui ou non) ")


    if carte_membre == "oui":
        prix_a_payer = PRIX_BILLET - rabais_membre
        if carte_etudiant == "oui" or (carte_etudiant == "oui" and forfait_famille == "oui"):
            prix_a_payer = PRIX_BILLET - (rabais_membre + rabais_etudiant)
        elif  carte_famille == "oui":
             prix_a_payer = PRIX_BILLET - (rabais_membre + forfait_famille)


    else:
        if carte_etudiant == "oui":
            prix_a_payer = PRIX_BILLET - rabais_etudiant


        elif carte_famille =="oui":
            prix_a_payer = PRIX_BILLET - forfait_famille

        else:
            prix_a_payer = PRIX_BILLET
    print ("prix a payer",prix_a_payer,"CHF")






















