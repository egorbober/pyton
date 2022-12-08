from collections import namedtuple

citizen = namedtuple("Житель: ""Имя возвраст статус какую_группу_ты_уважаеш")
alex =  citizen(Имя= "Саня", Возвраст= "1.3 года", Статус= "чел",Какую_группу_ты_уважаешь="голубые")
print (alex.имя)
print (alex.возвраст)
print (alex)