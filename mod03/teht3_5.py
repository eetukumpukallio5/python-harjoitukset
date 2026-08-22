#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. 
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
#kysytään käyttäjältä yksi yksikkö kerrallaan, ja muutetaan ne suoraan grammoiksi. kerättyämme yksiköt lisätään ne yhteen, jonka jälkeen esitetään grammat sekä kilogrammoina että grammmoina

print("Anna leiviskät.")
leiviska = float(input()) * 20 * 32 * 13.3

print("\nAnna naulat.")
naula = float(input()) * 32 * 13.3

print("\nAnna luodit.")
luoti = float(input()) * 13.3

gramma = leiviska + naula + luoti
kg = int(gramma // 1000)
g = gramma % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {g:.2f} grammaa.")