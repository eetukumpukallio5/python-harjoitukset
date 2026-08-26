#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. 
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

#melko yksinkertainen tehtävä, kysytään hyttiluokka käyttäjältä ja if-else rakenteella koetetaan eri vaihtoehtoja yksi kerrallaan.

hytti = (str(input("Anna hyttiluokkasi: "))).upper() #hieman edistyneempi komento tässä vaiheessa, mutta muuntaa käyttäjän syötteen isoiksi kirjaimiksi. koska pythonia kiinnostaa onko stringi minkälaisissa kirjaimissa, tämä tekee syötteen käsittelystä huomattavasti siistimpää.

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")