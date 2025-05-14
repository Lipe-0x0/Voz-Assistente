from tkinter import *

class Entrada:
    def __init__(self, parent, comp, alt, pos_x, pos_y, var_string):  
        self.entrada = Entry(parent, font=("arial"), textvariable=var_string)

        self.entrada.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando janela na raiz