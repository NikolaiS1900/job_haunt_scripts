import glob, os, re

# Tager alle tekster i mappen data.

file_list = glob.glob(os.path.join(os.getcwd(), "Data", "*.txt"))


# Curren working directory
cwd = os.getcwd()

corpus = []

for file_path in file_list:
    with open(file_path, encoding='utf8') as f_input:
        corpus.append(f_input.read())

samlet_tekst = ' '.join(corpus)


# Laver en ny tom tekstfil ved navn "ordliste.txt", som så tilskrives variablen
# tegnliste. Den nye tekstfil oprettes i mappen Resultat.
samlet_korpus = open(str(cwd)+'/Resultat_samlet_korpus/samlet_tekst.txt', 'w', encoding="utf8")

# nu tages indholdet af variablen "samlet_tekst" og det skrives til "samlet_korpus".
samlet_korpus.write("" + samlet_tekst)

# Skriver en hilsen

print("""
korpus_samler.py    færdig""")
