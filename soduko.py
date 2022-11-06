## Projet Sudoku - Valentin et Guilhem

S=[[0,1,0,0,7,8,0,0,0],
   [0,8,0,0,4,0,9,0,0],
   [0,0,5,6,0,0,0,1,0],
   [1,0,0,0,6,0,0,0,5],
   [0,4,0,9,1,5,0,7,2],
   [0,6,7,0,8,0,4,0,0],
   [0,0,0,3,0,0,1,0,0],
   [0,7,0,8,9,0,0,2,3],
   [0,0,0,0,0,4,0,0,0]]# Compléter la définition de S


def ligne(S:list,i:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 qui apparaissent à la ligne i.
    Test :
    >>> ligne(S,0)
    [1,7,8]

    """
    l = []
    for j in range(len(S)-1):
        if S[i][j] != 0:
            l.append(S[i][j])
    return l


def colonne(S:list,j:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 qui apparaissent dans la colonne j.
    Test :
    >>> colonne(S,0)
    [1]

    """
    l = []
    for i in range(len(S)-1):
        if S[i][j] != 0:
            l.append(S[i][j])
    return l


def bloc(S:list,a:int,b:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 qui apparaissent dans le bloc 3×3 auquel appartient
    la case de la ligne 𝑖 et de la colonne 𝑗
    Test :
    >>> bloc(S,3,4)
    [6,9,1,5,8]
    """
    l = []
    # Test
    if a <= 8:
        i = 6
    if a <= 5:
        i = 3
    if a <= 2:
        i = 0

    if b <= 8:
        j = 6
    if b <= 5:
        j = 3
    if b <= 2:
        j = 0

    for a in range(i,i + 3):
        for b in range(j,j + 3):
            if S[a][b] != 0:
                l.append(S[a][b])
    return l


def possibles(S:list,i:int,j:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 que l'on peut écrire dans la case  de la ligne i et de la colonne j
    (en tenant compte des règles du jeu)
    Test:
    >>> possibles(S,0,0)
    [2,3,4,6,9]
    """

    N = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
    l = ligne(S,i)
    c = colonne(S,j)
    blo = bloc(S,i,j)
    setN = set(N)
    setL = set(l)
    setC = set(c)
    setBlo = set(blo)

    res = list(setN - setL - setC - setBlo)


    print(res)

### Tien voila mon possible j'ai reussi à le faire lvdm il marche je suis trop heureux il est 2H du mat et j'ai ptn de reussi GUIGUI ON VA Y ARRIVER !!!!!

def suivante(i:int,j:int)->tuple:
    """
    Reçoit en paramètre la ligne i et la colonne j et qui renvoie le tuple (ligne,colonne) de la case suivante.
    Test :
    >>> suivante(0,0),suivante(0,8),suivante(8,8)
    (0,1),(1,0),(9,0)
    """
    l = ligne(S,i)
    c = colonne(S,j)

    if i > 9:
        print("Action impossible, recommencer")


    if j > 8:
        print("Action impossible, recommencer")
    elif j == 8:
        j = 0
        i = i + 1
    elif j < 8:
        j = j+1

    print('(',i,',',j,')')
   
  
### Tien mon pote j'ai aussi fait suivante il est 2h06 du mat et jsuis crevé si sa te dérange pas de faire le reste jveux bien ou jferais tkt juste dit moi stp
### En vrai on a fait un taf de dingue à deux donc niquel 


## Réponse Exercice 7:

# 1. Booléans , True or False.

# 2. Je sais pas

# 3. Au debut au if i == 9:

# 4. Je sais pas


def resoudre(S:list,i:int,j:int):
    """
    Indique si la grille passée en paramètre est globalement résolue à partir de la case (i,j)
    """
    p = possibles(S,i,j)
    if i == 9:
        print("La grille est globalement résolue")
    elif i == i and j == j:
        return p + 1
    else:
        for i in k:
            return 
         
 ## Pour les reponse d'exercice 7 et le truc résoudre j'ai pas reussi donc voila j'ai essayé de tout faire dsl

def resoudre(Grille:list,i:int,j:int):
    """Resolution recursive en place de la Grille à partir de la case (i,j) """
    if i == 9:
        return ("La Grille est globalement résolue")
    elif Grille[i][j] != 0:
        resoudre(Grille,suivante(i,j)[0],suivante(i,j)[1])
    elif Grille[i][j] == 0:
        for k in possibles(Grille,i,j):
            Grille[i][j] = k
            if suivante(i,j) == (9,9):
                return ("La Grille est globalement complétée")
        Grille[i][j] = 0
        return ("La Grille n'est pas globalement résolue")
            
# Test
print(resoudre(S,1,1))
print(S) 


# EMC https://www.canva.com/design/DAFOVgHSPuY/6Fp2I1ipXb3L7ZZf27VTCQ/edit?utm_content=DAFOVgHSPuY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton



















