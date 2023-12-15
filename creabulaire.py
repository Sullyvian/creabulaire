import sys

import proba_liste
import generer_mot

def usage()-> None:
    print("\nUsage: python3 creabulaire.py [nb_mots] [dep]")
    print("---------------------------------------------")
    print("nb_mots: int")
    print("\t| nombre de mots à générer")
    print("\t| OBLIGATOIRE")
    print("dep: int (0 < dep < 5)")
    print("\t| nombre de lettres utilisées pour générer la suivante")
    print("\t| OPTIONEL (par défaut 4)")

argv = sys.argv
nb_mots = 1
dep = 4

if len(argv) == 2:
    nb_mots = int(argv[1])
elif len(argv) == 3:
    nb_mots = int(argv[1])
    dep = int(argv[2])
else:
    usage()
    sys.exit(1)

L = proba_liste.proba_liste(dep)

for i in range(nb_mots):
    print(generer_mot.generer_mot(L, dep))
