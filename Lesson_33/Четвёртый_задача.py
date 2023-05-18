input()
a =input()
perehod = 0
ubiraem = 0

while perehod != len(a) - 1:
    if a[perehod] == a[perehod+1]:
        a = a[:perehod] +a[perehod+1:]
        ubiraem += 1
    else:
        perehod +=1
print(ubiraem)