pituus = float(input("Kuinka pitkä olet? "))

if 195 <= pituus:
    ika = int(input("Kuinka vanha olet? "))
    if 8 <= ika:
        print("Saat mennä kaikkiin laitteisiin paitsi Kirnuun.")
    else:
        print("Saat mennä kaikkiin laitteisiin paitsi Tulirekeen ja Kirnuun.")

elif 140 <= pituus < 195:
    ika = int(input("Kuinka vanha olet? "))
    if 8 <= ika:
        print("Saat mennä kaikkiin laitteisiin.")
    else:
        print("Saat mennä kaikkiin laitteisiin paitsi Tulirekeen.")

elif 100 <= pituus < 140:
    print("Saat mennä lasten laitteisiin.")

else:
    print("Ei laitteita sinulle.")