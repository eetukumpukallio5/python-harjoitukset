vuosi = int(input("Anna vuosi: "))

#and vaiheessa selvitetään ensin neljällä jaollisuus, ja sitten poistetaan != argumenteilla perutut olympialaiset neljällä jaollisista.
#or argumentilla otetaan ainoa poikkeava vuosiluku, 2021, jota ei saa neljällä jaolla.

if vuosi % 4 == 0 and vuosi != 1916 and vuosi != 1940 and vuosi != 1944 and vuosi != 2020 or vuosi == 2021: 
    print("Oli olympiavuosi.")
else:
    print("Ei ollut olympiavuosi.")