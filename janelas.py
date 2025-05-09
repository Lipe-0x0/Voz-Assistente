from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, parent, comp, alt, preenchimento = None):

        self.janela = ttk.Frame(parent, width=comp, height=alt, border=50) # Criação da janela 
        
        if preenchimento != None:
            self.janela.grid(ipadx=preenchimento[0], ipady=preenchimento[1],
                          padx=preenchimento[2], pady=preenchimento[3]) # Mostrar na tela e configurar posição