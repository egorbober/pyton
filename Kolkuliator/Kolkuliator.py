otvet = ""
a = 0
while a == 0:
    prim = input("Пример:")
    resh = prim.split(" ")
    znak = resh[1]
    if znak == "+":
        otvet = int(resh[0])+int(resh[2])

    elif znak == "-":
        otvet = int(resh[0]) - int(resh[2])

    elif znak == "*":
        otvet = int(resh[0]) * int(resh[2])

    elif znak == ":" or znak == "/":
        otvet = int(resh[0]) / int(resh[2])
    print(otvet)