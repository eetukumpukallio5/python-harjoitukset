#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

luvut = []

def luvunotto():
    while True:
        x = input("Anna kokonaisluku listaan, tai päätä ja tulosta listat tyhjällä rivillä. ")
        if x == "":
            break
        try:
            x = int(x)
        except ValueError:
            print("Syöte ei ole kokonaisluku!")
            continue
        break
    return x

def karsi_parittomat(lista):
    toista = True
    while toista:
        toista = False
        for i in range(0, len(lista)):
            if lista[i] % 2 != 0:
                del lista[i]
                toista = True 
                break
            
    print(lista)

syotto = luvunotto()

while syotto != "":
    luvut.append(syotto)
    syotto = luvunotto()

print(luvut)
karsi_parittomat(luvut)