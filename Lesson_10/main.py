# a = [0,1,2,3,4,5]
#
# for i in a:
#     print(i)
#
# for x in range (0,11): #От нуля до десяти
#     print(x)

#СПОСОБ 1 по
# a = int(input("Первое число:"))
# x = int(input("Второе число:"))
#
# while a != x + 1:
#     print(a )
#     a = a + 1

# a = int(input("Первое число:"))
# x = int(input("Второе число:"))
#
# for e in range(a,x + 1):
#     print(a)
#     a = a + 1

# while True:
#     try:
#         lvl = int(input("Число ярусав:"))
#     except ValueError:
#         print("хочу число")
#         continue
#     else:
#         break
#
#
# while True:
#     sim = input("символ:").strip()
#
#     if len(sim) == 1:
#         break
#
#
# for i in range (1,lvl + 1):
#     # левая половина
#     print(" " * (lvl - i ),end="")
#     print(sim * i, end= "||")
#
#
#     # правая половина
#     print(sim * i)
