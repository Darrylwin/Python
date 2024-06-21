d = {
    (1, 2): 'A',
    (3, 4): 'B',
    (6, 5): 'C',
    (5, 1): 'D',
}

d[(6, 1)] = 'D'
d[(5, 1)] = 'E'

print(d)

# ou

dos = {
    (1, 2): 'A',
    (3, 4): 'B',
    (6, 5): 'C',
    (5, 1): 'D',
}

dos.update({(6, 1): 'D'})
dos.update({(5, 1): 'E'})

print(dos)

cles = [x for x in d.keys()]
print(cles)

valeures_list = [y for y in d.values()]
valeures_tuple = tuple(valeures_list)
print(valeures_tuple)

for i, j in d.items():
    print(f"{j} : {i}")


def voyelle(car):
    """

    :param car: str
    :return: renvoir True si le caractere est une voyelle
    """
    if car in 'aoieuy':
        return True
    else:
        False


def compteVoyelles(phrase):
    """

    :param phrase: str
    :return: renvoie le nombre de voyelles contenues dans la phrase
    """
    n_voyelles = 0
    for caractere in phrase:
        if voyelle(caractere):
            n_voyelles += 1
    return n_voyelles

print(compteVoyelles("Python2.7 est remplacé par Python3.X depuis 2018"))