from tkinter import *
from tkinter import ttk
y = 0
x = 0
n = [2, 3, 4, 4, 3, 2]


def ok():
    global y
    global x
    if n[y] == x:
        usage = f'le renard a été trouvé en {x} ème position'
        y = 0
        x = 0
    else:
        usage = f'le renard n a pas été trouvé en {n[y]} ème position'
        y += 1
    usage_label["text"] = usage


def reset():
    global y
    global x
    if x != n[y]:
        usage = f'reset'
        usage_label["text"] = usage
    x = 0
    y = 0


def x1():
    global x
    if y == 0:
        x = 1
        ok()
    if x == 2:
        x = 1
        ok()


def x2():
    global x
    if y == 0:
        x = 2
        ok()
    if x == 3:
        x = 2
        ok()
    if x == 1:
        x = 2
        ok()


def x3():
    global x
    if y == 0:
        x = 3
        ok()
    if x == 4:
        x = 3
        ok()
    if x == 2:
        x = 3
        ok()


def x4():
    global x
    if y == 0:
        x = 4
        ok()
    if x == 3:
        x = 4
        ok()
    if x == 5:
        x = 4
        ok()


def x5():
    global x
    if y == 0:
        x = 5
        ok()
    if x == 4:
        x = 5
        ok()


fenetre = Tk()
image2 = PhotoImage(file="renard.png")
fenetre.title("le renard")
image2_label = ttk.Label(image=image2)
image2_label.place(y=0, x=0)
fenetre.config(width=900, height=800, background='white')
bouton1 = Button(text="     1     ", command=x1, activebackground="white")
bouton2 = Button(text="     2     ", command=x2, activebackground="white")
bouton3 = Button(text="     3     ", command=x3, activebackground="white")
bouton4 = Button(text="     4     ", command=x4, activebackground="white")
bouton5 = Button(text="     5     ", command=x5, activebackground="white")
reset = Button(text="         reset         ", command=reset, activebackground="white")
bouton1.place(x=350, y=375)
bouton2.place(x=450, y=400)
bouton3.place(x=550, y=400)
bouton4.place(x=650, y=400)
bouton5.place(x=750, y=375)
reset.place(x=525, y=480)
usage_label = ttk.Label()
usage_label.place(x=450, y=450)


fenetre.mainloop()
