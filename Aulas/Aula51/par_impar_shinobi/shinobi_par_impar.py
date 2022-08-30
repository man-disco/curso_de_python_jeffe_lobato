from tkinter import *
from constantes import *
from calculo_par_impar import *

raiz = Tk()


class Janela:
    def __init__(self, raiz):
        # --- Frames ---
        # Frame 1
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()
        # Frame 2
        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()
        # Frame 3
        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()
        # Frame 4
        self.fr4 = Frame(raiz, bg=cinza1)
        self.fr4.pack()
        # Frame 5
        self.fr5 = Frame(raiz, bg=cinza1)
        self.fr5.pack()
        # Frame 6
        self.fr6 = Frame(raiz, bg=cinza1)
        self.fr6.pack()

        #  --- Labels ---
        # Label 1
        self.lb1 = Label(self.fr1, bg=cinza1, font=fonte1, fg=branco, text="Batalha Shinobi", pady=20)
        self.lb1.pack()
        # Label 2
        self.lb2 = Label(self.fr2, bg=cinza1)
        self.lb2.pack()
        # Label 3
        self.lb3 = Label(self.fr3, bg=cinza1)
        self.lb3.pack()
        # Label 4
        self.lb4 = Label(self.fr4, bg=cinza1)
        self.lb4.pack()
        # Label 5
        self.lb5 = Label(self.fr5, bg=cinza1)
        self.lb5.pack()
        # label 6
        self.lb6 = Label(self.fr6, bg=cinza1)
        self.lb6.pack()

        # Imagens
        # Imagem do jogador
        self.img_jogador = PhotoImage(file="arq_projeto_shinobi/jogador.png")
        # Imagem maquina
        self.img_maq = PhotoImage(file="arq_projeto_shinobi/robo.png")
        # Imagens dos números
        self.img0 = PhotoImage(file="arq_projeto_shinobi/0.png")
        self.img1 = PhotoImage(file="arq_projeto_shinobi/1.png")
        self.img2 = PhotoImage(file="arq_projeto_shinobi/2.png")
        self.img3 = PhotoImage(file="arq_projeto_shinobi/3.png")
        self.img4 = PhotoImage(file="arq_projeto_shinobi/4.png")
        self.img5 = PhotoImage(file="arq_projeto_shinobi/5.png")
        self.img6 = PhotoImage(file="arq_projeto_shinobi/6.png")
        self.img7 = PhotoImage(file="arq_projeto_shinobi/7.png")
        self.img8 = PhotoImage(file="arq_projeto_shinobi/8.png")
        self.img9 = PhotoImage(file="arq_projeto_shinobi/9.png")
        self.img10 = PhotoImage(file="arq_projeto_shinobi/10.png")


janela = Janela(raiz)
raiz.geometry("800x400+300+30")
# raiz.iconbitmap('Aulas/Aula51/par_impar_shinobi/arq_projeto_shinobi/jogadorr.ico') não funciona no Ubuntu.
# Tente:
icon = PhotoImage(file="arq_projeto_shinobi/robo_venceu.png")
raiz.tk.call('wm', 'iconphoto', raiz._w, icon)
raiz.title("Shinobi: Par ou Ímpar")
raiz["bg"] = cinza1

raiz.mainloop()
