class student:

    def __init__(self, materia="", anno="", lezioni="", info="", numero="", walink=""):
        self.materia = materia
        #self.genere = genere
        #self.eta = eta
        self.anno = anno
        self.lezioni = lezioni
        #self.go = go
        self.info = info
        self.numero = numero
        self.walink = walink

    def __str__(self):
        return f"{self.materia} ### {self.info}"