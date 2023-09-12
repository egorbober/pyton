a = int(input("Число1:"))
b = int(input("Число2:"))

s = 0

if a > b:
    for num in range(b, a+1):
        print(num ** 2)
else:
    for num in range(a, b+1):
        print(num ** 2)

