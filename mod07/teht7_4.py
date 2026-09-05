#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa listassa olevien lukujen summan. 
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

luvut = []

def lista_summa(lista):
    summa = 0
    for i in range(0, len(lista)):
        summa = summa + lista[i]
    return summa

def luvunotto():
    while True:
        x = input("Anna kokonaisluku listaan, tai päätä ja tulosta listan summa tyhjällä rivillä. ")
        if x == "":
            break
        try:
            x = int(x)
        except ValueError:
            print("Syöte ei ole kokonaisluku!")
            continue
        break
    return x

syotto = luvunotto()

while syotto != "":
    luvut.append(syotto)
    syotto = luvunotto()

print(f"Listan alkioiden summa on {lista_summa(luvut)}")