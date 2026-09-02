#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

#otetaan kokonaislukuna heitettävien noppien määrä, ja käytetään numeroa for rakenteessa silmukoiden määrää varten. lisätään aina heitettyämme noppaa tulos muuttujaan, joka tulostetaan lopuksi.
import random
summa = 0

while True:
    heitot = input("Anna heitetävien noppien määrä. ")
    try:
        heitot = int(heitot)
    except ValueError:
        print("Syötteen täytyy olla kokonaisluku.")
        continue
    break

for n in range(heitot): #n lähtee arvosta 0, ja aina silmukan lopussa nousee yhden itsekseen. kun saapuu heitot arvoon, pysäyttää toiston.
    summa = summa + random.randint(1, 6)

print(f"Heittojen summa on {summa}.")