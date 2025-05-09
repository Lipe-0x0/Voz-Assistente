from tkinter import *
from tkinter import ttk

class Interface:
    def __init__(self, titulo):
        self.raiz = Tk()
        self.raiz.title(titulo)

    def botao(self):
        pass

    def telas(self, tamanho):
        self.janela = ttk.Frame(self.raiz, padding=tamanho)
        self.janela.grid()
    
    def iniciar(self):
        self.raiz.mainloop()

t = Interface(titulo="teste")
t.telas(tamanho="3 3 12 12")
t.iniciar()