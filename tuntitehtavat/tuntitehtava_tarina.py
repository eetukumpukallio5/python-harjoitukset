#tarvittavat muuttujat ja niihin kerätään tiedot käyttäjältä
nimi = input("Anna nimi: ")
adjektiivi = input("Anna adjektiivi: ")
kello = input("Anna kellon aika: ")

#tarina itsessään, käytin sekä + ja , merkkiä joko merkkien suoraan liittämiseen tai välin luomiseen
print("Olipa kerran", nimi + ".\n" + nimi, "kuuli kello", kello, "ovikellon soivan. Se oli pizzakuski.\nPizza oli yhtä", adjektiivi, "kuin", nimi, "oli tilannutkin.\n" + nimi, "oli hyvin tyytyväinen ja antoi tipin kuskille.")