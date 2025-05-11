from tkinter import *

class Botao:
    def __init__(self, parent, text, comp, alt, pos_x, pos_y):
        
        self.botao = Button(parent, text=text) # Criando botao

        self.botao.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando botao no frame