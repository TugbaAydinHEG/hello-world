"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

### Déclaration des variables

situation:str
age:int
nb_annee_permis:int
nb_accident:int
nb_annee_assurance:int


### Initialisation des variables






age = int(input("L'Age du conducteur"))


nb_annee_permis = int(input("Le nombre d'année de permis"))


nb_accident = int(input("Le nombre d'accidents"))


nb_annee_assurance = int(input("Le nombre d'années d'assurance"))



### Séquence d'opération


if age <25:
    if nb_annee_permis <2:
       if nb_accident == 0:
           situation = "rouge"
       else:
           if nb_accident == 1:
               situation = "pas assurance"

    else:
        if nb_accident == 0:
            if nb_annee_assurance <5:
               situation = "orange"
            else:
                situation = "vert"
        else:
            if nb_accident == 1:
               situation = "rouge"
            else:
                situation = "pas d'assurance"

else:
    if nb_annee_permis >2:
        if nb_accident == 0:
            if nb_annee_assurance <5:
                situation = "orange"
            else:
              situation = "vert"

        else:
            if nb_accident == 1:
                situation = "rouge"
            else:
               situation = "pas d'assurance"

        if nb_accident == 0:
                situation = "vert"
        else:
            if nb_accident == 1:
                situation = "orange"

            elif nb_accident ==2:
               situation = "rouge"

            else:
              print("pas d'accident")

if nb_annee_assurance >5:
    if situation == "rouge":
        situation = "orange"
    elif situation == "orange":
        situation = "vert"
    elif situation == "vert":
        situation = "bleu"




print ("votre situation:",situation)












