#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitto(x):
    return random.randint(1, x)

while True:
    x = input("Anna kokonaisluku. ")
    try:
        x = int(x)
    except ValueError:
        print("Syöte ei ole kokonaisluku!")
        continue
    break

tulos = 0 

while tulos != x:
    tulos = heitto(x)
    print(tulos)