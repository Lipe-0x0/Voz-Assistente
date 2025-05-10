from tkinter import *
from janelas import Janela

class Interface:
    def __init__(self, titulo,  col_image, tamanho_pag = None):
        self.raiz = Tk()
        self.raiz.title(titulo) # Título
        self.raiz.geometry(tamanho_pag) # Tamanho da página
        self.raiz.configure(background=col_image)
    def botao(self):
        pass
    
    def iniciar(self):
        self.raiz.mainloop()

t = Interface(titulo="teste",col_image="blue",tamanho_pag="500x650")
janela1 = Janela(t.raiz, comp=0.90, alt=0.70, pos_x=0.05, pos_y=0.14, 
                 cor_back="red", cor_borda="black", larg_borda=10)

janela2 = Janela(t.raiz, comp=1, alt=0.10, pos_x=0, pos_y=0, 
                 cor_back="green", cor_borda="black", larg_borda=5)

t.iniciar()