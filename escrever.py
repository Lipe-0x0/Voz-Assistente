
class Escrever:
    def __init__(self):
        
        self.key = ""


    def alterar(self):
        self.arquivo = open("frase.txt","w",encoding="utf8")

        self.arquivo.write(input())