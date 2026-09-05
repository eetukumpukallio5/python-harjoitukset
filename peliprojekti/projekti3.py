#luodaan päävalikkoon tarvittavat funktiot.
def lisaa_listaan(lista):
    lista.append(input("Mitä lisäät inventaarioon? "))
    print("Lisätty.")

def katso_lista(lista):
    print(lista)

def juo_vetta(lista):
    if "vesipullo" in lista:
        print("Hyvää vettä!")
    else:
        print("Et voi juoda vettä jota sinulla ei ole!")

def rakenna(lista, kerrokset):
    if "tiili" in lista:
        print("Rakentakaamme yhden kerroksen lisää.")
        for i in range(kerrokset):
            print(r" -- ")
            print(r"|  |")
            print(r" -- ")
    else:
        print("Tarvitset tiilin rakentaaksesi.")

#otetaan tarvittavat muuttujat käyttäjältä, ja alustetaan komento muuttuja sekä inventaario.
komento = "n/a"
inventaario = []
kerrokset = 0
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
    komento = input("Valitse ja syötä komento.\n1) Lisää esine inventaarioon\n2) Katso inventaarion sisältö\n3) Juo vettä (tarvitsee vesipullon)\n4) Rakenna tornia (tarvitsee tiilin)\nlopeta) Sammuta ohjelma\n")
    if komento == "1":
        lisaa_listaan(inventaario)
    elif komento == "2":
        katso_lista(inventaario)
    elif komento == "3":
        juo_vetta(inventaario)
    elif komento == "4":
        if "tiili" in inventaario:
            kerrokset = kerrokset + 1
        rakenna(inventaario, kerrokset)
    elif komento != "lopeta":
        print("Virheellinen komento!")