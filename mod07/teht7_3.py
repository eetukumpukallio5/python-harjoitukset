#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. 
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
#Muunnos on tehtävä aliohjelmaa hyödyntäen. 
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def luvunotto():
    while True:
        x = input("Anna gallonamäärä. ")
        try:
            x = float(x)
        except ValueError:
            print("Syöte ei ole numero!")
            continue
        break
    return x

def litra_muunnos(gallonat):
    x = gallonat * 3.785
    return x

gallonat = luvunotto()

while gallonat >= 0:
    print(f"Syöte on {litra_muunnos(gallonat)} litraa.")
    gallonat = luvunotto()