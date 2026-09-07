#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
#Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

while True:
    kuukausi = input("Anna kuukauden numero. ")
    try:
        kuukausi = int(kuukausi)
    except ValueError:
        print("Syötteen täytyy olla kokonaisluku.")
        continue
    if kuukausi == 12 or 0 < kuukausi < 3:
        print(f"Kuukautesi vuodenaika on {vuodenajat[0]}!")
    elif 2 < kuukausi < 6:
        print(f"Kuukautesi vuodenaika on {vuodenajat[1]}!")
    elif 5 < kuukausi < 9:
        print(f"Kuukautesi vuodenaika on {vuodenajat[2]}!")
    elif 8 < kuukausi < 12:
        print(f"Kuukautesi vuodenaika on {vuodenajat[3]}!")
    else:
        print("Virheellinen syöttö!")
        continue
    break