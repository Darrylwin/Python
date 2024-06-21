"""# jours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#          30, 31]
# mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
#         'Décembre']
#
# jours_mois = []
# for i in range(len(mois)):
#     jours_mois.append(mois[i])
#     jours_mois.append(jours[i]+1)
# print(jours_mois)
from typing import Dict

# perso = {
#     'nom': "Monkey D.",
#     'prenom': "Kakarot",
#     "age": 12
# }
#
# print(perso)
#
# print("Kakarot" in perso)"""

"""marques: dict[str, str] = {
    "marque_1": "Ferrari",
    "marque_2": "Wolkswagen",
    "marque_3": "Mercedes",
    "marque_4": "koenigsegg",
    "marque_5": "Bugatti",
    "marque_6": "BMW",
}

print(marques)

for x in marques:
    print(marques[x])

print('===================')

for x, y in marques.items():
    print(x, ':', y)"""

etudiant = {
    "nom": "Holandia",
    "prenom": 'Miss',
    "age": 18,
    "sexe": 'Féminin',
    "Classe": 'TC1-A',
    "Parcours": "GLSI/ASR",
}

print(etudiant.items())

etudiant["Classe"] = 'TC1-E'
print(etudiant)

etudiant.update({"age": 19})
print(etudiant)
etudiant["taille"] = 1.60
print(etudiant)

etudiant.update({'formes': "aucune"})
print(etudiant)

etudiant.pop("age")
print(etudiant)
# print(etudiant['taille'])

etudiant.popitem()
print(etudiant)

etudiant.clear()
print(etudiant)