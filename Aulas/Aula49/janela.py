from tkinter import *


class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz)
        self.fr1.pack()
        self.lb1 = Label(self.fr1, text="Olá mundo", background="grey", font=('Liberation', 23), )
        self.lb1.pack(side=LEFT)

        self.img = PhotoImage(file="2478184.png")

        self.fr2 = Frame(raiz)
        self.fr2.pack()

        self.bt1 = Button(self.fr2, text='Clique aqui!', background="#8bb158", font=('Times', 23, 'italic',),
                          command=self.muda_label)
        self.bt1.bind("<Tab>", self.muda_label2)
        self.bt1.pack(side=LEFT)

        self.lb2 = Label(self.fr1, text='   ', width=100)
        self.lb2.pack(side=RIGHT)

        self.lb2 = Label(self.fr2, text='   ', width=100)
        self.lb2.pack(side=RIGHT)

    def muda_label(self):
        self.lb1["text"] = "Deu certo! (muda_label)"
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

    def muda_label2(self, event):
        self.lb1["text"] = "Deu certo! (muda_label2)"


raiz = Tk()
Janela(raiz)
raiz.geometry("800x600+0+0")
raiz.mainloop()
