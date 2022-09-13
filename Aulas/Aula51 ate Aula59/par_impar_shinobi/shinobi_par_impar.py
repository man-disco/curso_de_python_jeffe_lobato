import random
from tkinter import *
from calculo_par_impar import *
from constantes import *
import tkinter.messagebox as mbox
raiz = Tk()


# noinspection PyStatementEffect

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
        # Frame 7
        self.fr7 = Frame(raiz, bg=cinza1)
        self.fr7.pack()
        # Frame 8
        self.fr8 = Frame(raiz, bg=cinza1)
        self.fr8.pack()
        # -- Imagens --
        # Imagem do jogador
        self.img_jogador = PhotoImage(file="arq_projeto_shinobi/jogador.png")
        # Imagem da maquina
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

        # -- Variáveis --
        self.placar1 = 0
        self.placar2 = 0
        self.escolha = StringVar()
        self.rb_par = Radiobutton(self.fr4, text="Par", value="par", variable=self.escolha, bg=cinza1, fg=branco,
                                  font=fonte2, pady=20, padx=20, selectcolor=cinza1, highlightthickness=0,
                                  activebackground=cinza1)
        self.rb_par.pack(side=LEFT)
        self.lb_separador2 = Label(self.fr4, text="  ", bg=cinza1)
        self.lb_separador2.pack(side=LEFT)
        self.rb_impar = Radiobutton(self.fr4, text="Ímpar", value="impar", variable=self.escolha, bg=cinza1, fg=branco,
                                    font=fonte2, pady=20, padx=20, selectcolor=cinza1, highlightthickness=0,
                                    activebackground=cinza1)

        self.rb_impar.pack(side=LEFT)
        self.num = Entry(self.fr5, background=cinza1, width=2, font=('Ubuntu', 15, "bold"), fg=branco, borderwidth=0,
                         border=0)
        self.num.pack(side=RIGHT)

        self.lb_separador3 = Label(self.fr6, text=" ", bg=cinza1)
        self.lb_separador3.pack()
        self.bt_jogar = Button(self.fr6, bg=cinza1, text="Jogar", width=12, fg=branco, font=fonte2, padx=40,
                               command=self.jogar, borderwidth=0, cursor="hand2")
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack()

        self.bt_restart = Button(self.fr7, bg=cinza1, text="Reiniciar", width=12, fg=branco, font=fonte2, padx=40,
                                 command=self.restart, borderwidth=0, cursor="hand2")
        self.bt_restart.bind("<Return>", self.restart)
        self.bt_restart.pack()
        self.bt_info = Button(self.fr8, bg=cinza1, text="Info", width=4, fg=branco, font=fonte2,
                              command=self.info, borderwidth=0,)
        self.bt_info.bind("<Return>", self.info)
        self.bt_info.pack(side=RIGHT)

        #  --- Labels ---
        # Label 1
        self.lb1 = Label(self.fr1, bg=cinza1, font=fonte1, fg=branco, text="Par ou Ímpar", pady=20)
        self.lb1.pack()
        # Label separa botão info e titulo
        self.lb_separador4 = Label(self.fr1, text="       ", bg=cinza1, padx=50)
        self.lb_separador4.pack(side=RIGHT)
        # Label resultado
        self.lb_result = Label(self.fr1, bg=cinza1, font=fonte2, fg="green", text="", padx=1)
        self.lb_result.pack()
        # Label (imagem) jogador
        self.lb_img1 = Label(self.fr3, image=self.img_jogador)
        self.lb_img1.pack(side=LEFT)
        # Label separador
        self.lb_separador = Label(self.fr3, text="  ", bg=cinza1)
        self.lb_separador.pack(side=LEFT)
        # Label (imagem) robo
        self.lb_img2 = Label(self.fr3, image=self.img_maq)
        self.lb_img2.pack(side=RIGHT)
        # Label 2
        self.lb2 = Label(self.fr1, bg=cinza1, font=fonte2, fg=branco, text="                         Jogador/a        "
                                                                           + str(self.placar1) +
                                                                           "     X    " + str(self.placar2) +
                                                                           "       Máquina", padx=10)
        self.lb2.pack()
        # Label 3
        self.lb3 = Label(self.fr5, bg=cinza1, text="Número de 1 a 10: ", fg=branco, font=fonte2)
        self.lb3.pack(side=LEFT)
        # Label 4
        self.lb4 = Label(self.fr4, bg=cinza1)
        self.lb4.pack()
        # Label 5
        self.lb5 = Label(self.fr5, bg=cinza1)
        self.lb5.pack()
        # label 6
        self.lb6 = Label(self.fr6, bg=cinza1)
        self.lb6.pack()
        # Label mensagem erro
        self.lb_erro = Label(self.fr7, bg=cinza1, text="", fg=vermelho, font=fonte2, pady=10)
        self.lb_erro.pack(side=RIGHT)
        # -- Funções --

    def jogar(self):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0, 11)

            if escolha == 'par' or escolha == 'impar':

                if num == 0:
                    self.lb_img1['image'] = self.img0
                elif num == 1:
                    self.lb_img1['image'] = self.img1
                    self.lb_erro["text"] = ""
                elif num == 2:
                    self.lb_img1['image'] = self.img2
                    self.lb_erro["text"] = ""
                elif num == 3:
                    self.lb_img1['image'] = self.img3
                    self.lb_erro["text"] = ""
                elif num == 4:
                    self.lb_img1['image'] = self.img4
                    self.lb_erro["text"] = ""
                elif num == 5:
                    self.lb_img1['image'] = self.img5
                    self.lb_erro["text"] = ""
                elif num == 6:
                    self.lb_img1['image'] = self.img6
                    self.lb_erro["text"] = ""
                elif num == 7:
                    self.lb_img1['image'] = self.img7
                    self.lb_erro["text"] = ""
                elif num == 8:
                    self.lb_img1['image'] = self.img8
                    self.lb_erro["text"] = ""
                elif num == 9:
                    self.lb_img1['image'] = self.img9
                    self.lb_erro["text"] = ""
                elif num == 10:
                    self.lb_img1['image'] = self.img10
                    self.lb_erro["text"] = ""
                else:
                    self.lb_erro["text"] = "Erro: Escolha um número de 0 até 10."

                if escolha != 'par' and escolha != 'impar':
                    self.lb_erro["text"] = "Ação invalida, tente novamente."

                if 0 <= num <= 10:
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == "par":
                        self.lb_result['text'] = "                         " + str(num + num_robo) + ' Deu Par'
                    elif par_impar == "impar":
                        self.lb_result['text'] = "                         " + str(num + num_robo) + ' Deu Ímpar'
                    else:
                        self.lb_erro["text"] = "Erro: Escolha par ou ímpar e digite um número até 10."

                        # Pontuações
                    if par_impar == "par" and escolha == "par":
                        self.placar1 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"
                    elif par_impar == "par" and escolha == "impar":
                        self.placar2 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"
                    if par_impar == "impar" and escolha == "impar":
                        self.placar1 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"

                    elif par_impar == "impar" and escolha == "par":
                        self.placar2 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(
                            self.placar1) + "     X    " + str(
                            self.placar2) + "      Máquina"

                    # Altera imagem do robo
                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0

                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1

                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2

                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3

                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4

                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5

                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6

                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7

                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8

                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9

                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10
                    else:
                        self.lb_erro["text"] = "Erro: Escolha um número entre 0 e 10."
            else:
                self.lb_erro["text"] = "Erro: Por favor escolha par ou ímpar."

        except ValueError:
            self.lb_erro["text"] = "Erro: Digite um valor entre 0 e 10."

    def jogar2(self, event):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0, 11)

            if escolha == 'par' or escolha == 'impar':

                if num == 0:
                    self.lb_img1['image'] = self.img0
                elif num == 1:
                    self.lb_img1['image'] = self.img1
                    self.lb_erro["text"] = ""
                elif num == 2:
                    self.lb_img1['image'] = self.img2
                    self.lb_erro["text"] = ""
                elif num == 3:
                    self.lb_img1['image'] = self.img3
                    self.lb_erro["text"] = ""
                elif num == 4:
                    self.lb_img1['image'] = self.img4
                    self.lb_erro["text"] = ""
                elif num == 5:
                    self.lb_img1['image'] = self.img5
                    self.lb_erro["text"] = ""
                elif num == 6:
                    self.lb_img1['image'] = self.img6
                    self.lb_erro["text"] = ""
                elif num == 7:
                    self.lb_img1['image'] = self.img7
                    self.lb_erro["text"] = ""
                elif num == 8:
                    self.lb_img1['image'] = self.img8
                    self.lb_erro["text"] = ""
                elif num == 9:
                    self.lb_img1['image'] = self.img9
                    self.lb_erro["text"] = ""
                elif num == 10:
                    self.lb_img1['image'] = self.img10
                    self.lb_erro["text"] = ""
                else:
                    self.lb_erro["text"] = "Erro: Escolha um número de 0 até 10."

                if escolha != 'par' and escolha != 'impar':
                    self.lb_erro["text"] = "Ação invalida, tente novamente."

                if 0 <= num <= 10:
                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == "par":
                        self.lb_result['text'] = "                         " + str(num + num_robo) + ' Deu Par'
                    elif par_impar == "impar":
                        self.lb_result['text'] = "                         " + str(num + num_robo) + ' Deu Ímpar'
                    else:
                        self.lb_erro["text"] = "Erro: Escolha par ou ímpar e digite um número até 10."

                        # Pontuações
                    if par_impar == "par" and escolha == "par":
                        self.placar1 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"
                    elif par_impar == "par" and escolha == "impar":
                        self.placar2 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"
                    if par_impar == "impar" and escolha == "impar":
                        self.placar1 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                                           + "     X    " + str(
                            self.placar2) + "      Máquina"

                    elif par_impar == "impar" and escolha == "par":
                        self.placar2 += 1
                        self.lb2['text'] = "                         Jogador/a        " + str(
                            self.placar1) + "     X    " + str(
                            self.placar2) + "      Máquina"

                    # Altera imagem do robo
                    if num_robo == 0:
                        self.lb_img2['image'] = self.img0

                    elif num_robo == 1:
                        self.lb_img2['image'] = self.img1

                    elif num_robo == 2:
                        self.lb_img2['image'] = self.img2

                    elif num_robo == 3:
                        self.lb_img2['image'] = self.img3

                    elif num_robo == 4:
                        self.lb_img2['image'] = self.img4

                    elif num_robo == 5:
                        self.lb_img2['image'] = self.img5

                    elif num_robo == 6:
                        self.lb_img2['image'] = self.img6

                    elif num_robo == 7:
                        self.lb_img2['image'] = self.img7

                    elif num_robo == 8:
                        self.lb_img2['image'] = self.img8

                    elif num_robo == 9:
                        self.lb_img2['image'] = self.img9

                    elif num_robo == 10:
                        self.lb_img2['image'] = self.img10
                    else:
                        self.lb_erro["text"] = "Erro: Escolha um número entre 0 e 10."
            else:
                self.lb_erro["text"] = "Erro: Por favor escolha par ou ímpar."

        except ValueError:
            self.lb_erro["text"] = "Erro: Digite um valor entre 0 e 10."

    def restart(self,event):
        resposta = mbox.askquestion("Reiniciar", "Deseja reiniciar o programa?")
        if resposta == "yes":
            self.lb_erro["text"] = ""
            self.lb_result["text"] = ""
            self.placar1 = 0
            self.placar2 = 0
            self.lb_img1['image'] = self.img_jogador
            self.lb_img2['image'] = self.img_maq
            self.lb2['text'] = "                         Jogador/a        " + str(self.placar1) \
                               + "     X    " + str(
                self.placar2) + "      Máquina"

    def info(self, event):
        info = mbox.showinfo("Informações", "Feito por João Lucas com a ajuda de Jefferson Lobato.\n"
                                            "                                                                      "
                                            "Este software está licenciado sobre a licensa de código aberto GPL 3.0 "
                                            "https://www.gnu.org/licenses/gpl-3.0.en.html")


janela = Janela(raiz)
# Tamanho da janela
raiz.geometry("750x750+300+30")

# raiz.iconbitmap('Aulas/Aula51 ate Aula59/par_impar_shinobi/arq_projeto_shinobi/jogadorr.ico') não funciona no Ubuntu.
# Tente:
icon = PhotoImage(file="arq_projeto_shinobi/jogador.png")
raiz.tk.call('wm', 'iconphoto', raiz._w, icon)
raiz.title("Tux: Par ou Ímpar")
raiz["bg"] = cinza1

raiz.mainloop()
