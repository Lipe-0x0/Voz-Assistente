from tkinter import *
from PIL import Image, ImageTk

class Botao:
    def __init__(self, parent, text, comp, alt, pos_x, pos_y, cor_letra = "black", 
                 cor_fundo = "white", tam_borda = 0, funcao = None):
        
        self.botao = Button(parent, text=text, command=funcao, fg = cor_letra, bg = cor_fundo, bd = tam_borda) # Criando botao

        self.botao.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando botao no frame

    def por_imagem(self, file, posicao):
        image = Image.open(file)

        image = image.resize((18,18))

        self.imagem = ImageTk.PhotoImage(image) # Carregando imagem e redimensionando ela

        self.botao.configure(image=self.imagem, compound=posicao)

    def mudar_atrib(self, fonte,cor_letra = "black", 
                 cor_fundo = "white", tam_borda = 0):

        self.botao.configure(font=fonte, fg = cor_letra, bg=cor_fundo, bd=tam_borda)