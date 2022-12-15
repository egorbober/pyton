# МНОЖЕСТВА
# s = set() # пустое множество
# s1 = {1,2,3,3} # дубликаты НЕ пишутся
# print(s1)
#
# s2 = {"А","Б","В"}# НЕУПОРЯДОЧЕНЫЙ тип данных
# print(s2)

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7,}
# print(s1 | s2) # Объединение
#
# print(s1.intersection(s2))#Пересечение
#
# print(s1 & s2) #Тоже пересечение
# print(s1 - s2) #Отнять множество
#
# print(s1.symmetric_difference(s2)) #Симетрическая разность
# print(s1 ^ s2)

# Словари
# a1 = {"Пи": 3.14 ,
#       "Препод":"Антон",
#       "Список дел": ["Выжить","Ловить шизу"],
#       "Словарь": {"Вл1":1}}
# print(a1["Препод"])
# print(a1["Список дел"][1])
# print(a1["Словарь"]["Вл1"])

# from random import randint
#
# lst = []
#
# for _ in range(5):
#     randint(1,5)
#     lst.append(randint(1,5))
# print(lst)
#
# unikue = set(lst)
# print(unikue)
#
# print(f"{len(unikue)} штук:{unikue}")

# from random import randint
# lst1 = []
# lst2 = []
# size = randint(100,1000)
# r_start = 0
# r_end = 10_000
#
# for _ in range(size):
#     lst1.append(randint(r_start,r_end))
#     lst2.append(randint(r_start,r_end))
# set1 = set(lst1)
# set2 = set(lst2)
#
# inter = set1.intersection(set2)
# print(f"Общих чисил:{len(inter)}")
# print(f"[Кол-во генераций]:{size}")
# print(f"[Мини. значение]:{min(inter)}")
# print(f"[Макс. значение]:{max(inter)}")

#Калхоз
# inter1 = list(inter)
# inter1.sort()
# print(inter1)

# Норм решение
# print(sorted(inter))

# set1 = set()
#
# insept = ""
# while insept != "end":
#     insept = input("Ввод:")
#     if insept.lstrip("-").isdigit():
#         if insept not in set1:
#             print("НЭТ")
#             set1.add(insept)
#         else:
#             print("ДА")
#     elif insept == "end":
#         break
#     else:
#         print("Хочу чиселко")