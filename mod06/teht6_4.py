#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. 
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
#käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

#ensimmäisessä silmukassa käytetään for rakennetta, kysytään yksi kaupunki kerrallaan. ei tarvetta merkkien tarkistamiseen tällä kertaa. toisessa käytetään for/in silmukkaa, tulostetaan yksi kaupunki yhdessää silmukassa.
kaupungit = []

for n in range(5):
    kaupungit.append(input("Anna listaan kaupunki. "))

for n in (kaupungit):
    print(n) #n on tässä tapauksessa sama kuin alkio. ensimmäisellä toistolla tämä on ensimmäinen listan alkio, toisella toinen yms...