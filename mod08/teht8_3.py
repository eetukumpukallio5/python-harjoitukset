#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
#Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
#Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
#Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
#Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
#Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
#ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

#luodaan päävalikko, joka jokaisella toistolla kysyy komennon listasta. komennon perustella pyöritetään vastaava funktio.

lentoasemat = {}

#hyväksytään ainoastaan valikossa sallittavat arvot, eli 1, 2 ja 3.
def ota_komento():
    print("Tervetuloa käsittelemään lentoasematietoja. Anna valintasi.\n1) Syötä uuden lentooaseman tiedot\n2) Hae lentoasemaa ICAO-koodilla\n3) Lopeta ohjelma")
    while True:
        x = input()
        if x != "1" and x != "2" and x != "3":
            print("Virheellinen komento.")
            continue
        break
    return x

#lentoaseman tietojen kerääminen. tallentaa samanaikaisesti annettuun sanakirjaan tiedot.
def uusi_lentoasema(lista):
    print("Anna uuden lentoaseman nelikirjaiminen ICAO-koodi.")
    while True:
        icao = input("")
        if len(icao) != 4:
            print("Koodin tulee olla nelikirjaiminen. Syötä uudelleen.")
            continue
        break
    icao = icao.upper()
    print("Koodi hyväksytty. Anna lentoaseman nimi.")
    while True:
        lentoasema = input("")
        if lentoasema == "":
            print("Lentoaseman nimi ei voi olla tyhjä. Syötä uudelleen.")
            continue
        break
    lista[icao] = lentoasema
    print("Lentoasema lisätty hakemistoon.")

#oma valikkonsa. toistuu syötettyään koodin. palaa päävalikkoon syöttämällä tyhjän rivin
def hae_lentoasema(lista):
    print("Tervetuloa hakuohjelmaan. Kirjoita nelikirjaiminen ICAO-koodi hakeaksesi, tai palaa päävalikkoon syöttämällä tyhjä rivi.")
    while True:
        syote = input("")
        if syote == "":
            break
        syote = syote.upper()
        if syote in lista:
            print(f"Löytyi! Koodin {syote} lentoasema on {lista[syote]}.\nHae uudelleen, tai päätä haku tyhjällä rivillä.")
        else:
            print("Syötettä ei löytynyt listasta.\nHae uudelleen, tai päätä haku tyhjällä rivillä.")

komento = ota_komento()

while komento != "3":
    if komento == "1":
        uusi_lentoasema(lentoasemat)
    else:
        hae_lentoasema(lentoasemat)
    komento = ota_komento()
else:
    print("Ohjelma sulkeutuu. Kiitos käytöstä.")