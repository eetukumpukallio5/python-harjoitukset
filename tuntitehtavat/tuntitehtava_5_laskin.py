toiminto = input("Anna toiminto (+,-,*,exit) ").lower()
while toiminto != "exit" and (toiminto == "+" or toiminto == "-" or toiminto == "*"):
    a = float(input("Anna ensimmäinen numero: "))
    b = float(input("Anna toinen numero: "))
    if toiminto == "+":
        print(a + b)
    elif toiminto == "-":
        print(a - b)
    elif toiminto == "*":
        print(a * b)
    toiminto = input("Anna toiminto (+,-,*,exit) ").lower()
#toimimampi tapa vielä olisi ollut luoda loopit toiminnon syötteeseen, ja pyörittää looppia kunnes saamme hyväksyttävän merkin (+,-,*,exit). nykyinen tapa riitää perustoimintoihin tehtävän parametreissa kuitenkin