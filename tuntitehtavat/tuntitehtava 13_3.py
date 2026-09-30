nimi = input("Tiedoston nimi: ")
try:
    with open(nimi, "r") as tiedosto:
        data = tiedosto.read()
        print(data)
except:
    print("Tiedostoa ei löydy, yritä uudelleen!")