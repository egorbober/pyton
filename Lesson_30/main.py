from tkinter import *
win=Tk()


#================ Первый задача ====================

# Label(win,text="Логин:").grid(row=0, column= 0)
# Label(win,text="Пароль:").grid(row=1, column= 0)
# Entry(win).grid(row=0, column= 0,pady= 5)
# Entry(win).grid(row=1, column= 0,pady=5)
# Button(win, text="Авторизация").grid()


#====================  Второй задача ========================

from random import  randint

def move(e):
    btn.place(x= randint(1,250),y= randint(1,250))

btn= Button(win,text="НЕ нажимай", bg= "green")
btn.place(x=10,y=10)
btn.bind("<Enter>",move)

#================ Третий задача =======================

# def blablabla():
#     rb_val.set(randint(1,5))
#     win.after(1000,blablabla)
#
# win.geometry("200x300")
# fr = Frame()
# fr.pack(anchor=NW)
# rb_val = IntVar()
# rb1 = Radiobutton(fr,variable=rb_val, value=1)
# rb1.pack(side= LEFT)
# rb1["bg"]= "pink"
# rb2 = Radiobutton(fr,variable=rb_val, value=2)
# rb2.pack(side= LEFT)
# rb2["bg"]= "orange"
# rb3 = Radiobutton(fr,variable=rb_val, value=3)
# rb3.pack(side= LEFT)
# rb3["bg"]= "black"
# rb4 = Radiobutton(fr,variable=rb_val, value=4)
# rb4.pack(side= LEFT)
# rb4["bg"]= "red"
# rb5 = Radiobutton(fr,variable=rb_val, value=5)
# rb5.pack(side= LEFT)
# rb5["bg"]= "blue"

# blablabla()
win.mainloop()