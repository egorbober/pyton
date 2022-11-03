 #Способ 1
# import random
# a = random.randint(0,100)

 #Способ 2
# import random as a
#  s = a.randint(0,100)

 #Способ 3
# from random import randint
# a = randint(0,100)

 #Способ 4 ПЛОХОЙ СПОСОБ!
# from random import *
# a = randint(0,100)

#Черепашка
#  import turtle
#  screen = turtle.Screen()
# t = turtle.Turtle()
#t.color("gold","dark green")
# t.begin_fill()
# t.pensize(10)
# t.speed(0)
# t.shape("turtle")
# d = 200
# c = 100
# t.forward(d)
# t.right(90)
# t.forward(c)
# t.right(90)
# t.forward(d)
# t.right(90)
# t.forward(c)
# t.rt(90)
# t.end_fill()
# t.penup()
# t.goto(x=130,y=-40)
# t.pendown()
# t.fd(45)
# t.begin_fill()
# t.color("red","blue")
# t.circle(50)
# t.end_fill()
# t.pencolor("blue")
# t.write("Антон",font = ("Arial Blak",50,"italic"), align= "center")
# screen.exitonclick()

# import turtle
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(10)
# colors = ["red","orange","yellow","green","light blue","blue","purple"]
# r = 360 / 7
# for v in range(0,7):
#     t.color(colors[v])
#     t.fd(100)
#     t.rt(r)
# screen.exitonclick()

#Русская рулетка
# import random
# import time
# print("Время пострелять!")
# j = True
# while j:
#     print("Заряжаем потроны!")
#     time.sleep(3)
#     print("Крутите барабан!")
#     time.sleep(1)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("бум!")
#     d = [1,2,3,4,5,6]
#     f = random.choice(d)
#     g = random.choice(d)
#     if f == g :
#        print("ТЫ ЗДОХ!")
#        time.sleep(0.5)
#        print("СМЭРТЬ!")
#        j = False
#     else:
#         print("ТЕБЕ ПОВЕЗЛО!")
#         x = input("Играем дальше?:")
#         if x == "нет":
#             j = False
