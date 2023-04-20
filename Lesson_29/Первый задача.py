import tkinter as tk

root = tk.Tk()


#
# def kak_hochesh():
#     if btn["state"] == "disabled":
#         btn["state"] = "normal"
#         btn["text"] = "Активен"
#     else:
#         btn["state"] = "disabled"
#         btn["text"] = "Не активен"
#

# cb = tk.Checkbutton(root,
#                     text= "Активировать",
#                     command= kak_hochesh)
# cb.pack()
# # cb.select()
#
#
# btn= tk.Button(root,
#                text= "Не активен",
#                state= tk.DISABLED)
#
#
# btn.pack()
#
#
def bold():
    if cb1_val.get():  # если св1 == True
        lab["font"] += " bold"
    else:
        lab["font"] = lab["font"].replace(" bold", "")


def italic():
    if cb2_val.get():  # если св1 == True
        lab["font"] += " italic"
    else:
        lab["font"] = lab["font"].replace(" italic", "")


def overs():
    if cb3_val.get():  # если св1 == True
        lab["font"] += " overstrike"
    else:
        lab["font"] = lab["font"].replace(" overstrike", "")


def und():
    if cb4_val.get():  # если св1 == True
        lab["font"] += " underline"
    else:
        lab["font"] = lab["font"].replace(" underline", "")


lab = tk.Label(root,
               text="abc",
               font="Arial 12")
lab.pack()
# =========
cb1_val = tk.BooleanVar()
cb1 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=bold
                     )
cb1.pack()
# =========
cb2_val = tk.BooleanVar()
cb2 = tk.Checkbutton(root,
                     text="Курсив",
                     variable=cb2_val,
                     onvalue=True,
                     offvalue=False,
                     command=italic
                     )
cb2.pack()
# =========
cb3_val = tk.BooleanVar()
cb3 = tk.Checkbutton(root,
                     text="Зачеркнутый",
                     variable=cb3_val,
                     onvalue=True,
                     offvalue=False,
                     command=overs
                     )
cb3.pack()
# =========
cb4_val = tk.BooleanVar()
cb4 = tk.Checkbutton(root,
                     text="Подчеркнутый",
                     variable=cb4_val,
                     onvalue=True,
                     offvalue=False,
                     command=und
                     )
cb4.pack()

root.mainloop()