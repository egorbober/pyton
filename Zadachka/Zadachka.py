word = input("Слово:")
sim = input("Символ:")
poluch = sim+""
for i in word:
    poluch += i+sim
print(poluch)
