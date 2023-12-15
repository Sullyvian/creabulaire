# Extraction, traitement et stockage des données


with open('gutenberg.txt', 'r', encoding='utf-8') as f:
    mots = f.read().lower().split('\n')

alphabet = 'aâàäãbcçdeéèêëfghiïîjklmnoôöpqrstuûüùvwxyz-'


def proba_dico1() -> dict[str, dict[str, int]]:
    '''renvoie un dico de dico d'entiers tel que d[a][b] renvoie le nombre d'occurence du motif ab dans la base de donnée'''
    d = {i: {j: 0 for j in alphabet} for i in alphabet}
    d[''] = {i: 0 for i in alphabet}
    for i in d.keys():
        d[i][''] = 0
    for mot in mots:
        n = len(mot)
        d[''][mot[0]] += 1
        for i in range(n-1):
            d[mot[i]][mot[i+1]] += 1
        d[mot[-1]][''] += 1
    return d


def proba_liste1() -> dict[str, list[str]]:
    '''renvoie un dico de listes tel que d[a] soit la liste des lettres (avec répétitions) suivant a dans les mots de la base de donnée'''
    d = {i: [] for i in alphabet}
    d[''] = []
    for mot in mots:
        n = len(mot)
        d[''].append(mot[0])
        for i in range(n-1):
            d[mot[i]].append(mot[i+1])
        d[mot[-1]].append('')
    return d


def proba_liste2() -> dict[str, dict[str, list[str]]]:
    '''renvoie un dico de dico de listes tel que d[a][b] soit la liste des lettres (avec répétitions) suivant ab dans les mots de la base de donnée'''
    d = {i: {j: [] for j in alphabet} for i in alphabet}
    d[''] = {i: [] for i in alphabet}
    d[''][''] = []
    for mot in mots:
        n = len(mot)
        if n >= 2:
            d[''][''].append(mot[0])
            d[''][mot[0]].append(mot[1])
            for i in range(n-2):
                d[mot[i]][mot[i+1]].append(mot[i+2])
            d[mot[-2]][mot[-1]].append('')
    return d


def proba_liste3() -> dict[str, dict[str, dict[str, list[str]]]]:
    '''renvoie un dico de dico de dico de listes tel que d[a][b][c] soit la liste des lettres (avec répétitions) suivant abc dans les mots de la base de donnée'''
    d = {i: {j: {k: [] for k in alphabet} for j in alphabet} for i in alphabet}
    d[''] = {i: {j: [] for j in alphabet} for i in alphabet}
    d[''][''] = {i: [] for i in alphabet}
    d[''][''][''] = []
    for mot in mots:
        n = len(mot)
        if n >= 3:
            d[''][''][''].append(mot[0])
            d[''][''][mot[0]].append(mot[1])
            d[''][mot[0]][mot[1]].append(mot[2])
            for i in range(n-3):
                d[mot[i]][mot[i+1]][mot[i+2]].append(mot[i+3])
            d[mot[-3]][mot[-2]][mot[-1]].append('')
    return d


def proba_liste4() -> dict[str, dict[str, dict[str, dict[str, list[str]]]]]:
    '''renvoie un dico de dico de dico de dico de listes tel que d[a][b][c] soit la liste des lettres (avec répétitions) suivant abcd dans les mots de la base de donnée'''
    d = {i: {j: {k: {l: [] for l in alphabet} for k in alphabet}
             for j in alphabet} for i in alphabet}
    d[''] = {i: {j: {k: [] for k in alphabet}
                 for j in alphabet} for i in alphabet}
    d[''][''] = {i: {j: [] for j in alphabet} for i in alphabet}
    d[''][''][''] = {i: [] for i in alphabet}
    d[''][''][''][''] = []
    for mot in mots:
        n = len(mot)
        if n >= 4:
            d[''][''][''][''].append(mot[0])
            d[''][''][''][mot[0]].append(mot[1])
            d[''][''][mot[0]][mot[1]].append(mot[2])
            d[''][mot[0]][mot[1]][mot[2]].append(mot[3])
            for i in range(n-4):
                d[mot[i]][mot[i+1]][mot[i+2]][mot[i+3]].append(mot[i+4])
            d[mot[-4]][mot[-3]][mot[-2]][mot[-1]].append('')
    return d


def proba_liste(dep: int):
    if dep == 1:
        return proba_liste1()
    elif dep == 2:
        return proba_liste2()
    elif dep == 3:
        return proba_liste3()
    elif dep == 4:
        return proba_liste4()
    else:
        raise ValueError("La dépendance doit être comprise entre 1 et 4")
