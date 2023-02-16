# f = open("усё норм!.txt","w")
# f.write("Hello World\n")
# f.write("Movavi")
#
# f.close()

# f = open("Усё норм!.txt","r")
# content = f.readlines()
# print(content)
# for line in content:
#     print(line.rstrip())
#
# f.close()


# txt = input("> ")
# f = open("усё норм2!.txt", "w", encoding="utf-8")
# while txt != "":
#     f.write(txt + "\n")
#     txt = input("> ")
# f.close()
# print("Всё!")
#
#
# второй задача


f = open("усё норм2!.txt","r",encoding= "utf-8")
content = f.readlines()
f.close()
f = open("text.txt","w",encoding= "utf-8")
count = 1
for lion in content:
    result = f"{count}) {lion}"
    f.write(result)
    count += 1
print(content)


#4 зад
n = int(input("N = "))
f = open("усё норм2!.txt","r",encoding= "utf-8")
elements = f.readlines()
f.close()
a = elements[:n]
for element in a:
    print(element.rstrip())