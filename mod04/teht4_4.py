#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. 
#Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

#kysytään vuosi, ja selvitetään voiko sen jakaa neljällä. 
#jos voidaan, hyväksytään se heti jos sitä ei voi jakaa sadalla. 
#jos sen voi jakaa sadalla, jaetaan se vielä neljälläsadalla. 
#jos sen voi jakaa, hyväksytään se, muutoin hylätään se.

vuosi = int(input("Anna vuosi: "))
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Vuosi on karkausvuosi.")
        else:
            print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")