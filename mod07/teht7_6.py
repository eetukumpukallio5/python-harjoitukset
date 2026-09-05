#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
#Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def yksikköhinta(halkaisija, euro):
    return (math.pi * halkaisija) / euro

cm1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä. "))
euro1 = float(input("Anna ensimmäisen pizzan hinta euroina. "))
yh1 = yksikköhinta(cm1, euro1)

cm2 = float(input("Anna toisen pizzan halkaisija senttimetreinä. "))
euro2 = float(input("Anna toisen pizzan hinta euroina. "))
yh2 = yksikköhinta(cm2, euro2)

if yh1 > yh2:
    print("Ensimmäinen pizza antaa parempaa vastinetta rahalle.")
elif yh2 > yh1:
    print("Toinen pizza antaa parempaa vastinetta rahalle.")
else:
    print("Pizzat ovat yhtä hyvää vastinetta.")