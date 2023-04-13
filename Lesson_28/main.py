import tkinter as tk

def baget(event):
    print("Я круасан(❁´◡`❁)")

okno = tk.Tk()
okno.geometry("500x400")
okno.title("Моё первое окошко")

btn = tk.Button(okno,text= "Моя первая онопочька <:")
btn.pack()
btn["text"]="Ы"
btn["font"]=("Arial Black",
             14,
             "bold",
             "underline",
             "italic",
             "overstrike"
             )
#btn["background"]= "gold4"
btn["bg"]= "orange"
#btn["foreground"]= "pink"
btn["fg"]= "yellow"
btn["width"]= 10
btn["height"]= 3
btn["bd"]= 10
#btn["command"]= baget
btn.bind("<Double-Button-1>",baget)

okno.mainloop()
