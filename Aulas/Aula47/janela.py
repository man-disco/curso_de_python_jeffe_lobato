from tkinter import *


class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz)
        self.fr1.pack()
        self.lb1 = Label(self.fr1, text="Olá mundo")
        self.lb1.pack()
        self.bt1 = Button(self.fr1, text='Olá pycharm')
        self.bt1.pack()


raiz = Tk()
Janela(raiz)
raiz.geometry("800x600+0+0")
raiz.mainloop()
