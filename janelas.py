from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, parent, comp, alt, pos_x, pos_y):

        self.janela = ttk.Frame(parent) # Criação da janela 
    
        self.janela.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando janela na raiz