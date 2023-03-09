# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return ("Я Кристина")

# Eugenii = Person("Юджин",100)
# anna = Person(vozrast=1000000, imya="Кристина")
#
# print(anna.name)
# print(anna.age)
# print(anna)

# class HelloWorld:
#     def __getitem__(self, key):
#         print("Hello World", key)
# hi = HelloWorld()
# hi[42]
# hi["Movavi"]


# Первый задача
# from random import randint
# class Person:
#     def __init__(self,imia,vosvrast,familia):
#         self.vosrast = vosvrast
#         self.imia = imia
#         self.familia = familia
#         self.ochenci = [randint(2,5) for n in range (randint(5,10))]
#         self.summa = sum(self.ochenci) / len(self.ochenci)
#
#     def __str__(self):
#         return f"{self.imia} {self.vosrast} {self.familia} "
#     def greed (self):
#         return f"Привки!! Я {self.imia} {self.familia}. Мне {self.vosrast} и я милашка, няяяя 🤗🤗🤗"
#
# Masha = Person(vosvrast=6,imia="Машуля",familia="Милашкова")

# print(Masha.imia)
# print(Masha.familia)
# print(Masha.vosrast)
# print(Masha)
# print(Masha.greed())
# print(Masha.ochenci)
# print(Masha.summa)

# listochec = []
# for i in  range (randint(5,11)):
#     x = randint(2,5)
#     listochec.append(x)
#
# Milanya = Person("Милаша",13,"Дорн")
# Bobr = Person("Егор",10000,"Бобер")
# Anton = Person("Антошка",22.22,"Смирнов")
# ychenici = [Masha,Milanya,Anton,Bobr]
# dnevnic = {}
# for item in ychenici:
#     print(item)
#     dnevnic[item.imia] = item.summa
# print(dnevnic)
#
#
# sorted_dnevnik = dict(reversed(sorted(dnevnic.items(),key= lambda item:item[1])))
#
# print(sorted_dnevnik)
# for item in sorted_dnevnik:
#     print(item)

class Rectangle:
    def __init__(self,d1,d2):
        self.dot1 = d1
        self.dot2 = d2
    def ploshadi(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return a * b
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

dot1 = Point(1,100)
dot2 = Point(2,254)
priamoug = Rectangle(dot1,dot2)
print (priamoug.ploshadi())
