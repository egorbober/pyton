# def bibim (a:int = "Ы") -> int: #Стрелочка:)
#     return a
#
# result = bibim()


# def aoa(*args, **kwargs):
#     print(kwargs)
#     print(args)
#
# print(aoa(1,2,3, a=32, soroka="е"))

# def foo(**kwargs):
#     for i in kwargs:
#         print(i.ljust(30)+str(kwargs[i]).rjust(10))
#     print("-"*40)
#     print(str(sum(kwargs.values())))
#
# print(foo(apple=105,banana=230,tutifruti=132))

# def camel2snake (stroka:str) -> str:
#     a = ""
#     for i in stroka:
#         if i.isupper():
#             a += "_" + i.lower()
#         else:
#             a += i
#     return a
#
#
# print(camel2snake("word"))
# print(camel2snake("wordSecond"))


class Human:
    def say(self, frase): #метод публичный
        self.__vdoh()
        return "О,"+frase
    def __vdoh(self):# Приватный
        print("*вдохнул*")

    def __init__ (self):
        self.age = 5


petr = Human()
print(petr.say("Привки"))
print(petr._Human__vdoh())
print()
igor = Human()
print(petr.age)
