# class Nazvanie:
#     def __init__(self):
#         self.money = 1000
#         self.__zarplata = 5
#     def Bar(self):
#         if self.__zarplata > 50:
#             return True
#         else:
#             self.__sad()
#             return False
        #     print("Гуляем!!!😁😁😁")
        # else:
        #     print("Сори чел.Я бомж!☹☹☹")
#     def __sad(self):
#         print("Грустим...")
# Sanya = Nazvanie()
# print(Sanya.money)
# Sanya.money += 100
# print(Sanya.Bar())

# Sanya.__zarplata = 100
# Sanya.__zarplata += 100
# print(Sanya.__zarplata)


# Sanya._Nazvanie__zarplata = 1_000_000_000_000_000_000_000_000_000_000_000
# print(Sanya.Bar())


# (class Mashina:
#     def __init__(self):
#         self.zapusk = "Автомобиль заведен"
#         self.konech = "Автомобиль заглушен"
#         self.god_vipuska = "1000 лет до н.э."
#         self.tip = "Бэха"
#         self.color = "Серо-буро-малиновый в крапенку"
#         print(f"Для zapusk нажмите _1_,"
#               f" для konech нажмите _2_ для,"
#               f" god_vipuska нажмите _3_,"
#               f" для tip нажми _4_,"
#               f" для color нажми _5_.")
#
#         peremena = input("Чё хошь???(1,2,3,4,5):")
#
#         if peremena == "1":
#             print(self.zapusk)
#         if peremena == "2":
#             print(self.konech)
#         if peremena == "3":
#             print(self.god_vipuska)
#)   -------    плохое решение☹☹☹☹☹☹☹☹☹☹




 # Второй задача
# import string
# class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def pritn(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
#
# all = Alphabet("eng")
# all.pritn()
# all.letters_num()



# Третий задача
import datetime
class Clock:
    def __init__(self):
        self.__time = datetime.datetime.now().strftime("%H:%M:%S")
        self.__h,self.__m,self.__s = self.__time.split(":")
        self.__h,self.__m,self.__s = int(self.__h),int(self.__m),int(self.__s)
        # self.m = self.__time.split(":")[1]
        # self.s = self.__time.split(":")[2]
    def hours(self):
        self.__h += 1
    def minut(self):
        self.__m += 1
    def seconds(self):
        self.__s += 1
    def test_s(self):
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
    def test_m(self):
        if self.__m > 59:
            self.__m = 0
            self.__h += 1
    def test_h(self):
        if self.__h > 23:
            self.__h = 0


    def vivod(self):
        print(f"{str(self.__h).rjust(2,'0')}:{str(self.__m).rjust(2,'0')}:{str(self.__s).rjust(2,'0')}")


time_0 = Clock()
time_0.minut()

time_0.vivod()


