#dažādiem produktiem ir atšķirīga gala cenas aprēķināšana

#bāzes klase Produkts
class Produkts:
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena
    def galiga_cena(self):    #metode gala cenas aprēķinam
        return self.cena 


#klase Elektronika manto no Produkts
class Elektronika(Produkts):    
    def galiga_cena(self):
        return self.cena * 1.21 #šai klasei gala cena būs ar 21% PVN
    
#klase Apgerbs manto no Produkts
class Apgerbs(Produkts):
    def galiga_cena(self):
        return self.cena * 0.90 #Šai klasei piemērojam 10% atlaidi

#klase Partika manto no Produkts
class Partika(Produkts):
    #Šajā piemērā pārtikai atstājam sākotnējo cenu
    def galiga_cena(self):
        return self.cena


#objekti kā dažādi produktti
p1 = Elektronika("Telefons", 500)
p2 = Elektronika("Austiņas", 80)
p3 = Apgerbs("Jaka", 60)
p4 = Apgerbs("Sporta krekls", 25)
p5 = Partika("Maize", 1.50)
p6 = Partika("Piens", 1.20)

#visus produktus vienā sarakstā
grozs = [p1, p2, p3, p4, p5, p6]

kopeja_summa = 0

for produkts in grozs:
    gala_cena = produkts.galiga_cena()    #aprēķinām viena produkta gala cenu

    print(f"{produkts.nosaukums}: {gala_cena:.2f} EUR")
    kopeja_summa += gala_cena

print(f"kopējā groza cena: {kopeja_summa:.2f} EUR")
