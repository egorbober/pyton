import time
import random
znaki = ["+","-"]
schot = 0
uroven = print("Начинаем через 3")
time.sleep(1)
print("               2")
time.sleep(1)
print("               1")
time.sleep(1)
print("    начили!")
while True:
    otvet1 = random.randint(1, 100)
    otvet2 = random.randint(1, 100)
    znak = random.choice(znaki)
    primer = f"{otvet1}{znak}{otvet2}"
    print(primer)
    variant = int(input("Ответ:"))
    if znak == znaki[1]:
        otvet = otvet1 - otvet2
        if otvet == variant:
            print("Всё правильно!")
            schot += 1
        else:
            print(f"Неправильно! Ты проиграл! Правильный ответ:{otvet}.")
            print(f"Твой счёт:{schot}")
            break
    if znak == znaki[0]:
        otvet = otvet1 + otvet2
        if otvet == variant:
            print("Всё правильно!")
            schot += 1
        else:
            print(f"Неправильно! Ты проиграл! Правильный ответ:{otvet}.")
            print(f"Твой счёт:{schot}")
            break