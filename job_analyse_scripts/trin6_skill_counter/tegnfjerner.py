import re

def tegnfjerner(tekst):
    set_tekst = set(tekst)
    sorted_set = sorted(set_tekst, key=str.lower)
    streng = ' '.join(sorted_set)
    rens = re.sub('[a-zA-ZæøåÆØÅ-]', '', streng)
    tegnliste = rens.split()

    for i in tekst:
        if '\\' not in tegnliste:
            tekst = re.sub('\\\\', '', tekst)
        if i in tegnliste:
            tekst = tekst.replace(i, '')
        else:
            pass

    return tekst
