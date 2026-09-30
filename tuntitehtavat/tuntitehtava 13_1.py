with open("ostos.txt", "r") as tiedosto:
    tuotteet = tiedosto.readlines()
    print("Tuotteita listalla:", len(tuotteet))