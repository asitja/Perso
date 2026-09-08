from random import *
import matplotlib.pyplot as plt
import matplotlib.markers
import math

# labyrinthe carré simple de taille n généré aléatoirement
# création d'une matrice de 0 et 1 -> 1 = mur
# visualisation de la matrice par tracé

def zeros(n) :
    MS = []
    for i in range(n):
        L = [0]*n
        MS.append(L)
    return MS

def cadre (n):
    M = zeros(n)
    
    for i in range (n) :
        M[0][i] = 1
    for i in range (n) :
        M[i][0] = 1
    for i in range (n) :
        M[n-1][i] = 1
    for i in range (n) :
        M[i][n-1] = 1
    M[n-2][n-1] = 0
    M[1][0] = 0
    return M

def printL (L):
    for loop in range (len(L)):
        print(L[loop])

def autourLibre(M,x,y):
    if (M[x-1][y] + M[x+1][y] + M[x][y-1] + M[x][y+1]) == 3 or (x == 0 and y == 0) or (x == 0 and y == 1) :
        return False
    else :
        return True

def traceL (M) :
    plt.clf()     # clear figure
    n = len(M)
    Lx = []
    Ly = []
    for i in range (n) :
        for j in range (n) :
            if M[i][j] == 1 :
                Lx.append(j)
                Ly.append(-i)
            x = []
            y = []
            if i != n-1 and j != n-1 :
                if M[i][j] == M[i][j+1] == 1 :
                    x.append(j+1)
                    y.append(-i)
                    x.append(j)
                    y.append(-i)
                if M[i][j] == M[i+1][j] == 1 :
                    x.append(j)
                    y.append(-i)
                    x.append(j)
                    y.append(-(i+1))
            elif i == n-1 and j != n-1 :
                if M[i][j] == M[i][j+1] == 1 :
                    x.append(j)
                    y.append(-i)
                    x.append(j+1)
                    y.append(-i)
            elif j == n-1 and i != n-1 :
                if M[i][j] == M[i+1][j] == 1 :
                    x.append(j)
                    y.append(-i)
                    x.append(j)
                    y.append(-(i+1))
            plt.plot(x, y,color = 'k')  # , linewidth = 25

    plt.axis('equal')
    plt.scatter(Lx, Ly, color = 'k', marker = 's', s = 164153*(n**(-2.29))) # fait les carrés
    plt.show()

def Laby (n):
    M = cadre(n)
    for i in range (n-2):
        for j in range (1,n-1):
            if autourLibre(M,i,j):
                M[i+1][j] = randint(0,1)
            if autourLibre(M,i,j) == False:
                M[i+1][j] = randint(0,2)%2
    M[1][1] = 0
    M[n-2][n-2] = 0
    for i in range (n-2):
            for j in range (1,n-1):
                if autourLibre(M,i,j) == False and M[i][j] == 0 :
                    M[i+1][j] = 0
    traceL (M)
    #return M



Laby (50)