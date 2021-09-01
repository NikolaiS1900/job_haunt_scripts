#!/bin/bash

cd 'trin1_samlet_korpus/Resultat_samlet_korpus'
rm *.txt

cd ../..

cd 'trin2_stopord/Resultat'
rm *.txt

cd ../..

cd 'trin3_Frekvensliste/Resultat'
rm *.txt

cd ../..

cd 'trin4_lemma_token/Resultat'
rm *.txt



read -p "Alle tekstfiler er nu slettet, bortset fra dem i mappen Data i første trin. Tryk på enter for at afslutte..."
