import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("Цветь")
window.configure(background='white')

def funktia(chtoto):
    msg = chtoto.bg()
    print(msg)
lab = tk.Label(window,
               text= "Выбери цветь",
               font= "Verbana 18 bold italic",
               bg="white",
               fg= "black",
               width= 20)
lab.pack()

btn1 = tk.Button(window,
               bg="red",
               width= 20
                )
btn1.pack()
btn1.bind("<Button-1>",funktia)

btn2 = tk.Button(window,
               bg="orange",
               width= 20
                )
btn2.pack()
btn2.bind("<Button-1>",funktia)

btn3 = tk.Button(window,
               bg="yellow",
               width= 20
                )
btn3.pack()
btn3.bind("<Button-1>",funktia)

btn4 = tk.Button(window,
               bg="green",
               width= 20
                )
btn4.pack()
btn4.bind("<Button-1>",funktia)

btn5 = tk.Button(window,
               bg="lightblue",
               width= 20
                )
btn5.pack()
btn5.bind("<Button-1>",funktia)

btn6 = tk.Button(window,
               bg="blue",
               width= 20
                )
btn6.pack()
btn6.bind("<Button-1>",funktia)

btn7 = tk.Button(window,
               bg="purple",
               width= 20
                )
btn7.pack()
btn7.bind("<Button-1>",funktia)







window.mainloop()