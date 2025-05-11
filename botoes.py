from tkinter import *

class Botao:
    def __init__(self, parent, text, comp, alt, pos_x, pos_y, image = None, posicao_text = None, funcao = None):
        
        self.botao = Button(parent, text=text, image=image, compound=posicao_text, command=funcao) # Criando botao

        self.botao.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando botao no frame