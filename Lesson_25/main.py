# class Chelovek:
#     __city = "Новосиборск"
#     def __int__(self,haight):
#         self.hi = haight
#         self.vosrast = haight
#         obj = Chelovek
#         print(obj.hi)
#         obj2 = Chelovek(150)
#         print(obj2.hi)
from random import randint

class Human:
    defult_name = "Антон"
    defult_age = 56
    def __init__(self,name = defult_name,age = defult_age):
        self.name = name
        self.age = age
        self.__money = 50
        self.__house = None
    def info(self):
        return self.name,self.age,self.__money,self.__house
    def earn_money(self,__money):
        return __money + 100


    def defult_info(self):
        return Human.defult_name,Human.defult_age

    def __mace_dele(self,dom):
        if self.__money > dom.final_prise():
            self.__money -= dom.final_prise()
            print("Денег достаточно !")
            return True

    def buy_house(self,dom):
        if self.__mace_dele(dom):
            dom.owner = self.name
            self.__house = dom
            return "Хата теперь твоя"
        else:
            return f"Иди копи денег {dom.final_prise() - self.__money}"

class Dom:
    def __init__(self,ar="Новосибирск",pr= 50000):
        self.__are = ar
        self.__prise = pr
        self.skidka = randint (5,25)/100
    def final_prise(self):
        return self.__prise - self.__prise * self.skidka
anton = Human()
dom1 = Dom()
print(anton.buy_house(dom1))

