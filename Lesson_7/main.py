#Ошобки

#ZeroDivisionError
#a = 5/0

#TypeError
#a = "a" + 15

#IndexError
# a = [0 ,-15, "Антон"]
# a.pop(-10)

# SyntaxError
# a = "прпшцпен

#NameError
#a = "фывапролджрпав"
#print(a1)

#AssertionError
# assert
# def summa (numbers):
#     return sum (numbers)
#
# #print(summa([3,4]))
#
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4

#Попытаться, работа с ошибками.
# try:
#     a = int(input("Введи число:"))
# except ZeroDivisionError:
#     print("На нУль делить нельзя!")
# except Exception:#любая ошибка
#     print("ты ОшИбИлСя")
# except ValueError:
#     print("XХочу цыфры!")
# else: #всё норм 🙃
#     print("Я поделиф! ")
# finally:
#     print("Я всё")


try:
     a = input("Имя:")
     if a == "Антон":
         raise Exception ("Антона в обиду не дам!")
except Exception as q:
     print("Это слово запрещено!",q)