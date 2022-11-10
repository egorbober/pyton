# ЦИКЛЫ!
# while
# a = 10
# while a != 0:
#     print (a)
#     a -= 1
#
# while True: # Срабатывает всегда!
#     break # Выйти из цикла!
#
# for

# s = ["А","Б","В","Г","Д"]
# for d in s:
#     print(d)
#
# for x in range(0,3):
#     print(x)

# УМЕНЬШАТОР СЛОВА!
# a = input("Твоё постоднее слово:")
# while a != 0:
#     print(a, end=" ")
#     a = a[:-1]
#     break

# a = int(input(":"))
# while a != 0:
#     a -= 1
#     if a % 2 == 0:
#         print(a)

a = input("число: ")
if not a.isdigit() or int(a) < 1:
    print("Одна ошибка и ты ошибся!")
    quit()
else:
    a = int(a)
d = 0
while a != 1:
    d += 1
    if a % 2 == 0:
        print(f"{d})", end=" ")
        print(a,"/ 2 =", end=" ")
        a = a // 2
    else:
        print(f"{d})", end=" ")
        print(a, "* 3 + 1", end=" ")
        a = a * 3 + 1
    print(a)
print("шагов:",d)