from tkinter import *


class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg="#8bb158", highlightbackground="black", highlightthickness=3)
        self.lb1 = Label(self.fr1, text="Olá mundo", bg="#8bb158", font=('Mono', 23), )
        self.lb1['relief'] = RIDGE
        self.lb1['border'] = 2
        self.lb1.pack(side=LEFT)
        self.fr1.pack()

        self.img = PhotoImage(file="2478184.png")
        self.lb_img = Label(raiz, image=self.img)
        self.fr2 = Frame(raiz, bg="#8bb158")
        self.fr2.pack()

        self.bt1 = Button(self.fr2, text='Clique aqui!', bg="GREEN", font=('Mono', 23,),
                          command=self.muda_label)
        self.bt1.bind("<Tab>", self.muda_label2)
        self.bt1['relief'] = RAISED
        self.bt1['border'] = 5
        self.bt1.pack(side=LEFT)

        self.lb2 = Label(self.fr1, text='   ', bg="#8bb158")
        self.lb2.pack(side=RIGHT)

        self.lb2 = Label(self.fr2, text='   ', bg="#8bb158")
        self.lb2.pack(side=RIGHT)

    def muda_label(self):
        self.lb1["text"] = "Deu certo! (muda_label)"
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

    def muda_label2(self, event):
        self.lb1["text"] = "Deu certo! (muda_label2)"


raiz = Tk()
Janela(raiz)
raiz.geometry("800x600+100+0")
raiz.title("Meu programa")
raiz["bg"] = '#8bb158'

# Por eu estar no linux mint (Ubuntu) por algum motivo o arquivo '.ico' não é reconhecido então eu pulei essa
# parte.

raiz.mainloop()
