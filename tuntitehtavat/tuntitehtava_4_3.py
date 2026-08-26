nimi = str(input("Anna nimi: "))

print(f"{nimi} on oppitunnilla ja ruokatunti lähestyy. {nimi} harkitsee käymistä kaupassa ruokalan sijaan. \nMeneekö {nimi} syömään ruokalassa vai ei? (y/n)")
valinta = str(input())

if valinta == "y":
    print(f"{nimi} teki erinomaisen valinnan ja nautti ruokalan antimista.")
elif valinta == "n":
    print(f"{nimi} valitsi kehnosti ja jäi ilman lämpimää ruokaa.")
else:
    print("Virheellinen komento!")