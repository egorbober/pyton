# x = ["Никита", "Екатерина", "Арсалан", "Наталья", "Григорий", "Евгений", "Анастасия", "Андрей", "Евгения", "Герман", "Тимур", "Ярослава", "Есения", "Даниил", "Данил"]
# povtori = 0
# imia = input("Введи имя:").capitalize()
# for i in x:
#     if imia == i:
#         povtori += 1
# print(povtori)

from random import randint
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
x = 0
a = int(input())
stroka = []
while x != a:
    random = randint(0, 25)
    stroka.append(alphabet[random])
    x += 1
print(stroka)

