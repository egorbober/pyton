from tkinter import *
win= Tk()
win.geometry("500x500")
c = Canvas(win,width=500,height= 500,bg= "orange")
c.pack(anchor= CENTER,expand=True)

#=================== Первый задача ====================

# img = PhotoImage(file="Clocks.png").subsample(4,4)
# timer = 0
#
# def poop():
#     global timer
#     c.delete("all")
#     timer += 1
#     c.create_text(250,255,text=timer,font= "Arial 15")
#     c.create_image(250, 250, image=img)
#     c.after(1000,poop)
#     if timer == 16:
#         win.destroy()
#
# c.create_text(250,250,text=timer,font= "Arial 15")
# poop()
#
# c.create_image(250,250,image=img)

#================= Второй задача ==================

c.create_text(10,10,anchor=NW,
              text= "Школа",
              font= "Arial 15")
c.create_line(150,30,250,30,arrow=LAST)

c.create_text(300,10,anchor=NW,
              text= "Я",
              font= "Arial 15")
c.create_line(350,30,350,100,arrow=LAST)

c.create_text(325,120,anchor=NW,
              text= "Дом",
              font= "Arial 15")





win.mainloop()