# 3) ===========================
y = int(input())
u = 0
for i in range(y):
    a = input()
    n = a.split(" ")
    n1 = int(n[0])
    n2 = int(n[1])
    n3 = int(n[2])
    if n1 + n2 + n3 > 1:
        u += 1
print(u)
