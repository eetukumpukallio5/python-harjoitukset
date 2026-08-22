#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
#kerätään kokonaisluvut muuttujiin a b ja c, ja suoritetaan tarvittavat yhtälöt

a = int(input("Anna ensimmäinen kokonaisluku: "))
b = int(input("Anna toinen kokonaisluku: "))
c = int(input("Anna kolmas kokonaisluku: "))

print(f"Summa on {a + b + c}, tulo on {a * b * c} ja keskiarvo on {(a + b + c) / 3}")
#ei erityisempää sanottavaa koodista, keskiarvossa kuitenkin käytin sulkeita a+b+c kohdassa jotta laskujärjestys menisi oikein