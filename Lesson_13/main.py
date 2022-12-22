# Первый задача.
# phise = "РоСсИя, РоСсИя, РоСсИя И бОгДаН! ".lower() #Опустили буквы.
# print(phise)
# sumbol = "!@#$%^&*()123456789'\",.?" # \" экраниравание.
# phise_clen = "" # Ща будем мыть phise
# for i in phise: # моем phise
#     if i not in sumbol:
#         phise_clen += i
#
# phise_list = phise_clen.strip(" ")
# print(phise_list)
#
# d = {}
# for dom in d:
#     if dom in d:
#         d[dom] = 1
#     else:
#         d[dom] += 1
#         print (d)

# Второй задача.
# d = {"Молоко":100,
#      "Дошик":21,
#      "Чипсы":0.1,
#      "Богдан":999.9}
# slog = 0
# for i in d.values():
#     slog += 1
#     print(i)

DIE_SIDES = 6
DIE_COUNT = 2
d = {}

for first in range (1,DIE_SIDES + 1):
    for second in range (1,DIE_COUNT + 1):
        if first + second not in d:
            d[first + second] = [(first, second)]
        else:
            d[first + second].append((first, second))

print(d)

for tagici in d:
    print(f"{tagici}: {d[tagici]}")
