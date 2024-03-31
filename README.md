# Webová aplikácia
Tento repozitár obsahuje zdrojový kód webovej aplikácie, ktorá slúži ako to-do list

# Komponenty
Web - frontend - html, css.
    - backend - Python Flask.
Databáza - PostgreSQL
Databáza pgAdmin - Správa PostgreSQL

# Spustenie kontajnerov v termináli
python start-app.py

# Zastavenie služieb v termináli
python end-app.py

# Spustenie aplikácie vo webovom prehliadači
localhost:5000 - aplikácia
localhost:443 - prostredie pgAdmin

# Popis aplikácie
Aplikácia slúži ako to-do list, ktorý umožňuje používateľovi pridávať nové úlohy (tasky), po kliknutí na nich možnosť presúvania do kategórií doing, resp. done. 
Z kategórie done je taktiež možné task opäť vrátiť do doing. 
Jednotlivé tasky je možné mazať. 
Nové tasky je možné pridať iba ak ešte nie sú zadané.

# Databáza
Databáza (a tabuľka v nej) bola vytvorená v prostredí pgAdmin. 
V prostredí je taktiež možné sledovať všetky záznamy.
