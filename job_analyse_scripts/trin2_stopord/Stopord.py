import os, re
from path_finder import path_finder
from tegnfjerner import tegnfjerner

cwd = os.getcwd()

path = path_finder()

with open (cwd+'/stopord.txt', 'r', encoding="utf8") as f:
    stopord = f.read()

with open (path+'/trin1_samlet_korpus/Resultat_samlet_korpus/samlet_tekst.txt', 'r', encoding="utf8") as f:
    tekst = f.read()

tekst = tegnfjerner(tekst)

lower_tekst = tekst.lower()
tekst_liste = lower_tekst.split()

lower_stopord = stopord.lower()
stopord_liste = lower_stopord.split()


# Fjern stopord og links

no_stop_words = []

for i in tekst_liste:
    if "http" not in i:
        pass
        if i not in stopord_liste:
            no_stop_words.append(i)

streng = ' '.join(no_stop_words)

ingen_stopord = open(str(cwd)+'/Resultat/ingen_stopord.txt', 'w', encoding="utf8")
ingen_stopord.write("" + streng)
ingen_stopord.close()


print("""
stopord.py          færdig""")
