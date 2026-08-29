#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
#(Oikea käyttäjätunnus on python ja salasana rules).

#kysytään käyttäjältä käyttäjätunnusta ja salasanaa, ja verrataan niitä tehtävässä annettuisiin oikeisiin merkkijonoihin.
#jos molemmat oikein, tulostetaan tervetuloa ja rikotaan silmukka. 
#virheellisestä merkkijonon syötteestä meidän ei tarvitse tässä huolehtia, ovathan käyttäjätunnus ja salasana aina kirjainten koosta riippuvaisia.

yritykset = 5

while yritykset > 0:
    kt = str(input("Syötä käyttäjätunnuksesi.\n"))
    ss = str(input("Syötä salasanasi.\n"))
    if kt == "python" and ss == "rules":
        print("Tervetuloa.")
        break
    yritykset = yritykset - 1
    if yritykset > 1:
        print(f"Väärä syöte! {yritykset} yritystä jäljellä.")
    elif yritykset == 1:
        print("Väärä syöte! 1 yritys jäljellä.")
    else:
        print("Pääsy evätty.")