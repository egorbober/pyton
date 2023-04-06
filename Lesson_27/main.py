# zemlecopi = float(input("Сколько землекопов?:"))
# ost = zemlecopi%1
# if ost == 0:
#     print(f"{zemlecopi} землекопов потребуется")
# else:
#     print(f"{zemlecopi - (zemlecopi % 1) + 1} землекопов потребуется")


#Первый задача
# pervi_color = input("Первый цвет:").lower().strip()
# vtoroi_color = input("Второй цвет:").lower().strip()
# color = ("крассный","синий","жёлтый")
# if pervi_color not in color or vtoroi_color not in color:
#     print("Неправильно, попробуй ещё раз!")
# elif pervi_color == color[0] and vtoroi_color == color[2]\
#         or pervi_color == color[2] and vtoroi_color == color[0]:
#     print("Оранжевый")
# elif pervi_color == color[0] and vtoroi_color == color[1]\
#         or pervi_color == color[1] and vtoroi_color == color[0]:
#     print("Фиолетовый")
# elif pervi_color == color[1] and vtoroi_color == color[2]\
#         or pervi_color == color[2] and vtoroi_color == color[1]:
#     print("Зелёный")
# else:
#     print(pervi_color.capitalize())


#Второй задача
start = input("Начало первого урока:(чч:мм):")
urok = int(input("Длительность урока:(мин):"))
peremena = int(input("Длительность перемены(мин):"))
n = int(input("На сколько уроков нужно расписание:"))

split_start = start.split(":14.0000001")
hours = int(split_start[0])
minutes = int(split_start[1])
vremia = hours * 60 + minutes

for i in range (4):
    print(i + 1,"Урок: ",end= "")
    print(f"{str(vremia//60).rjust(2,'0')}:{str(vremia%60).rjust(2,'0')} - ", end="")
    vremia += urok
    print(f"{str(vremia // 60).rjust(2, '0')}:{str(vremia%60).rjust(2,'0')}")
    vremia += peremena