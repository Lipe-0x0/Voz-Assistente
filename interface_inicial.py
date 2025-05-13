from tkinter import *
from janelas import Janela
from botoes import Botao
from entradas import Entrada

class Interface:
    def __init__(self, titulo,  col_image, tamanho_pag = None):
        self.raiz = Tk()
        self.raiz.title(titulo) # Título
        self.raiz.geometry(tamanho_pag) # Tamanho da página
        self.raiz.configure(background=col_image) # Inserindo cor/imagem de fundo
        self.raiz.iconbitmap("icones/mensagem-de-voz.ico") # Ícone

    def botao(self):
        self.opcao = Botao(self.janela2.janela, text="OPÇÃO", comp=0.2,alt=0.50, pos_x=0.10, pos_y= 0.3, fonte="Courier New",
                           tam_font=14).por_imagem("icones/opcao (1).png", posicao=LEFT) # Botão de Opção

        self.info = Botao(self.janela2.janela, text="INFO", comp=0.2,alt=0.50, pos_x=0.35, pos_y= 0.3, fonte="Courier New",
                           tam_font=14).por_imagem("icones/em-formacao.png", posicao=LEFT) # Botão de informação

    def frame(self):
        self.janela1 = Janela(self.raiz, comp=0.90, alt=0.70, pos_x=0.05, pos_y=0.14, 
                 cor_fundo="#231d1e", cor_borda="#ff8207", larg_borda=10) # Frame onde escreve o texto

        self.janela2 = Janela(self.raiz, comp=1, alt=0.10, pos_x=0, pos_y=0, 
                 cor_fundo="#231d1e") # Frame onde mostra os botões
    
    
    def iniciar(self):
        self.frame()
        self.botao()
        self.raiz.mainloop()




t = Interface(titulo="Assistente de Voz",col_image="#fcfcfc",tamanho_pag="500x650")

t.iniciar()