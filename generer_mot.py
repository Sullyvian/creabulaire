# Génération des mots

import numpy.random as rd

# Récupération des données traitées


alphabet = 'aâàäãbcçdeéèêëfghiïîjklmnoôöpqrstuûüùvwxyz-'

# ##################################
# Dépendance de la lettre précédente
# ##################################


def generer_mot1(L1: dict[str, list[str]]) -> str:
    m = ''
    n = len(L1[''])
    l = L1[''][rd.randint(n)]
    while l != '':
        m += l
        l1 = m[-1]
        n = len(L1[l1])
        l = L1[l1][rd.randint(n)]
    return m

# #######################################
# Dépendance des deux lettres précédentes
# #######################################


def generer_mot2(L2: dict[str, dict[str, list[str]]]) -> str:
    m = ''
    n = len(L2[''][''])
    l = L2[''][''][rd.randint(n)]
    m += l
    l1 = m[-1]
    n = len(L2[''][l1])
    l = L2[''][l1][rd.randint(n)]
    while l != '':
        m += l
        l1, l2 = m[-2:]
        n = len(L2[l1][l2])
        l = L2[l1][l2][rd.randint(n)]
    return m

# ########################################
# Dépendance des trois lettres précédentes
# ########################################


def generer_mot3(L3: dict[str, dict[str, dict[str, list[str]]]]) -> str:
    m = ''
    n = len(L3[''][''][''])
    l = L3[''][''][''][rd.randint(n)]
    m += l
    l1 = m[-1]
    n = len(L3[''][''][l1])
    l = L3[''][''][l1][rd.randint(n)]
    m += l
    l1, l2 = m[-2:]
    n = len(L3[''][l1][l2])
    l = L3[''][l1][l2][rd.randint(n)]
    while l != '':
        m += l
        l1, l2, l3 = m[-3:]
        n = len(L3[l1][l2][l3])
        l = L3[l1][l2][l3][rd.randint(n)]
    return m

# #########################################
# Dépendance des quatre lettres précédentes
# #########################################


def generer_mot4(L4: dict[str, dict[str, dict[str, dict[str, list[str]]]]]) -> str:
    m = ''
    n = len(L4[''][''][''][''])
    l = L4[''][''][''][''][rd.randint(n)]
    m += l
    l1 = m[-1]
    n = len(L4[''][''][''][l1])
    l = L4[''][''][''][l1][rd.randint(n)]
    m += l
    l1, l2 = m[-2:]
    n = len(L4[''][''][l1][l2])
    l = L4[''][''][l1][l2][rd.randint(n)]
    m += l
    l1, l2, l3 = m[-3:]
    n = len(L4[''][l1][l2][l3])
    l = L4[''][l1][l2][l3][rd.randint(n)]
    while l != '':
        m += l
        l1, l2, l3, l4 = m[-4:]
        n = len(L4[l1][l2][l3][l4])
        l = L4[l1][l2][l3][l4][rd.randint(n)]
    return m


def generer_mot(L, dep: int) -> str:
    if dep == 1:
        return generer_mot1(L)
    if dep == 2:
        return generer_mot2(L)
    if dep == 3:
        return generer_mot3(L)
    if dep == 4:
        return generer_mot4(L)
    else:
        raise ValueError("La dépendance doit être comprise entre 1 et 4")
