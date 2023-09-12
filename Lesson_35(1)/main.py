x = [1,2,3]
y = x
y.append(5)
print(x)
print(y)

x = [1,2,3]
y = x[:]
y.append(5)
print(x)
print(y)