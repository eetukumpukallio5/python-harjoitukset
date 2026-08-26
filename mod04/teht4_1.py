#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. 
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

#kysytään kuhan pituus, ja if-else rakenteella tulostetaan syötteen perusteella vastaus.

kuha = float(input("Anna kuhan pituus senttimetreinä: "))
if kuha > 0:
    if kuha < 37:
        print("Kuha on alamittainen, laske se takaisin järveen. Alimmasta sallitusta pyyntimitasta jäi", 37 - kuha, "senttimetriä.")
    else:
        print("Kuha täyttää pyyntimitan, onnittelut!")
else:
    print("Vikasyöttö!") #emme halua että käyttäjä syöttäisi negatiivisia lukuja, joten ohjelma tulostaa tämän jos pituus ei ole positiivinen.