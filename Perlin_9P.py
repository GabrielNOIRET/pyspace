"""
Fonction permettant de généerer un matrice
nb_point: Nombre de point par ligne/ nombre de ligne
"""
import random;

def puissance(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)





tab_in = [[pno, pne], [pso, pse]]

def eval_carre(tab_in, dif):
    """
    :param tab_in: tableau des 4 points en entrée [[pno, pne], [pso, pse]]
    :return: tableau des 9 points en sortie
    """
    # on initialise le tableau en sortie
    tab_out = [[0 for x in range(3)] for y in range(3)]

    # on calcule les 4 extrémités
    tab_out[0][0] = tab_in[0][0]
    tab_out[0][2] = tab_in[0][1]
    tab_out[2][0] = tab_in[1][0]
    tab_out[2][2] = tab_in[1][1]

    # on calcule le centre
    tab_out[1][1] = tab_out[0][0] + tab_out[0][2] + tab_out[2][0] + tab_out[2][2]
    tab_out[1][1] /= 4
    tab_out[1][1] += random.uniform(-dif, dif)

    # on calcule le milieu des aretes
    tab_out[0][1] = tab_in[0][0] + tab_in[0][1]
    tab_out[0][1] /= 2
    tab_out[0][1] += random.uniform(-dif, dif)
    tab_out[1][0] = tab_in[0][0] + tab_in[1][0]
    tab_out[1][0] /= 2
    tab_out[1][0] += random.uniform(-dif, dif)
    tab_out[1][2] = tab_in[0][1] + tab_in[1][1]
    tab_out[1][2] /= 2
    tab_out[1][2] += random.uniform(-dif, dif)
    tab_out[2][1] = tab_in[1][0] + tab_in[1][1]
    tab_out[2][1] /= 2
    tab_out[2][1] += random.uniform(-dif, dif)

    return tab_out

def imbriquement(tab_in, dif, n):
    
    if n == 1:
        t = eval_carre(tab_in, dif)
        return t

    else:
        
        t1 = [[t[0][0], t[0][1]], [t[1][0], t[1][1]]]
        t2 = [[t[0][1], t[0][2]], [t[1][1], t[1][2]]]
        t3 = [[t[1][0], t[1][1]], [t[2][0], t[2][1]]]
        t4 = [[t[1][1], t[1][2]], [t[2][1], t[2][2]]]

        t1_out = imbriquement(t1, dif, n-1)
        t2_out = imbriquement(t2, dif, n-1)
        t3_out = imbriquement(t3, dif, n-1)
        t4_out = imbriquement(t4, dif, n-1)

        t = 

    return tab_out

t[0][0] = random.uniform(0, 100)
t[0][1] = random.uniform(0, 100)
t[1][1] = random.uniform(0, 100)
t[1][0] = random.uniform(0, 100)

def carre(n):
    """
    :param n: nombre de lignes et de colonnes du carré
    """
    # initialisation du tableau
    t = [[0 for x in range(n)] for y in range(n)]
    
    #initialisation des coins --------------------------------------------
    #    pno - - - pne
    #     -  - - -  -
    #     -  - - -  -
    #     -  - - -  -  
    #    pso - - - pse    
    t[0][0] = random.uniform(0, 100);
    t[0][n-1] = random.uniform(0, 100);
    t[n-1][n-1] = random.uniform(0, 100);
    t[n-1][0] = random.uniform(0, 100);


         
    #print ("i = ",i, "type = ",type(i));
    #print ("nb_point = ",nb_point, "type = ",type(nb_point));

    #---------------------
    while  (n > 2):
        i = n / 2
        print ("id = ",id, "type = ",type(id))
       
        #début de la phase du diamant ------------------------------------
        #     - -   -    - -  
        #     - -   -    - -  
        #     - - center - -
        #     - -   -    - -  
        #     - -   -    - -  
        for x in range (int(id), nb_point, int(i)):
            for y in range (int(id), nb_point, int(i)):
                center = (t[x-int(id)][y-int(id)] + t[x-int(id)][y+int(id)] + t[x+int(id)][y+int(id)] + t[x+int(id)][y-int(id)]) /4
                t[x][y] = center + random.uniform(-dif ,dif)
                                

         #Phase du diamant -----------------------------------------------
        #     - X   X    X -  
        #     X X   X    X X 
        #     X X   -    X X
        #     X X   X    X X 
        #     - X   X    X -  
    

        for x in range (0, nb_point, int(id)):
            if x % i == 0:
                décalage = int(id)
            else:
                décalage = 0
           # print ("Décalage = ",décalage, "type = ", type(décalage))
        
            for y in range (int(décalage), nb_point, int(i)):
                somme = 0
                n = 1
                if x >= id:
                    somme = somme + t[x - int(id)][y]
                    n += 1
                elif (x + id) < nb_point:
                    somme = somme + t[x + int(id)][y]
                    n += 1
                elif y >= id:
                    somme = somme + t[x][y - int(id)]
                    n += 1
                elif (y + id) < nb_point:
                    somme = somme + t[x][y + int(id)]
                    n += 1
                #print ("somme = ",somme, "type = ",type(somme))
                #print ("n = ",n, "type = ",type(n))
                #print ("décalage = ",décalage, "type = ",type(décalage));
                t[x][y] = (somme/n) + random.uniform(-dif ,dif)

               

        i = id


    print ("Tableau :", t)


nomFichier = input("Choisir le nom du fichier : ")
nb_point_ini = int(input("Nombre de point par ligne : "))
dif = int(input("Min/Max de différence entre les points : "))
if (nb_point_ini %2 == 0):
    nb_point = nb_point_ini + int (1)
    print("Afin de faire un nombre impaire le nombre de lignes sera", nb_point_ini,"+1, soit",nb_point)
else : nb_point = nb_point_ini


carre()


fichier = open(nomFichier+'.txt', "a")
#fichier.write()
fichier.close()

