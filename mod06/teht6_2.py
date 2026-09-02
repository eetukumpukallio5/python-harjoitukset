#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

#kerätään lukuja silmukassa ja lisätään ne listaan, kunnen silmukka päättyy tyhjällä syötteellä. käytetään sort-metodia reversella ja tulostataan 5 ensimmäistä lukua.

luvut = []

while True:
    luku = input("Syötä luku, tai päätä syöttäminen syöttämällä tyhjä rivi.\n")
    try:
        luku = float(luku)
    except ValueError:
        if luku == "":
            break
        else:
            print("Syöte ei ole numero eikä tyhjä!")
            continue
    break

while luku != "":
    luvut.append(luku)
    while True:
        luku = input("Syötä luku, tai päätä syöttäminen syöttämällä tyhjä rivi.\n")
        try:
            luku = float(luku)
        except ValueError:
            if luku == "":
                break
            else:
                print("Syöte ei ole numero eikä tyhjä!")
                continue
        break

luvut.sort(reverse=True)
#katsotaan listan lukujen määrä. jos ei yhtään lukua, ei tulosteta mitään. jos jotain lukuja mutta alle 5, tulostetaan kaikki. muutoin tulostetaan suurimmat 5.
if 0 < len(luvut) < 5:
    print(f"Listan {len(luvut)} suurinta lukua ovat {luvut}.")
elif len(luvut) >= 5:
    print(f"Listan 5 suurinta lukua ovat {luvut[:5]}.")