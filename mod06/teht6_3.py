#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

#otetaan validi kokonaisluku käyttäjältä, ja for silmukkaa käyttäen jaetaan luku luvusta 2 lähtien, päättyen lukuun ennen syötettä. esim luvussa 23 välillä 2-22.
#jakojäännöksellä selvitetään onko luku jaollinen kyseisellä luvulla.

while True:
    luku = input("Anna kokonaisluku. ")
    try:
        luku = int(luku)
    except ValueError:
        print("Syöte ei ole kokonaisluku!")
        continue
    break

for n in range(2, luku):
    if luku % n == 0:
        print("Luku ei ole alkuluku.")
        break
else:
    print("Luku on alkuluku!")