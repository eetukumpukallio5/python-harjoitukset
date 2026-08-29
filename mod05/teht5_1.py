#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

#otetaan muuttujaan aluksi luku 1, ja while silmukassa tarkastellaan jokaisella toistolla jääkö kolmella jaettaessa jakojäännös. 
#jos ei, tulostetaan luku. lopuksi lisätään yksi luku muuttujaan. 
#tehdään toistoa kunnes olemme ylittäneet luvun 1000.

luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku = luku + 1