a = input("цвет1:").capitalize()
b = input("цвет2:").capitalize()
if a == "Красный" and b == "Синий" or a == "Синий" and b == "Красный":
    print("Фиолетовый")
elif a == "Красный" and b == "Жёлтый" or a == "Жёлтый" and b == "Красный":
    print("Оранжевый")
elif a == "Синий" and b == "Жёлтый" or a == "Жёлтый" and b == "Синий":
    print("Зеленый")
elif a == b:
    print(a)
else:
    print("Ощибка!!!")

