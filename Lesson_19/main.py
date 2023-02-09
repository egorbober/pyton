import easygui
def adbash(txt):
    rusia = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    english = "ZYXWVUTSRQPONMLKJIHGFEDCBA"[::-1]
    reversid_alfabet = rusia[::-1]
    reversid_alfabet2 = english
    fraza = ""
    for leter in txt:
        if leter not in rusia and leter not in english:
            fraza += leter
        elif leter in rusia:
            bukva=rusia.index(leter)
            bukvari = reversid_alfabet[bukva]
            fraza = fraza + bukvari
        else:
            bukva2= english.index(leter)
            bukvari2 = reversid_alfabet2[bukva2]
            fraza = fraza + bukvari2
    easygui.msgbox(
        msg=fraza
    )
    #print(fraza)


shifr = easygui.enterbox(
        msg= "Чё шифруем?:"
    ).upper()
#shifr=input("Чё шифруем?:").upper()
adbash(shifr)