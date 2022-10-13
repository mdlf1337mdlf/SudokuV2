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
    NOMBRES = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
    l = ligne(i)
    c = colonne(j)
    temp = []
    for x in l:
        if x in NOMBRES:
            temp.append(x)
    for y in c:
        if c in NOMBRES and c not in temp:
            temp.append()


























