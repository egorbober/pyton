from collections import namedtuple

citizen = namedtuple("Житель: имя возвраст статус какую_группу_ты_уважаешь")
alex = citizen(Имя= "Саня", Возвраст= "1.3 года", Статус= "чел",Какую_группу_ты_уважаешь="голубые")
print(alex.Имя)
print(alex.Возвраст)
print(alex.Статус)
print(alex.Какую_группу_ты_уважаешь)