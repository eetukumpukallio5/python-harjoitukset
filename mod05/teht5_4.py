#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

#arvotaan satunnainen luku 1-10 välillä, jonka jälkeen edetään while silmukkaan, jossa kysytään käyttäjältä arvausta satunnais luvun arvosta.
#saadessamme hyväksyttävän kokonaisluvun vertaamme sitä satunnaislukuun. 
#tulostamme vertailun perusteella vastauksen, ja jos arvaus oli oikein tulostuksen jälkeen rikomme silmukan.
#lopuksi tulostetaan myös arvausten määrä.

import random
satluku = random.randint(1, 10)
yritykset = 1

while True:
    while True:
        arvaus = input("Anna arvauksesi kokonaislukuna.\n")
        try:
            arvaus = int(arvaus)
        except ValueError:
            print("Syöte ei ole kokonaisluku!")
            continue
        break
    if arvaus > satluku:
        print("Arvaus on liian suuri.")
    elif arvaus < satluku:
        print("Arvaus on liian pieni.")
    else:
        print("Arvaus on oikein!")
        break
    yritykset = yritykset + 1

if yritykset == 1:
    print("Sait ensimmäisellä oikein, onnittelut!")
else:
    print(f"Onnistuminen vaati {yritykset} yritystä.")