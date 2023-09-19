#Задача 1

# a = [1, 2, 3, 4, 5]
# print(sum(a))
# print(min(a))
# print(max(a))
# x = sorted(a)
# print(x[0],x[-1])

#Задача 2

# f = "Тетради Ус Москва обнимать?!"
# print(f[3:16:3] + f [-5:-2])

#Задача 3

# l = [1, 2, 2, 3, 1, 4]
# v = []
# for i in l:
#     if i not in v:
#         v.append(i)
#     else:
#         pass
# print(v)

#Задача 4

# a = [1, 3/4, 2, "Аниме"]
# d = {"int":0,
#      "float":0,
#      "str":0
#      }
#
# for i in a:
#     if type(i) == int:
#         d['int'] += 1
#     elif type(i) == float:
#         d["float"] += 1
#     else:
#         d["str"] += 1
#print(d)

#Задача 5

# a = [1,2,3,4,5,6]
# b = [7,8,9,10,1,2,3,4,5]
# print(sorted(a + b))

#Задача 6

# a = "Привет мир"
# stop = "1234567890!@#$%^&*()№:? "
# d = {}
# for i in a:
#     if i not in stop:
#         d[i] = a.count(i)
# print(d)

# Задача 7

# import string
# bol = string.ascii_uppercase
# mal = string.ascii_lowercase
# d = {}
# for i in range(len(bol)):
#     d[mal[i]] = bol[i]
# print(d)

# Задача 8

c = 0
oper = {
    "add":lambda x: c+x,
    "mul":lambda x: c*x,
    "minus":lambda x: c-x,
    "div":lambda x: c//x,
}

while True:
    a = input().split()
    if len(a) == 1:
        a = a[0]
        if a == "exit":
            break
        if a == "result":
            print(c)
        elif a == "zero":
            c = 0
    else:
        c = oper[a[0]](int(a[1]))
