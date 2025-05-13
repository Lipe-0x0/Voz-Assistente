from tkinter import *
from PIL import Image

class Botao:
    def __init__(self, parent, text, comp, alt, pos_x, pos_y, funcao = None,
                 fonte = "times new roman", tam_font = 13, cor_letra = "black", cor_fundo = "white"):
        
        self.botao = Button(parent, text=text, command=funcao,
                            font=(fonte, tam_font), fg=cor_letra, bg=cor_fundo) # Criando botao

        self.botao.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando botao no frame

    def por_imagem(self, file, posicao):
        self.image = Image.open(file)

        self.imagem = PhotoImage(self.image).subsample(3,3) # Carregando imagem e redimensionando ela

        self.botao.configure(image= self.imagem, compound=posicao )