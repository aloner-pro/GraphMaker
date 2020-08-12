from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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


def trigono():
    win2 = Tk()
    win2.title('Trigonometric Graphs')
    win2.geometry('300x300')
    win2.wm_iconbitmap('images\\trig.ico')

    def select(event=None):
        l2.config(text='The graph of ' + cb.get() + ' is')

    li = Label(win2, text='Select the function for which you want graph:')
    li.place(x=5, y=10)
    l2 = Label(win2, text='')
    l2.place(x=5, y=50)

    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')])
    bc = ttk.Button(win2, text="Click Here", style="C.TButton", command=select)
    bc.place(x=200, y=30)

    values = ["sin(x)", 'cos(x)', 'tan(x)', 'cosec(x)', 'sec(x)', 'cot(x)']
    cb = ttk.Combobox(win2, values=values, width=10)
    cb.place(x=10, y=30)
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
            lkj.config(text="The degree of polynomial is " + str(g) + '.')
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
    buti = Label(win4, text="Sorry!", font=30).pack()
    buti2 = Label(win4, text="Currently under Development.").pack()
    win4.mainloop()


phy = Button(main_win, text='Other', fg='yellow', bg='deep sky blue', width=8,
             justify='center', activebackground='powder blue', command=pysco)
phy.place(x=290, y=300)

photo = PhotoImage(file=r"images\exit.png")
photoimage = photo.subsample(1, 1)
qu = Button(main_win, text='Exit', image=photoimage, bg='salmon', fg='yellow',
            compound=LEFT, command=main_win.destroy)
qu.place(x=340, y=360)
C.pack()

main_win.resizable(False, False)
main_win.mainloop()
