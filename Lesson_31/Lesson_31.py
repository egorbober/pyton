from tkinter import *
root = Tk()
root.geometry("500x500")



c = Canvas(root,
           width=500,
           height=500,
           bg= "orange")


c.pack(anchor= CENTER, expand= True)

# #===============Текст================

# c.create_text(250,250,
#              text= "Пельмени * 15,5",
#              font= "Arial 15",
#               fill= "gold4",
#               anchor= NW)

#===============Rectamble================

# c.create_rectangle(100,10,
#                    20,160,
#                    fill= "red2",
#                    width= 4,
#                    outline= "dark blue")

#===============Многоуголник================

# c.create_polygon(10,10,
#                  50,50,
#                  10,50)

#===============Окружность================

# c.create_oval(10,10,
#               100,100)

#===============arc================

# c.create_oval(10,10,
#               150,150,
#               fill= "silver")
#
# c.create_arc(10,10,
#              150,150,
#              fill= "red",
#              start= 45,
#              extent= -90)
#
# c.create_arc(10,10,
#              150,150,
#              fill= "blue",
#              start= 90,
#              extent= 135,
#              style=CHORD)
#
# c.create_arc(10,10,
#              150,150,
#              fill= "magenta",
#              start= 110,
#              extent= 135,
#              style=ARC,
#              width= 10)

#===============lines================
# c.create_line(10,10,
#               150,150,
#               width= 5,
#               arrow= BOTH,
#               arrowshape=(10,10,10))

#===============dash================
#
# c.create_rectangle(100,10,
#                    20,160,
#                    fill= "red2",
#                    width= 4,
#                    outline= "dark blue",
#                    dash=".- -.",
#                    activefill= "blue",
#                    activewidth= 10)





root.mainloop()