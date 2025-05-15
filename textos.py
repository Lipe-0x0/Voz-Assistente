from tkinter import *

class Texto:
    def __init__(self, parent, comp, alt, pos_x, pos_y, fonte):  

        self.frase = Text(parent, wrap="word", font=fonte)

        self.frase.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando janela na raiz