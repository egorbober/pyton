import easygui

# result = easygui.msgbox(
#     msg="С днём дня!!!",
#     title="Я карта!",
#     ok_button="Понял,принял",
#     image="Img/лягушка.png"
# )
# if result == None:
#     print("хорошего дня дружочек ❤")
# elif result == "Img/лягушка.png":
#     print("Ты то, на что нажал! (лягушка 🐸)")



# easygui.buttonbox(
#     msg= "Выбери кто ты!!!",
#     choices= ("Заниженный", "Умеренный", "Завышенный"),
#     images=["Img/бобёр.png","Img/бобёр.png","Img/бобёр.png"],
#     title= "Кто ты???"
# )



# easygui.integerbox(
#     msg="Сколько раз",
#     title="Чиселко",
#     lowerbound= 10,
#     upperbound= 50,
#     image="Img/бобёр.png",
#     default= 46
# )


# easygui.enterbox(
#     msg="Никнейм",
#     title="Кто ты???",
#     image="Img/бобёр.png"
# )


# import easygui
# import random
#
#
#
# def rock_paper_scissors(otvet=None):
#     znachenie = {1:"Img/камень.png",
#             2:"Img/ножницы.png",
#             3:"Img/бумага.png"
#             }
#     result = easygui.buttonbox(
#         msg= "Выбирай",
#         title=  "Игра",
#         images= ["Img/камень.png","Img/ножницы.png","Img/бумага.png"],
#         choices= []
#     )
#     print(znachenie.keys())
#     #comp = random.choice(list(znachenie.keys()))
#     comp = "ножницы"
#     print(comp)
#     if result == znachenie["камень"] and comp == "ножницы":
#         easygui.msgbox(msg= "Хорош")
#
#
#
# def guess_the_number():
#     easygui.msgbox('Здесь будет игра "Угадай число"')
#
#
# games = [
#     'Камень, ножницы, бумага',
#     'Угадай число'
# ]
#
# games_entry_points = [
#     rock_paper_scissors,
#     guess_the_number
# ]
#
# while True:
#     res = easygui.buttonbox('Выбери игру!', choices=games)
#     if res is None:
#         break
#     games_entry_points[games.index(res)]()



easygui.integerbox(
    upperbound= 75,
    lowerbound= 50
)



