            #Классная работа


# def func():
#     pass
#
#
# print("temperature")

# try:
#     number = int(input("Число"))
# except ValueError:
#     print("Это не число!!! Учи матешу!!!")

# name = input("Введи имя друга(собаки):").title()
# try:
#     if name == "Антон":
#         raise ValueError("Ты чё, пёс")
# except ValueError as pelmeni:
#     print(pelmeni,"Запрещаю")

#Первый задача

# def masha(content):
#     s = 0
#     k = 0
#     for chiselko in content:
#         try:
#             s += int(chiselko)
#         except ValueError:
#             print("Мне нужно чиселко!!!Учи матешу!!!")
#         else:
#            k += 1
#         if k ==0:
#             print("Файл без чисел")
#             return "[Там пусто]"
#     return s / k
#
#
#
#
# try:
#     fail = open("Чиселко.txt","r",encoding= "utf-8")
# except FileNotFoundError:
#     print ("нет файла! пока!")
#     quit()
#
# content = fail.read().split()
# fail.close()
# print(content)
#
# print(masha(content))


# try:
#      fail = open("Чиселко.txt","r",encoding= "utf-8")
# except FileNotFoundError:
#     print("нет файла! пока!")
#     quit()
# content = fail.readlines()
# fail.close()
# print(content)
#
# for i,student in enumerate(content):
#     content[i] = student.split()
#
# maxi = -1
# for student in content:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print("Ошибка  в балах", student)
#     except IndexError:
#         print("нет балов у ",student)
#     except FileNotFoundError:
#         print("он пустой")
#
#
# print(maxi)


try:
     fail = open("Чиселко.txt","r",encoding= "utf-8")
except FileNotFoundError:
    print("нет файла! пока!")
    quit()

content = fail.read()
word = input("Какое слово ищем?:")
print(content.count(word))