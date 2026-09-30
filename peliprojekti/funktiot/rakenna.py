def rakenna(lista, kerrokset):
    if "tiili" in lista:
        print("Rakentakaamme yhden kerroksen lisää.")
        for i in range(kerrokset):
            print(r" -- ")
            print(r"|  |")
            print(r" -- ")
    else:
        print("Tarvitset tiilin rakentaaksesi.")