import time
import random
true = 1
znaki = f"+ -".split(" ")
uroven = print("Начинаем через 3")
time.sleep(1)
print("               2")
time.sleep(1)
print("               1")
time.sleep(1)
print("    начили!")
while true == 1:
    true = 1
    varianti = f"{random.randint(1, 100)}{random.choice(znaki)}{random.randint(1, 100)}"
    print(varianti)
    input("Ответ:")
    # Дальше я не знаю
