# def plus_one (a,b):
#     return a + b + 1
#
# print(plus_one(4,5))
#
# #лямда функция
# plus_one2 = lambda a,b:a+ b + 1
# print (plus_one2(6,7))
#
# #if-else в lambda
# result = lambda answer: True if answer == "Д" else False
#
# # list comprehension
# spisok = []
# for i in range (1,6):
#     spisok.append(i)
# print (spisok)
#
# # 1. list comprehension
# spisok2 = [i for i in range(1,6)]
# print (spisok2)


#кости
#Второй задача
# from random import randint
# banana = lambda zxc: True if zxc == "да" else False
# while True:
#     a = int(input("Сколько раз бросаем kosti?:"))
#     kosti = [randint(1,6) for n in range (a)]
#     print(kosti)
#     kivi = input("играем дальше? да/нет:").upper()
#
#     if banana(kivi):
#         break

#Третий задача
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#          ]
# cot = [choice(choice(chars))for n in range(6)]
# cotik = "".join(cot)
# dictionaryy = {"https://www.google.com":"Алd5I9"}
# ssilka_na_kavkaz = "https://www.google.com"
# if ssilka_na_kavkaz in dictionaryy:
#     print("эта ссылка уже в базе, вот её код:")
#     print(dictionaryy[ssilka_na_kavkaz])
# else:
#     print("ссылка добавлена, лови её!!!")
#     dictionaryy[ssilka_na_kavkaz] = cotik

#Четвёртый задача
y = lambda a, b:a / b
print(y(6,3))
y1 = lambda a, b:a % b
print(y1(6,3))
y2 = lambda a, b:a // b
print(y2(6,3))
y3 = lambda a, b:a ** b
print(y3(6,3))
y4 = lambda a:-a if a < 0 else a
print(y4(6))