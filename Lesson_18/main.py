# Фуктия
# def functia(x):
#     return x + 1
#
# print (functia(5))
#
# a = lambda x2: x2 + 1
# print (a(3))
#
# fasol = 20
#
# def  minus_fasol (x):
#     global fasol
#
# while fasol > 0:
#     while True:
#         x = int(input("скоко фасоли убирёшь?:"))
#         if x < 4 and x > 0:
#             break



# стрелок
#from random import randint
# import time
# print("Время пострельть...")
# time.sleep(randint(2.0,5.0))
# print("Стреляй!!!")

from random import randint
a = int(input("Скоко раз кидаем кости?:"))
d = {}
for i in range (a,a*6+1):
    d[i] = 0
for b in range(1_000_000):
    total = 0
    for _ in range(a):
        brosok = randint(1,6)
        total += brosok
    d[total] += 1
print(d)

# Функции
# def functia(x):  # объявление функции
#     return x + 1
#
# print(functia(5))  # вызов функции с аргументом
#
# f = lambda x2: x2 + 1  # объявление лямбда функции
# print(f(5))  # вызов лямбда функции

# Фа соль

beans = 20


def vichitanie(x):
    global beans
    beans -= x


while beans > 0:
    while True:  # Валидация (НЕ ТРОГАТЬ)
        pervi = int(input("Первый игрок сколько фа соли взять? : "))
        if pervi < 4 and pervi > 0:
            break
    vichitanie(pervi)
    print(beans)
    if beans <= 0:
        print("========== ПОБЕДИЛ ВТОРОЙ ИГРОК ==========")
        break
    while True:  # Валидация (НЕ ТРОГАТЬ)
        vtoroi = int(input("Второй игрок сколько фа соли взять? : "))
        if vtoroi < 4 and vtoroi > 0:
            break

    vichitanie(vtoroi)
    print(beans)
    if beans <= 0:
        print("========== ПОБЕДИЛ ПЕРВЫЙ ИГРОК ==========")
        break

from random import randint
import time

print(
    "Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")

input("нажми Enter чтобы начать:")
print("Время пострелять")
time.sleep(randint(2, 5))
start = time.time()
input("СТРЕЛЯЙ!!!")
end = time.time()
delta = end - start
print(delta)
if delta > 0.3:
    print("Ты медленная черепаха!! Стреляй быстрее!! 🐢 ")
elif delta < 0.01:
    print("Ты слишком быстрый!")
else:
    print("Ты победил😎")

from random import randint

a = int(input("Сколько костей хотите кинуть?:"))
d = {}

for i in range(a, 6 * a + 1):
    d[i] = 0
for b in range(1_000_000):
    total = 0
    for _ in range(a):
        brosok = randint(1, 6)

        total += brosok
    d[total] += 1
print(d)