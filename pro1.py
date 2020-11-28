from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

main_win = Tk()
main_win.title("Graph Maker")
main_win.wm_iconbitmap('images\\logo1.ico')

C = Canvas(main_win, bg="blue", height=400, width=400)
filename = PhotoImage(file="images\\graph.png")
background_label = Label(main_win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lb = Label(main_win, text="Welcome to\nGraph Maker", font=('Cooper Black', 20), fg='light coral')
lb.place(x=30, y=10)
lb2 = Label(main_win, text="Click on the type of graph you want:", fg='navy', font=('Franklin Gothic Demi', 12))
lb2.place(x=90, y=260)
lb3 = Label(main_win, text='Created with  😁  & </> by 👨🏻‍💻', fg='deep pink', font=10)
lb3.place(x=0, y=380)


def formalities():
    plt.xlabel("x axis")
    plt.grid(True, which='both')
    plt.axhline(y=0, color='#FF7F00')
    plt.axvline(x=0, color='#FF7F00')
    radian_multiples = [-2, -3 / 2, -1, -1 / 2, 0, 1 / 2, 1, 3 / 2, 2]
    radians = [n * np.pi for n in radian_multiples]
    radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
    plt.xticks(radians, radian_labels)
    plt.show()


def trigono():
    win2 = Tk()
    win2.geometry('300x300')
    win2.title('Trigonometric Graphs')
    win2.wm_iconbitmap('images\\trig.ico')
    values = ["sin(x)", 'cos(x)', 'tan(x)', 'cot(x)', 'sec(x)', 'cosec(x)']

    def select(event=None):

        def sine():
            plt.ylabel("$sin(x)$")
            x = np.arange(-2*np.pi, 2*np.pi, 0.01)
            y = np.sin(x)
            plt.plot(x, y)
            plt.title('Sin(x)')
            formalities()

        def cosine():
            plt.ylabel("$cos(x)$")
            x = np.arange(-2*np.pi, 2*np.pi, 0.01)
            y = np.cos(x)
            plt.plot(x, y)
            plt.title('Cos(x)')
            formalities()

        def tangent():
            plt.ylabel("$tan(x)$")
            x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
            y = np.tan(x)
            y[:-1][np.diff(y) < 0] = np.nan
            plt.ylim(-3, 3)
            plt.plot(x, y)
            plt.title('Tan(x)')
            formalities()

        def cotangent():
            plt.ylabel("$cot(x)$")
            x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
            y = 1 / (np.tan(x))
            y[:-1][np.diff(y) > 0] = np.nan
            plt.ylim(-3, 3)
            plt.plot(x, y)
            plt.title('Cot(x)')
            formalities()

        if cb.get() == values[0]:
            sine()
        elif cb.get() == values[1]:
            cosine()
        elif cb.get() == values[2]:
            tangent()
        elif cb.get() == values[3]:
            cotangent()

    li = Label(win2, text='Select the function for\nwhich you want graph:', font=('Cooper Black', 12))
    li.place(x=5, y=10)
    l2 = Label(win2, text='')
    l2.place(x=5, y=50)

    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    bc = ttk.Button(win2, text="Click Here", style="C.TButton", command=select)
    bc.place(x=200, y=50)

    cb = ttk.Combobox(win2, values=values, width=10)
    cb.place(x=10, y=50)
    cb.current(0)

    win2.bind('<Return>', select)
    win2.mainloop()


trig = Button(main_win, text='Trigonometric', fg='yellow', bg='deep sky blue',
              justify='center', activebackground='powder blue', command=trigono)
trig.place(x=20, y=300)


def poly_act():
    win3 = Tk()
    win3.title('Polynomial Graphs')
    win3.geometry('300x300')
    win3.wm_iconbitmap('images\\poly.ico')
    lk = Label(win3, text='Enter the degree of the polynomial')
    lk.place(x=0, y=10)

    def funk(event=None):
        try:
            g = int(ent.get())
            values = [i+1 for i in range(g)]

            lkj.config(text="The degree of the polynomial is " + str(g) + '.')
        except ValueError:
            messagebox.showerror('ValueError', 'Degree of a polynomial\nis a integer number.')

    lkj = Label(win3, text="")
    lkj.place(x=5, y=35)
    ent = Entry(win3, width=12, background='powder blue')
    ent.place(x=190, y=10)
    ent.focus()
    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    bh = ttk.Button(win3, text="Click Here", style="C.TButton", command=funk)
    bh.place(x=180, y=35)
    win3.bind('<Return>', funk)
    win3.mainloop()


poly = Button(main_win, text='Polynomial', fg='yellow', bg='deep sky blue',
              justify='center', activebackground='powder blue', command=poly_act)
poly.place(x=165, y=300)


def pysco():
    win4 = Tk()
    win4.title('Other Graphs')
    win4.geometry('300x300')
    buti = Label(win4, text="Sorry!", font=30)
    buti.pack()
    buti2 = Label(win4, text="Currently under Development.")
    buti2.pack()
    win4.mainloop()


phy = Button(main_win, text='Other', fg='yellow', bg='deep sky blue', width=8,
             justify='center', activebackground='powder blue', command=pysco)
phy.place(x=290, y=300)

photo = PhotoImage(file=r"images/exit.png")
photoimage = photo.subsample(1, 1)
qu = Button(main_win, text='Exit', image=photoimage, bg='salmon', fg='yellow',
            compound=LEFT, command=main_win.destroy)
qu.place(x=340, y=360)
C.pack()

main_win.resizable(False, False)
main_win.mainloop()
