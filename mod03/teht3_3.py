#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
#Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
#melko itseselitteinen tehtävän anto, selvitetään kanta ja korkeus. näitten perusteella tehdään tarvittavat laskut. pinta-ala on pelkästään kanta kerrottuna korkeudella

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

print(f"Suorakulmion piiri on {(kanta * 2 + korkeus * 2):.5f} ja pinta-ala on {(kanta * korkeus):.5f}")
#rajoitin harjoituksen nimissä desimaalit viiden tarkkuuteen