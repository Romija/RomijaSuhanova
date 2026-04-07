class Persona:
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards
    def info(self):
        return f"Vārds: {self.vards}, Uzvārds: {self.uzvards}."

class Darbinieks(Persona):
    def __init__(self, vards, uzvards, alga):
        super().__init__(vards, uzvards)
        self.alga = alga #tikai pie klases darbinieks
    
    #pārrakstām info(), paņemot tekstu no bāzes klases
    #pievienojot darbinieka algu
    def info(self):
        pamata_info = super().info()
        return f"{pamata_info}, Alga: {self.alga} EUR"

#objektu izveide
darbinieks1 = Darbinieks("Anna","Bērza",2200)
print(darbinieks1.info())
       