class Skolotajs: #klase
    def __init__(self, vards, prieksmets): #konstruktors
        self.vards = vards #lauki=atribūti=iekšējie mainīgie
        self.prieksmets = prieksmets

    #metode
    def iepazistinatArSevi(self):
        print(f"Sveiki, mani sauc {self.vards}")

    def izliktVertejumu(self, punkti):
        if punkti > 5:
            return f"Prieksmets {self.prieksmets} ir nokārtots."
        else:
            return f"Prieksmets {self.prieksmets} nav nokārtots."

#objekti = instance / objekta izveidošana ir instancēšana
#objektam ir uzvedība
rinalds = Skolotajs("Rinalds","Ģeogrāfija")
sandra = Skolotajs("Sandra","Matemātika")

rinalds.iepazistinatArSevi() #atgriež tekstu un izsauc metodi objektam
print(rinalds.izliktVertejumu(10)) #tā atzīme, ko ieguva

sandra.iepazistinatArSevi()
print(sandra.izliktVertejumu(3))
