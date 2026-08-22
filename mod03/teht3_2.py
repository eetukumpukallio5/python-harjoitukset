#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#kaava ympyrän pinta-alaan on A=πr^2, jossa r on säde. otetaan käyttäjältä säde ja suoritetaan yhtälö liukuluvuilla

from math import pi #voisimme tuoda koko math kirjaston, mutta oppiakseni tuon ainoan tarvitun ominaisuuden, piin
säde = float(input("Anna ympyrän säde: ")) #kysytään säde ja muutetaan stringistä floattiin
print(f"Pinta-ala on ympyrällesi {pi * säde ** 2}") #pi hakee laskuun piin vakion. python selkeästi noudattaa oikeaa laskujärjestystä, laskut onnistuvat ilman ongelmia