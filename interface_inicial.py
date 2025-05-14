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
        self.opcao = Botao(self.janela2.janela, text="OPÇÃO", comp=0.2,alt=0.50, pos_x=0.10, pos_y= 0.3) # Botão de Opção
        self.opcao.mudar_atrib(tam_borda=6, cor_fundo="#231d1e", cor_letra="white") # Mudando configs do botao
        self.opcao.por_imagem("icones/opcao.png", posicao=LEFT)

        self.info = Botao(self.janela2.janela, text="INFO", comp=0.2,alt=0.50, pos_x=0.35, pos_y= 0.3) # Botão de informação
        self.info.mudar_atrib(tam_borda=6, cor_fundo="#231d1e", cor_letra="white") # Mudando configs do botao
        self.info.por_imagem("icones/simbolo-de-informacao.png", posicao=LEFT)

    def frame(self):
        self.janela1 = Janela(self.raiz, comp=0.90, alt=0.70, pos_x=0.05, pos_y=0.14, 
                 cor_fundo="#231d1e", cor_borda="#ff8207", larg_borda=10) # Frame onde escreve o texto

        self.janela2 = Janela(self.raiz, comp=1, alt=0.10, pos_x=0, pos_y=0, 
                 cor_fundo="#231d1e") # Frame onde mostra os botões
        
    def entrada(self):
        self.frase = StringVar()

        self.entrada1 = Entrada(self.janela1.janela, comp=1, alt=1, pos_x=0, pos_y=0, var_string=self.frase)

        frase = self.frase.get()
    
    
    def iniciar(self):
        self.frame()
        self.botao()
        self.entrada()
        self.raiz.mainloop()




t = Interface(titulo="Assistente de Voz",col_image="#fcfcfc",tamanho_pag="500x650")

t.iniciar()