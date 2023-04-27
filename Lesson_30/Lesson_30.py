from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
#
# def get_lst(bind_e):
#     index=lstbox.curselection()[0]
#     print(lst[index])
#
# lst = ["Первый","Второй","Третий"]
#
# lst_tk = StringVar(value=lst)
# lstbox = Listbox(win,listvariable=lst_tk,selectmode=SINGLE)
# lstbox.pack()
# lstbox.bind("<<ListboxSelect>>",get_lst)





# ===== Верхний блок =====
# frame_top = LabelFrame(win, text="Верх")
# frame_top.pack()
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()
#
# # ===== Нижний блок =====
# frame_bottom = LabelFrame(win, text="Низ")
# frame_bottom.pack()
# Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3").pack()
# Label(frame_bottom, width=7, height=4, bg='lightblue', text="4").pack()
#
#



#================messagebox================

# messagebox.showerror("Заголовок1","Одна ошибка и ты ошибся")
# messagebox.showinfo()
# messagebox .showwarning()
#
#
# #==================== pack ===================
#
# fr= Frame(win)
# fr.pack()
#
# but = Button(win,text= "Перекус таксы")
# but.pack(side=LEFT)
# but2 = Button(win,text= "Перекус таксы")
# but2.pack(side=LEFT)

#=================== grid ==================

# btn1 =Button(win,text="Перекус таксы")
# btn1.grid(row=0,column=0)
# btn2 =Button(win,text="Перекус таксы")
# btn2.grid(row=1,column=1)
# btn3 =Button(win,text="Перекус таксы")
# btn3.grid(row=2,column=2)
# btn4 =Button(win,text="Перекус таксы")
# btn4.grid(row=3,column=3,columnspan=3,sticky=E)

#===================== place =========================
# btn1 = Button(win,text="аьлтцрутаг")
# btn1.place(x= 10,y= 10)

#=================== after ==========================
# def color():
#     btn1["bg"] = "green"
def func(ee):
    print("print")
btn1 = Button(win,text="Что-то")
btn1.pack()
btn1.bind("<Enter>", func)



win.mainloop()