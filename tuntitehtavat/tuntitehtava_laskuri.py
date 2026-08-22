paiva = float(input("Kuinka monta päivää: ")) #otetaan käyttäjän syöte, ja muovataan heti samassa rivissä float muotoon.
sec = paiva * 86400 #lasketaan sekunnit kertolaskulla
print("Annettu määrä päiviä sekunteina: " + str(sec)) #tulostetaan vastaus. pystyisin myös yksinkertaistamaan vielä tekemällä ", sec) pelkästään + merkin ja str muovauksen sijaan