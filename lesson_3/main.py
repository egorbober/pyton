# многострочный string
#  a = "Egor\nEgor\nEgor"
#  a1 = """строка1
#  строка2
#  строка3"""
#  print (a1)

# братва
# a = "Egor"
# b = "Федя"
# c = "Серёжа"
# bratva = [a,b,c]
# print(bratva)
# print(bratva[0])

# алфавит(alphabet)
# alphabet = "АБВГДЕЁЖЗИКЛМН"
# print(alphabet[0])
# print(alphabet[-1])
# print(alphabet[0] + alphabet[1] + alphabet[2])
# print(alphabet[-3:]) #вывести 3 последних
# print(alphabet[:3])#вывести 3 первых
# print(alphabet[::2])#вывести через одного
# print(alphabet[::-1])#вывести в обратном порядке
# print(alphabet[::-2])#вывести в обратном порядке через одного

#используем Lenу
#a = input ("Число:")
#print (a[0])
#print (a[-1])
#temp = a[-1]
#print (a.index(temp) + 1)#индекс последнего символа + 1
#print (len(a))

#решение, но не крутое!
# path = "C:/Python3/python.exe"
# print ("Имя файла:",path[-10:])
# print ("Расширение:",path [-3:])
# print ("Имя котолога:",path [3:10])
# print ("Полный путь к катологу:",path[:10])

#Решение ,но крутое!
# path = "C:/Python3/python.exe"
# a = path.split("/")
# print (a)
# print ("Имя файла:",a[-1])
# print ("Расширение:",a[-1][-4:])
# print ("Имя котолога:",a[1])
# print ("Полный путь к катологу:",a[0] + "/" + a[1])
# a1 = input("Глава1:")
# d1 = input("Страница:")
# a2 = input("Глава2:")
# d2 = input("Страница:")
# print(a2.ljust(15), d2.rjust(15))
# print(a1.ljust(15), d1.rjust(15))