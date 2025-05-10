from tkinter import *

class Janela:
    def __init__(self, parent, comp, alt, pos_x, pos_y, cor_back, cor_borda,
                 larg_borda = 0, ):

        self.janela = Frame(parent, bg= cor_back, 
                            highlightbackground=cor_borda, highlightthickness=larg_borda) # Criação da janela e configurando borda do frame
    
        self.janela.place(relx= pos_x, rely= pos_y, relheight=alt, relwidth=comp) # Botando janela na raiz