from escrever import Escrever
import gtts
from playsound import playsound
import random
import  os


class Psy:
    def __init__(self):

        self.escrita = Escrever()

        self.lista_audios = []

    def play(self):

        while True:
            self.escrita.alterar()
             
            with open("frase.txt","r",encoding="utf8") as arquivo:
                for linha in arquivo:

                    frase=gtts.gTTS(linha,lang="pt-BR",slow=False)
                    
                    # ALTERAÇÃO NO NOME DO ARQUIVO (CONSEQUENTEMENTE CRIANDO OUTROS ARQUIVOS) PARA CADA FRASE
                    filename = random.randrange(-500,50060)

                    # EVITAR ACÚMULO DE ARQUIVOS MP3 NA PASTA
                    self.lista_audios.append(filename)
                    if len(self.lista_audios)>=2:
                        os.remove("Voz-Assistente/sons/"+str(self.lista_audios[0])+".mp3") 
                        del self.lista_audios[0]
                    
                    frase.save("Voz-Assistente/sons/"+str(filename)+".mp3")
                    playsound("Voz-Assistente/sons/"+str(filename)+".mp3")

Psy().play()