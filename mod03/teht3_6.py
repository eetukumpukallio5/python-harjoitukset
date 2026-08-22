#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#hyödynnetään randint() funktiota ohjeiden mukaisesti, ja tulostetaan ohjeiden mukaisesti koodit.
import random

print(f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}")
print(f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}")