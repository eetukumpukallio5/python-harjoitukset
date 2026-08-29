#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#luodaan aluksi muuttujat pienimälle ja suurimalle luvulle, ja laitetaan aluksi arvoiksi n/a siinä tapauksessa että käyttäjä välittömästi päättää ohjelman ja mennään tulostukseen.
#jos saamme numeron tyhjän sijaan, asetetaan se välittömästi sekä pienimmäksi ja suurimmaksi. 
#vasta ensimmäisen syötteen käsittelyn päätteksi edetään while silmukkaan. 
#kun aloitamme toisessa silmukassa ja syöte on tyhjä, menemme koodin loppuun jossa tulostamme pienimmän ja suurimman luvun.

pienin = "n/a"
suurin = "n/a"

while True:
    syote = input("Syötä luku, tai päätä syöttäminen syöttämällä tyhjä rivi.\n")
    try:
        syote = float(syote)
    except ValueError:
        if syote == "":
            break
        else:
            print("Syöte ei ole numero eikä tyhjä!")
            continue
        #käytimme try komentoa, jossa koetimme aluksi saammeko muunnettua syötteen liukuluvuksi, jolloin meillä olisi numero syötteenä.
        #jos ei ole numero, saisimme valueerrorin, jonka saatuamme except kohta pyörii. jos syöte on tyhjä, rikomme silmukan.
        #jos ei tyhjä kyseessä on epämääräinen merkkijono, joka ei palvele tarpeitamme. 
        #tällöin continue komennolla skippaamme sen jälkeisen break komennon, ja palaamme silmukan alkuun kysymään numeroa ja tarkistamaan syötteen uudelleen.
    pienin = syote
    suurin = syote
    break
    #pääsemme tähän loppuosioon ainoastaan liukuluvuksi muuntamisen onnistuttua, joten muuttujiin tulee ainoastaan numeroita.
    #jos syöte oli nyt tyhjä, pienin ja suurin siis yhä ovat n/a.

while syote != "":
    if syote > suurin:
        suurin = syote
    elif syote < pienin:
        pienin = syote #jos olisimme ensimäisessä silmukassa jättänyt asettamatta syötettä näihin, vertaisimme nyt kaikkia numeroita merkkijonoon
    while True: #sisäinen silmukka uuden luvun keräämiseen ja mahdolliseen toistoon vikasyöte tilanteissa
        syote = input("Syötä luku, tai päätä syöttäminen syöttämällä tyhjä rivi.\n")
        try:
            syote = float(syote)
        except ValueError:
            if syote != "": #jos merkkirivi tyhjä, menee numeroiden kanssa break komentoon. alin while taso lopettaa toiston lopuksi
                print("Syöte ei ole numero eikä tyhjä!")
                continue
        break

print(f"Pienin luku on:\n{pienin}")
print(f"Suurin luku on:\n{suurin}")