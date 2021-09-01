@echo off
@cd %DIR%

cd trin1_samlet_korpus

@py.exe Korpus_samler.py %*

cd ..

cd trin2_stopord
@py.exe Stopord.py

cd ..

cd trin3_Frekvensliste
@py.exe Frekvensliste.py

cd ..

cd trin4_lemma_token
@py.exe Lemma_token.py 

echo All scripts are now done running
@pause

Rem Batch-script lavet af Nikolai Sandbeck
