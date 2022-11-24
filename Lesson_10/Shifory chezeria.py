alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = [" ",",","(",")","?","!"]
should_end = False

while should_end == False:
    txt = input("слово:").lower()
    txt = list(txt) #строка -> список

    shift = int(input("Сдвиг на:"))

    if shift > len(alphabet): #Если больше 26
        shift = shift % len(alphabet)

    elif shift < -len(alphabet): # len уволили!
        shift = shift % -len(alphabet)
           #!МЕХАНИЗМ СДВИГА!
    chiper_txt = ""
    for later in txt:
        if later in symbol:
            chiper_txt += later
        else:
            position = alphabet.index(later)
            if position + shift >len (alphabet):
                new_position = position + shift - len (alphabet)
            elif position + shift < 0:
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            chiper_txt += alphabet[new_position]
    print (chiper_txt)
