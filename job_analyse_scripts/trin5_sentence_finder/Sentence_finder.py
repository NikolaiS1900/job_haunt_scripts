import os, re, difflib
from nltk.tokenize import sent_tokenize
from tegnfjerner import tegnfjerner
from path_finder import path_finder

cwd = os.getcwd()
path = path_finder()


with open (path+'/trin1_samlet_korpus/Resultat_samlet_korpus/samlet_tekst.txt', 'r', encoding="utf8") as f:
    korpus_tekst = f.read()

# Denne funktioner forbereder det samlede korpus, ved at dele sætningerne op via NLTK's sent_tokenizer.
# Så bruger den tjegnfjerner, til at rense for alle unøskede tegn.
def forbered(tekst):

    lower_tekst = tekst.lower()

    sætninger = sent_tokenize(lower_tekst)

    sætninger = set(sætninger)

    sætninger = '\n \n'.join(sætninger)

    sætninger = tegnfjerner(sætninger)

    rens = re.sub(' +', ' ', sætninger)

    ny_liste = rens.split('\n \n')
    
    return ny_liste


liste_sætninger = forbered(korpus_tekst)
liste_sætninger2 = ' '.join(liste_sætninger)
liste_sætninger2 = liste_sætninger2.split()

søgeord = input("skriv dit søgeord: ").lower()

# Denne funktion finder eksempler

def eksempelfinder(search):
    sorteret_liste = []

    for i in liste_sætninger:
        if search in i:
            sorteret_liste.append(i)

    nice_liste = '\n \n_* '.join(sorteret_liste)
    return nice_liste


# Denne funktion benytter en spellchecker

def ordgætter():

    suggestion = difflib.get_close_matches(søgeord, liste_sætninger2)
    print(f'{søgeord} ej fundet.\nAndet søgeforslag:   {", ".join(str(x) for x in set(suggestion))}')
    indput1 = input('\nVil du forsætte søgningen, så skriv "ja", ellers skriv noget andet for at stoppe: ').lower()
    if indput1 == "ja":
        indput2 = input('\nSkriv det ord eller den specifikke form du vil søge på: ').lower()
        print("Du har søgt på {indput2}, her er resultatet")
        print("__________________________________________\n \n")
        indput2_rens = forbered(indput2)
        search_word = ' '.join(indput2_rens)
        search = eksempelfinder(search_word)
        print(search)
    else:
        print("stopper script")
        exit()


def tjekker():
    word = søgeord
    
    if word in liste_sætninger2:
        return eksempelfinder(word)
    if word not in liste_sætninger2:
        return ordgætter()

start = tjekker()
print(start)


