a = input().split(" ")
b = int(a[0])
c = int(a[1])
d = int(a[2])
z = 0
for i in range(1,d+1):  # итого цена
    z += i * b
if z > c :
    print(z-c)
else:
    print(0)