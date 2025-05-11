from tkinter import *

class Entrada:
    def __init__(self, parent, comp, alt, pos_x, pos_y):  
        self.entrada = Entry(parent)

        self.entrada.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando janela na raiz