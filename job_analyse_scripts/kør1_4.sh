#!/bin/bash

cd 'trin1_samlet_korpus'
python3 Korpus_samler.py

cd ..

cd 'trin2_stopord'
python3 Stopord.py

cd ..

cd 'trin3_Frekvensliste'
python3 Frekvensliste.py

cd ..

cd 'trin4_lemma_token'
python3 Lemma_token.py

read -p "Alle scripts er nu kørt færdige. Tryk på enter for at afslutte..."
