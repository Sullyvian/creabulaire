# Créabulaire

Ce projet contient des scripts Python pour générer des mots semblables à des mots français.

Pour cela, On étudie les fréquences d'apparition de suites de lettres de taille 1,2,3 ou 4 dans un corpus de mots français. \
On génère ensuite aléaotoirement des mots en respectant ces fréquences. \
Il est possible que les mots générés existent déjà en français.

## Fichiers

- [`creabulaire.py`](./creabulaire.py): Script principal. Utilisez-le pour générer des mots.
- [`proba_liste.py`](./proba_liste.py): Contient des fonctions pour calculer des probabilités.
- [`generer_mot.py`](./generer_mot.py): Contient des fonctions pour générer des mots.
- [`gutenberg.txt`](./gutenberg.txt): Corpus de mots français trouvés à cette [source](https://www.pallier.org/liste-de-mots-francais.html)

## Utilisation

```bash
> python3 creabulaire.py [nb_mots] [dep]
```

- `nb_mots` (entier) : Nombre de mots à générer. Ce paramètre est OBLIGATOIRE.
  
- `dep` (entier, 0 < dep < 5) : Nombre de lettres utilisées pour générer la lettre suivante. Ce paramètre est OPTIONNEL. Par défaut, sa valeur est 4.

## Exemple

### Exemple 1

Génération de 5 mots avec une profondeur de 4.

```bash
> python3 creabulaire.py 5
empêtrassiez
semontoilerons
déplacardonnassions
étallie
hydrofugeai
```

### Exemple 2

Génération de 5 mots avec une profondeur de 2.

```bash
> python3 creabulaire.py 5 2
grimmorie
cons
goûtes
grailles
fras
```

### Exemple 3

Si on ne met pas d'argument, on obtient l'aide.

```bash
> python3 creabulaire.py

Usage: python3 creabulaire.py [nb_mots] [dep]
---------------------------------------------
nb_mots: int
 | nombre de mots à générer
 | OBLIGATOIRE
dep: int (0 < dep < 5)
 | nombre de lettres utilisées pour générer la suivante
 | OPTIONEL (par défaut 4)

```

## Améliorations possibles

- Utiliser un corpus de mots plus grand
- Utiliser un corpus d'une autre langue
- Utiliser des suites de lettres de taille plus grande (arbitrairement grande si possible)
- Utiliser des suites de lettres de taille variable (par exemple, on peut utiliser une suite de 2 lettres pour générer la 3ème lettre, puis une suite de 3 lettres pour générer la 4ème lettre, etc.)
- Optimiser le code
