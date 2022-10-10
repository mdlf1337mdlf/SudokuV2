S=[[0,1,0,0,7,8,0,0,0],
   [0,8,0,0,4,0,9,0,0],
   [0,0,5,6,0,0,0,1,0],
   [1,0,0,0,6,0,0,0,5],
   [0,4,0,9,1,5,0,7,2],
   [0,6,7,0,8,0,4,0,0],
   [0,0,0,3,0,0,1,0,0],
   [0,7,0,8,9,0,0,2,3],
   [0,0,0,0,0,4,0,0,0]] # Compléter la définition de S


def colonne(S:list,j:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 qui apparaissent à la ligne i.
    Test :
    >>> colonne(S,0)
    [1]

    """
    l = []
    for i in range(len(S)-1):
        if S[i][j] != 0:
            l.append(S[i][j])
    return l

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

def bloc(S:list,i:int,j:int)->list:
    """
    Retourne la liste des chiffres de 1 à 9 qui apparaissent dans le bloc 3×3 auquel appartient
    la case de la ligne 𝑖 et de la colonne 𝑗
    Test :
    >>> bloc(S,3,4)
    [6,9,1,5,8]
    """
    









