import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
    

continuer_generation = True
while continuer_generation:
    nb_multi = input("Tapez le nombre de multiplication du carré : ")
    nb_multi = int(nb_multi)
    if nb_multi > 7:
        print ("Le nombre est trop grand .. \n (Un nombre aussi grand ferait planter la visualisation graphique)")
        nb_multi = input("Tapez le nombre de multiplication du carré : ")
    nb_multi = int(nb_multi)
    dif_pt = input("Definissez la différence d'altitude maximun entre les point (ex:10) : ")
    dif_pt = int(dif_pt)

    nb_pts_ligne = int((2**nb_multi)+2)
    if nb_multi <1:
        print ("Le nombre de répétition doit etre supérieur à 1")
        
        


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



    #-------Ecriture fichiers------#
    fichier_02 = open("02_FichierPointsXYZ.py", "w")
    #fichier_02 = open("02_FichierPointsXYZ.txt", "w")
    mon_fichier = open("01_MatriceZ.txt", "w")

    fichier_02.write("from mpl_toolkits.mplot3d import Axes3D"+'\n'+"import matplotlib.pyplot as plt"+'\n'+'\n'+'\n'+'\n'+"fig = plt.figure()"+'\n'+"ax = fig.add_subplot(111, projection='3d')"+'\n'+'\n')
                     


    #X
    fichier_02.write("x =")
    x = 0
    list_x =[]
    for x in range(1, nb_pts_ligne, 1):
        for x in range(1, nb_pts_ligne, 1):
            list_x.append(x)
        x += 1
    fichier_02.write(str(list_x))

    #Y
    fichier_02.write("\n"+"y =")
    y1 = 0
    y2 = 0
    list_y =[]
    for y1 in range(1, nb_pts_ligne, 1):
        for y2 in range(1, nb_pts_ligne, 1):
            list_y.append(y1)
        y1 += 1
    fichier_02.write(str(list_y))


    #Z
    fichier_02.write("\n"+"z =[")
    t_ok = generate_tab(t, dif_pt, nb_multi)
    list_z = []
    for l in t_ok:
        for i in range(0, len(l),1):
            fichier_02.write(str(l[i])+",")
            list_z.append(l[i])
    fichier_02.write("]")    
            
    mon_fichier.write("ncols"+"         "+"33"+"\n")
    mon_fichier.write("nrows"+"         "+"33"+"\n")
    mon_fichier.write("xllcorner"+"     "+"0"+"\n")
    mon_fichier.write("yllcorner"+"     "+"0"+"\n")
    mon_fichier.write("cellsize"+"      "+"5.000000"+"\n")
    mon_fichier.write("NODATA_value"+"   "+"-9999"+"\n")

    for l in t_ok:
        a = 1
        for i in l:
            mon_fichier.write(str(i)+" ")
        mon_fichier.write("\n")


    fichier_02.write("\n"+"\n"+"\n"+"\n"+"ax.scatter(x, y, z, c='r', marker='o')"+"\n"+"\n"+"ax.set_xlabel('X Label')"+"\n"+"ax.set_ylabel('Y Label')"+"\n"+"ax.set_zlabel('Z Label')"+"\n"+"\n"+"plt.show()")


    fichier_02.close()    
    mon_fichier.close()


    #-----------generation point --------
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x =list_x
    y =list_y
    z =list_z



    t = np.arange(100)
    ax.scatter(x, y, z, c='b', marker='o')

    ax.set_xlabel('axe des X')
    ax.set_ylabel('axe des Y')
    ax.set_zlabel('axe des Z')
    
    plt.show()
    quitter = input("Souhaitez-vous recommencer (o/n) ? ")
    if quitter == "n" or quitter == "N":
        continuer_generation = False
        print ("Au revoir")


