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
janela1 = Janela(t.raiz, comp=0.07, alt=0.61, pos_y=0.5, pos_x=0.5)
janela2 = Janela(t.raiz, comp=0.07, alt=0.61, pos_y=0.7, pos_x=0)

t.iniciar()