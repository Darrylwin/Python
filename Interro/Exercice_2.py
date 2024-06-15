# Exercice 2, numero 2:
def extrait_mot(chaine):
    decoupe = chaine.split(' ')
    resultat = []
    for mot in decoupe:
        if comptelettre(mot) > 0:
            resultat.append(mot)
    return resultat


def comptelettre(mot: str) -> int:
    """Prend une chaine de caracteres et renvoie le nombre de chiffres qu'elle contient"""
    n_chiffres = 0
    for i in mot:
        if i.isdigit():
            n_chiffres += 1
    return n_chiffres


print(extrait_mot('Bon1jour le m0nde'))
