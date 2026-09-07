#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. 
#Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
#Käytä joukkotietorakennetta nimien tallentamiseen.¨

nimet = set() #luodaan joukko. tallentaa sattumanvaraiseen järjestykseen alkioon ja ei hyväksy enempää kuin yhden tapauksen alkiota.
syote = str(input("Anna uusi nimi listaan! "))

while syote != "":
    if syote in nimet:
        print("Aiemmin syötetty nimi!")
    else:
        print("Uusi nimi!")
        nimet.add(syote)
    syote = str(input("Anna uusi nimi listaan! "))

for i in nimet:
    print(i)