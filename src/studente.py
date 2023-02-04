from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class student:
    materia: str
    #self.genere = genere
    #self.eta = eta
    anno: str
    lezioni:str
    #self.go = go
    info: str
    numero: str
    walink: str