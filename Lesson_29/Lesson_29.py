import tkinter as tk


root = tk.Tk()
root.geometry("400x500")
#val_cb = tk.BooleanVar()


# def check():
#         print(val_cb.get())


# cb = tk.Checkbutton(root,
#                     text= "Подписка",
#                     font= 15,
#                     bg= "pink",
#                     variable= val_cb,
#                     onvalue= True,
#                     offvalue= False,
#                     command= check
#                     )
# cb.pack()



# def rb():
#     print(val_rb.get())
#
# val_rb1= tk.IntVar()
# rb1 = tk.Radiobutton(root,
#                      text= "Я почему то РАДИОкнопка",
#                      variable= val_rb1,
#                      value= 246,
#                      command=rb)
#
# val_rb= tk.IntVar()
# rb2 = tk.Radiobutton(root,
#                      text= "Я почему то РАДИОкнопка",
#                      variable= val_rb,
#                      value= 0,
#                      command=rb)
# rb1.pack()
# rb2.pack()




# def get_skala(chtoto):
#     print(skala.get())
#     print(chtoto)
#
# skala= tk.Scale(root,
#                 from_= 500,
#                 to= 1000,
#                 width= 50,
#                 length= 300,
#                 orient= tk.HORIZONTAL,
#                 tickinterval= 100,
#                 resolution= 50  ,
#                 command= get_skala
#                 )
#
#
# skala.pack()



img = tk.PhotoImage(file= "амогус.png")
img = img.subsample(3,3)
img = img.zoom(2,2)
lab= tk.Label(root,
              image= img)

lab.pack()



# def svitch():
#     if btn2["state"] == "disabled":
#         btn2["state"] = "normal"
#     else:
#         btn2["state"] = "disabled"
#
# btn1= tk.Button(root,
#                 text= "Нажмёшь - лох",
#                 command= svitch,
#                 fg= "red",
#                 width= 30,
#
#                 )
# btn2= tk.Button(root,
#                 text= "Нажмёшь - хорош",
#                 state= tk.DISABLED,
#                 fg="red",
#                 disabledforeground= "black",
#                 width= 30
#                 )
# btn1.pack(pady=20, ipady= 20)
# btn2.pack()
#
#
# ent = tk.Entry(root)
#
#
# ent.pack()
# ent.insert(tk.END, "Перекус бобра чеeeк...")
#





root.mainloop()