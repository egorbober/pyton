# a = 7
# if a == 5:
#     print ("Я не сработаю 😥")
# elif a > 5:
#     print("a > 5 🤓")
# else:
#     print("Я, вероятно сработаю 😁")

#Угадай слово
# a = input("Введи слово(1/2):")
# b = input("Введи слово(2/2):")
# a = a.lower()
# b = b.lower()
# if a.isalpha() and b.isalpha():
#     sorted_a = sorted(a)
#     sorted_b = sorted(b)
#     print(sorted_a, sorted_b)
#     if sorted_a == sorted_b:
#         print("Ура, у нас анаграмма!")
#     elif sorted_a == sorted_b:
#         print("ТЫ ЛОХОНУЛСЯ!")
# else:
#     print ("ХоЧу ТоЛьКо БуКвЫ")

a1 = input("Сколько будет 2 + 2?\n"
           "а)4,б)5\n"
           "-->")
if a1 == "а":
    print ("Тебе повезло 🙃")
    c = +1
else:
    print("Ты проиграл - ДЕ**ИЛ 😕")
    quit()
a2 = input("Арбуз это...\n"
           "а) корнеплод\n"
           " б)овощ\n"
           " в)ягода\n"
           " г)фрукт\n"
           "-->")
if a2 =="в":
    print ("Тебе повезло 🙃")
    c = +1
else:
    print("Ты проиграл - ДЕ**ИЛ 😕")
    quit()
a3 = input("Обезьяна это...\n"
           "а) ты\n"
           " б)насекомое\n"
           " в)овощ\n"
           " г)животное\n"
           "-->")
if a3 == "г":
    print("Тебе повезло 🙃")
    c =+1
else:
    print("Ты проиграл - ДЕ**ИЛ 😕")
    quit()
    print ("Ты ПоБеДиЛ")


