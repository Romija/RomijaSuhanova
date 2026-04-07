#uzdevums: dažādām aktivitātēm ir atšķirīgs kaloriju aprēķins

class Aktivitate:
    def __init__(self, ilgums):    #konstruktors saglabā ilgumu minūtēs
        self.ilgums = ilgums

    def kalorijas(self):#vispārīga metode kaloriju aprēķinam
        return 0


class Skriesana(Aktivitate):
    def __init__(self, ilgums):
        super().__init__(ilgums)
        self.nosaukums = "Skriešana"

    def kalorijas(self):
        return self.ilgums * 10   #10 kalorijas minūtē(pieņemsim)


class Ritenbrauksana(Aktivitate):
    def __init__(self, ilgums):
        super().__init__(ilgums)
        self.nosaukums = "Riteņbraukšana"

    def kalorijas(self):
        return self.ilgums * 8   #8 kalorijas minūtē


class Peldesana(Aktivitate):
    def __init__(self, ilgums):
        super().__init__(ilgums)
        self.nosaukums = "Peldēšana"

    def kalorijas(self):
        return self.ilgums * 11   #11 kalorijas minūtē


#izveido objektus
a1 = Skriesana(30)
a2 = Ritenbrauksana(45)
a3 = Peldesana(20)
a4 = Skriesana(15)

#saraksts ar aktivitātēm
aktivitates = [a1, a2, a3, a4]

#kopējais kaloriju skaits
kopejas_kalorijas = 0

#cikls cauri aktivitātēm
for aktivitate in aktivitates:
    kaloriju_skaits = aktivitate.kalorijas()
    
    #izdrukā nosaukumu un kalorijas
    print(f"{aktivitate.nosaukums}: {kaloriju_skaits} kalorijas")

    kopejas_kalorijas += kaloriju_skaits

print(f"Kopā sadedzinātas kalorijas: {kopejas_kalorijas}")