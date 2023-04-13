import tkinter as tk
def funktia(chtoto):
    msg = ent.get()
    ent.delete(0,"end")
    print(msg)
    lab["text"]= msg
    msg2 = txt.get(0.0, "end")
    txt.delete(0.0, "end")
    print(msg2)

window = tk.Tk()
window.geometry("500x400")
window.title("Писемко")

lab = tk.Label(window,
               text= "Бублики",
               font= "Verbana 18 bold italic",
               bg="orange",
               fg= "yellow",
               width= 50)
lab.pack()

ent = tk.Entry(bd= 10, width= 10)
ent.pack()

btn = tk.Button(window,
               text= "Отправить",
               font= "Verbana 18 bold italic",
               bg="orange",
               fg= "yellow",
               width= 50
                )
btn.pack()
btn.bind("<Button-1>",funktia)

txt = tk.Text(window,width= 20,height= 10)
txt.pack()


window.mainloop()