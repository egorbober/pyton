# ООП
# 1) Инкапсуляция: приветное и публичное
# 2) Наследование: родительские и дочерние классы, super
# 3) Полиморфизм: магические методы


# ------------ инкапсуляция ------------
# class Urok:
#     shkola = 222222 # Статический публичный атрибут
#     __secret = 123 # Динамический публичный  атрибут
#
#     def __init__ (self,dlina):
#         self.dlitelnost = dlina # Динамический публичный атрибут
#         self.__secret2 = 321 # Динамический приватный атрибут
#     def get5(self): # Публичный метод
#         return 5 # Динамический публический атридут
# matematika = Urok(50) # Инициализация -> создание объекта на основе класса
# print(matematika.get5()) # 5
# print(matematika.dlitelnost) # 40
#
# fizika = Urok(10)
# print(fizika.shkola)
# Urok.shkola = "Жизнь"
# print(Urok.shkola)

# ------------ полиморфизм ------------

# class Cls1:
#     def __call__(self, *args, **kwargs): # срабатывает при вызове объекта класса
#         print(kwargs)
#         print(args)
#         return "Гоша"
#     def __add__(self, other): # При с ложении self - relf куда; other - что
#         return f"{self} и {other}"
#
#
#
# class Cls2:
#     def __str__(self):
#         return "Чё пуп ели?"
#
#
#
# c1 = Cls1() # __init__
# c2 = Cls2() # __init__
# print(c1(1, [""], key1 = {})) # __call__
# print(c2)
# print(c1 + c2)
# print(c1.__add__(c2))

# ----------- наследование -------------
class Cl1:
    def __init__(self):
        self.parapapam = "уУуУуУ"
    def say_hi(self):
        print("Привки")
    def __int__(self):
        super().__init__()
        self.param = "ЫыЫыЫы"

class Cl2(Cl1): #Наследник Сl1
    pass

obj1 = Cl1()
print(obj1.parapapam)
obj2 = Cl2()
print(obj2.parapapam)
print(hasattr(obj2, "param"))
