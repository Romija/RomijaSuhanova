class Dzivnieks:
    def __init__(self,vards,skana): #konstruktors
        self.vards = vards
        self.skana = skana

    def izdod_skanu(self):
        return f"{self.vards} saka {self.skana}!"

#objekti
kakis = Dzivnieks("Kaķis","Ņau")
suns=Dzivnieks("Suns","Vau")

print(kakis.izdod_skanu())
print(suns.izdod_skanu())
