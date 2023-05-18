a = input().split(" ")

n1 = int(a[0])
n2 = int(a[1])
goda = 0
while n1 < n2 or n1 == n2:
    n1 = n1 * 3
    n2 = n2 * 2
    goda += 1
print(goda)