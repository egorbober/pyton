import random
import Risunci

print(Risunci.intro)
life = 6
vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_anser = random.choice(vocabulary)
word_display = []

for _ in range(len(word_anser)):
    word_display.append("_")

print (word_display)
counter = 0

while life > 0 and counter != len(word_anser):
    print(Risunci.stages[life])
    leter_is_be = False
    leter = input ("Буква:").lower()
    for i in range (len(word_anser)):
        if leter == word_anser[i]:
            if word_display[i] != "_":
                leter_is_be = True
            else:
                word_display[i] = leter
                counter += 1
                leter_is_be = True
    if leter_is_be == False:
        life -= 1
    print (word_display)

if counter == len(word_anser):
    print("!!!Победа!!!")
else:
    print("!!!Проиграл!!!")
    print(Risunci.stages[life])
    print(word_anser)
