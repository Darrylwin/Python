L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
chaine = "Python2.7 est remplacé par Python3.X depuis 2018"
etudiants = {
    "etudiant_1": 13,
    "etudiant_2": 17,
    "etudiant_3": 9,
    "etudiant_4": 15,
    "etudiant_5": 8,
    "etudiant_6": 14,
    "etudiant_7": 16,
    "etudiant_8": 12,
    "etudiant_9": 13,
    "etudiant_10": 15,
    "etudiant_11": 14,
    "etudiant_12": 9,
    "etudiant_13": 10,
    "etudiant_14": 12,
    "etudiant_15": 13,
    "etudiant_16": 7,
    "etudiant_17": 12,
    "etudiant_18": 15,
    "etudiant_19": 9,
    "etudiant_20": 17
}


def liste_paires__impaires(liste_nombres) -> tuple:
    """
    :param liste_nombres: list
    :return: renvoie un tuple de listes impaire et paire

    """
    l_pair = []
    l_impaire = []
    for n in liste_nombres:
        if n % 2 == 0:
            l_pair.append(n)
        else:
            l_impaire.append(n)
    return (l_pair, l_impaire)


print(liste_paires__impaires(L))
print(type(liste_paires__impaires(L)))


def contient_un_chiffre(T) -> list:
    """

    :param T: list
    :return: renvoie la liste des mots contenant un chiffre
    """
    liste_mots = []
    T_separee = T.split(' ')
    for mot in T_separee:
        if nombres_chiffres(mot) >= 1:
            liste_mots.append(mot)
    return liste_mots


def nombres_chiffres(mot: str) -> int:
    """

    :param mot:
    :return: renvoie le nombre de chiffres contenus dans un mot
    """
    n_chiffres = 0
    for i in mot:
        if i.isdigit():
            n_chiffres += 1
    return n_chiffres


print(contient_un_chiffre(chaine))

print(list(etudiants))

etudiantAdmis = {}
etudiantNonAdmis = {}

for x, y in etudiants.items():
    if etudiants[x] >= 10:
        etudiantAdmis.update({x: y})
    else:
        etudiantNonAdmis.update({x: y})

print(etudiantAdmis)
print(etudiantNonAdmis)


def moyenneNote(liste):
    """
    :param liste:
    :return: retourne la moyenne des éléments de la liste
    """
    total_notes = 0
    for z in liste:
        total_notes += z
    return total_notes / len(liste)


etudiantMoyen = {}
notes = []
for x in etudiants.values():
    notes.append(x)

for x, y in etudiants.items():
    if etudiants[x] > moyenneNote(notes):
        etudiantMoyen[x] = y

print(etudiantMoyen)
