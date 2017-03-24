import random


def eval_carre(t, dif):
    """
    :param tab_in: tableau des 4 points en entrée [[pno, pne], [pso, pse]]
    :param dif: valeur de bruit autorisée dans le calcul des altitudes
    :return: tableau des 9 points en sortie
    """
    # on initialise le tableau en sortie
    t_out = [[0 for i in range(3)] for j in range(3)]

    # on calcule les 4 extrémités
    t_out[0][0] = t[0][0]
    t_out[0][2] = t[0][1]
    t_out[2][0] = t[1][0]
    t_out[2][2] = t[1][1]

    # on calcule le centre
    t_out[1][1] = (t[0][0] + t[0][1] + t[1][0] + t[1][1]) / 4 + random.uniform(-dif, dif)

    # on calcule le milieu des aretes
    t_out[0][1] = (t[0][0] + t[0][1]) / 2 + random.uniform(-dif, dif)
    t_out[1][0] = (t[0][0] + t[1][0]) / 2 + random.uniform(-dif, dif)
    t_out[1][2] = (t[0][1] + t[1][1]) / 2 + random.uniform(-dif, dif)
    t_out[2][1] = (t[1][0] + t[1][1]) / 2 + random.uniform(-dif, dif)

    return t_out


def generate_tab(t_in, dif, n):
    """

    :param t_in:
    :param dif:
    :param n:
    :return:
    """
    t = eval_carre(t_in, dif)
    if n > 1:
        # on découpe le tableau en 4 et on répète l'opération
        t1 = [[t[0][0], t[0][1]], [t[1][0], t[1][1]]]
        t2 = [[t[0][1], t[0][2]], [t[1][1], t[1][2]]]
        t3 = [[t[1][0], t[1][1]], [t[2][0], t[2][1]]]
        t4 = [[t[1][1], t[1][2]], [t[2][1], t[2][2]]]

        t1_out = generate_tab(t1, dif, n-1)
        t2_out = generate_tab(t2, dif, n-1)
        t3_out = generate_tab(t3, dif, n-1)
        t4_out = generate_tab(t4, dif, n-1)

        # on fusionne les 4 parties
        t = fusion_tab(t1_out, t2_out, t3_out, t4_out)

    return t


def fusion_tab(t1, t2, t3, t4):
    """
    Fusion de 4 tableaux en un seul.
    En prend la moyenne des extrémités.
    :param t1:
    :param t2:
    :param t3:
    :param t4:
    :return:
    """
    n = len(t1)
    t = [[0 for i in range(2*n-1)] for j in range(2*n-1)]

    for i in range(n-1):
        for j in range(n-1):
            t[i][j] = t1[i][j]

        t[i][n-1] = (t1[i][n-1] + t2[i][0]) / 2

        for j in range(n, 2*n-1):
            t[i][j] = t2[i][j-n+1]

    for j in range(n-1):
        t[n-1][j] = (t1[n-1][j] + t3[0][j]) / 2

    t[n-1][n-1] = (t1[n-1][n-1] + t2[0][n-1] + t3[n-1][0] + t4[0][0]) / 4

    for j in range(n, 2*n-1):
        t[n-1][j] = (t2[n-1][j-n+1] + t4[0][j-n+1]) / 2

    for i in range(n, 2*n-1):
        for j in range(n-1):
            t[i][j] = t3[i-n+1][j]

        t[i][n-1] = (t3[i-n+1][n-1] + t4[i-n+1][0]) / 2

        for j in range(n, 2*n-1):
            t[i][j] = t4[i-n+1][j-n+1]

    return t


t = [[0, 0], [0, 0]]
t[0][0] = random.uniform(0, 100)
t[0][1] = random.uniform(0, 100)
t[1][1] = random.uniform(0, 100)
t[1][0] = random.uniform(0, 100)

t_ok = generate_tab(t, 10, 1)
for l in t_ok:
    print(l)
