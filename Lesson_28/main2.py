import tkinter as tk

def funktia(chtoto):
    msg = ent.get()
    ent.delete(0, "end")
    print(msg)
    msg2 = txt.get(0.0, "end")
    txt.delete(0.0, "end")
    print(msg2)

window = tk.Tk()
window.geometry("500x400")
window.title("Писемко")
window.configure(background='white')
lab = tk.Label(window,
               text= "Ваш адрес:",
               font= "Verbana 18 bold italic",
               bg="white",
               fg= "black",
               width= 10)
lab.pack()
ent = tk.Entry(bd= 3, width= 20)
ent.pack()

lab2 = tk.Label(window,
               text= "Коменты:",
               font= "Verbana 18 bold italic",
               bg="white",
               fg= "black",
               width= 10)
lab2.pack()

txt = tk.Text(window,width= 20,height= 10)
txt.pack()

btn = tk.Button(window,
               text= "Отправить",
               font= "Verbana 18 bold italic",
               bg="blue",
               fg= "black",
               width= 20
                )
btn.pack()
btn.bind("<Button-1>",funktia)



window.mainloop()