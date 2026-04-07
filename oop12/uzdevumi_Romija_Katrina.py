print("3.uzdevums -----------------------------------------")
class Printeris: #klases Printeris izveidne
    def __init__(self, teksts):
        self.teksts = teksts
    def darbiba(self): #metode parāda tekstu
        print(f"Printeris izprintē: {self.teksts}")

class Skeneris: #klases Skeneris izveidne
    def __init__(self, teksts):
        self.teksts = teksts
    def darbiba(self): #metode parāda tekstu
        print(f"Skeneris noskenē: {self.teksts}")

class Kamera: #klases Kamera izveidne
    def __init__(self, teksts):
        self.teksts = teksts
    def darbiba(self): #metode parāda tekstu
        print(f"Kamera nofotografē: {self.teksts}")

#objektu izveide
printeris1 = Printeris("Epson")
skeneris2 = Skeneris("Canon")
kamera3 = Kamera("Sony")

saraksts = [printeris1, skeneris2, kamera3]
def izpildi_darbibu(saraksts):
    for obj in saraksts:
        obj.darbiba()

izpildi_darbibu(saraksts)

print("\n4.uzdevums -----------------------------------------")
class Produkts: #bāzes klase
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena
    def galiga_cena(self):
        return f"Produkta cena: {self.cena} EUR"

class Elektronika(Produkts): #atvasinājuma klase
    def __init__(self, nosaukums, cena, PVN):
        super().__init__(nosaukums, cena)
        self.PVN = PVN
    def galiga_cena(self):
        return f"Elektronikas cena: {self.cena*(100/self.PVN)} EUR"

class Apgerbs(Produkts): #atvasinājuma klase
    def __init__(self, nosaukums, cena, atlaide):
        super().__init__(nosaukums, cena)
        self.atlaide = atlaide
    def galiga_cena(self):
        return f"Apģērbs cena: {self.cena-((self.atlaide/self.cena)*100)} EUR"

class Partika(Produkts): #atvasinājuma klase
    def __init__(self, nosaukums, cena):
        super().__init__(nosaukums, cena)
    def galiga_cena(self):
        return f"Pārtikas cena: {self.cena} EUR"

#objektu izveide
prod1 = Produkts("Nazis", 4)
prod2 = Elektronika("Kamera", 100, 21)
prod3 = Apgerbs("Kleita", 100, 10)
prod4 = Partika("Piens", 1.80)
prod5 = Elektronika("Monitors", 1000, 12)
prod6 = Partika("Siers", 3)

saraksts2 = [prod1, prod2, prod3, prod4, prod5, prod6]

kopsumma = 0

for i in saraksts2:
    gala_cena=i.galiga_cena()
    print(gala_cena)
    print(f"{i.nosaukums}:{gala_cena}")

    '''kopsumma+=gala_cena
print(kopsumma)'''

print("\n5.uzdevums -----------------------------------------")
class Transportlidzeklis: #bāzes klase
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def atrums(self):
        speed = 2
        print(f"{self.nosaukums} transportlīdzeklis brauc ar ātrumu {speed}km/h")
        return speed

class Auto(Transportlidzeklis): #atvasinājuma klase
    def __init__(self, nosaukums):
        super().__init__(nosaukums)

    def atrums(self):
        speed = 100
        print(f"{self.nosaukums} auto brauc ar ātrumu {speed}km/h")
        return speed

class Velosipeds(Transportlidzeklis): #atvasinājuma klase
    def __init__(self, nosaukums):
        super().__init__(nosaukums)

    def atrums(self):
        speed = 30
        print(f"{self.nosaukums} velosipeds brauc ar ātrumu {speed}km/h")
        return speed

class Vilciens(Transportlidzeklis): #atvasinājuma klase
    def __init__(self, nosaukums):
        super().__init__(nosaukums)

    def atrums(self):
        speed = 120
        print(f"{self.nosaukums} vilciens brauc ar ātrumu {speed}km/h")
        return speed

#objektu izveide
trans1 = Auto("Peugeon")
trans2 = Vilciens("Vivi")
trans3 = Velosipeds("Trek")
trans4 = Transportlidzeklis("Skrituļslidas")
trans5 = Transportlidzeklis("Slēpes")

saraksts3 = [trans1, trans2, trans3, trans4, trans5]
atrie = [] #transportlīdzekļi kuru ātrums ir lielāks par 50

for i in saraksts3:
    x = i.atrums()
    if x > 50:
        atrie.append(x)

    print('Ātrie transportlīdzekļi: ', atrie)
    
print("\n6.uzdevums -----------------------------------------")
class Aktivitate: #bāzes klase
    def __init__(self, ilgums):
        self.ilgums = ilgums

    def kalorijas(self):
        daudzums = 100
        print(f"Aktivitāte tika darīta {self.ilgums} h => tika patērētas {self.ilgums*daudzums}") #print funkcijā, jo atgriezīs kopējo kaloriju daudzumu, ko vēlāk skaitīs kopā
        return self.ilgums*daudzums #atgriež kopējās kalorijas nodedzinātas šajā aktivitātē

class Skriesana(Aktivitate):#atvasinājuma klase
    def __init__(self, ilgums):
        super().__init__(ilgums)

    def kalorijas(self):
        daudzums = 200
        print(f"Skriešana tika darīta {self.ilgums} h => tika patērētas {self.ilgums*daudzums}")#print funkcijā, jo atgriezīs kopējo kaloriju daudzumu, ko vēlāk skaitīs kopā
        return self.ilgums*daudzums #atgriež kopējās kalorijas nodedzinātas šajā aktivitātē

class Ritenbrauksana(Aktivitate): #atvasinājuma klase
    def __init__(self, ilgums):
        super().__init__(ilgums)

    def kalorijas(self):
        daudzums = 300
        print(f"Riteņbraukšana tika darīta {self.ilgums} h => tika patērētas {self.ilgums*daudzums}")#print funkcijā, jo atgriezīs kopējo kaloriju daudzumu, ko vēlāk skaitīs kopā
        return self.ilgums*daudzums #atgriež kopējās kalorijas nodedzinātas šajā aktivitātē

class Peldesana(Aktivitate): #atvasinājuma klase
    def __init__(self, ilgums):
        super().__init__(ilgums)

    def kalorijas(self):
        daudzums = 800
        print(f"Aktivitāte tika darīta {self.ilgums} h => tika patērētas {self.ilgums*daudzums}")#print funkcijā, jo atgriezīs kopējo kaloriju daudzumu, ko vēlāk skaitīs kopā
        return self.ilgums*daudzums #atgriež kopējās kalorijas nodedzinātas šajā aktivitātē

#objektu izveide
akt1 = Aktivitate(2)
akt2 = Skriesana(4)
akt3 = Ritenbrauksana(6)
akt4 = Peldesana(1)

saraksts4 = [akt1, akt2, akt3, akt4]
kopa_kalorijas = 0

for i in saraksts4:
    kopa_kalorijas += i.kalorijas() #pieskaita, lai iegūtu kopējo kaloriju skaitu

print(f"Kopā patērētas kalorijas: {kopa_kalorijas}")

