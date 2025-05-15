from tkinter import *
from tkextrafont import Font

class Fonte:
    def __init__(self, familia = ("typewriter", "machine", "pixel"), tam_letra = 14):
        if familia == "typewriter":
            self.custom = Font(file = "fontes_letra/jmh_typewriter/JMH Typewriter.ttf",family=familia[0],size=tam_letra)
        elif familia == "machine":
            self.custom = Font(file = "fontes_letra/la_machine_company/La Machine Company.ttf",family=familia[1], size=tam_letra)
        else:
            self.custom = Font(file = "fontes_letra/pixeled/Pixeled.ttf",family=familia[2], size=tam_letra)