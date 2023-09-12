a = int(input("Число:"))
proisvedenie = 1
for num in range(1, a+1):
    proisvedenie = num * proisvedenie
    print(proisvedenie)