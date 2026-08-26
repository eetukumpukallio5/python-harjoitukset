#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

#kysytään tiedot, ja filtteröidään mahdolliset vikasyötöt. if-else rakenteella otetaan kussakin kohdassa huomioon sekä sukupuoli että hemoglobiiniarvo, ja sen perusteella joko vastataan tai edetään seuraavaan kohtaan.

sp = (str(input("Anna biologinen sukupuolesi (m/f): "))).upper()
hg = float(input("Anna hemoglobiiniarvosi (g/l): "))

if (sp == "M" or sp == "F") and hg > 0:
    if (sp == "F" and hg < 117) or (sp == "M" and hg < 134):
        print("Hemoglobiiniarvosi on alhainen.")
    elif (sp == "F" and hg > 175) or (sp == "M" and hg > 195):
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaalilla tasolla.")
else:
    print("Vikasyöttö!")