import random

#otetaan tarvittavat muuttujat käyttäjältä, ja alustetaan komento muuttuja.
komento = "n/a"
nimi = input("Anna nimesi.\n")
while True:
    ika =  input("Anna ikäsi.\n")
    try:
        ika = float(ika)
    except ValueError:
        print("Iän täytyy olla numero.")
        continue
    break

#tarkistetaan ikä, ja jos alle 12 while loopin argumentti epäonnistuu ja päättää ohjelman
if ika >= 12:
    print(f"Tervetuloa, {nimi}!")
    print(r" ____ _   _ _   _            _ _ _    _         ")
    print(r"|  _ (_)_(_|_)_(_)_   ____ _| (_) | _| | _____  ")
    print(r"| |_) / _` |/ _` \ \ / / _` | | | |/ / |/ / _ \ ")
    print(r"|  __/ (_| | (_| |\ V / (_| | | |   <|   < (_) |")
    print(r"|_|   \__,_|\__,_| \_/ \__,_|_|_|_|\_\_|\_\___/ ")
else:
    print("Sinun täytyy olla vähintään 12-vuotias pelataksesi.")
    komento = "lopeta"

#yksinkertainen silmukka päävalikolle
while komento != "lopeta":
    komento = input("Valitse ja syötä komento.\n1) Heitä 20 puoleinen noppa\n2) Tulosta kissa\nlopeta) Sammuta ohjelma\n")
    if komento == "1":
        print(f"Tulos on {random.randint(1, 20)}!")
    elif komento == "2":
        print(r"    /\_/\           ___")
        print(r"   = o_o =_______    \ \  ")
        print(r"    __^      __(  \.__) )")
        print(r"  <_____>__(_____)____/")
    elif komento != "lopeta":
        print("Virheellinen komento!")