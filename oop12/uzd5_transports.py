#Filtrēšana pēc metodes rezultāta, nevis pēc klases tipa

class Transportlidzeklis:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
    def atrums(self):
        return 0
#Transportlidzeklis manto no Auto
class Auto(Transportlidzeklis):
    def atrums(self):
        return 90

class Velosipeds(Transportlidzeklis):
    def atrums(self):
        return 25

class Vilciens(Transportlidzeklis):
    def atrums(self):
        return 120


#izveidojam objektus
t1 = Auto("BMW")
t2 = Velosipeds("Kalnu velosipēds")
t3 = Vilciens("Pasažieru vilciens")
t4 = Auto("Audi")
t5 = Velosipeds("Pilsētas velosipēds")

#objekti  sarakstā
transporti = [t1, t2, t3, t4, t5]

print("Transportlīdzekļi, kuru ātrums ir lielāks par 50:")

for transports in transporti:    #Izsauc metodi atrums()/neskatoties, kādas klases objekts tas ir
    if transports.atrums()>50:
        print(f"{transports.nosaukums} -{transports.atrums()} km/h")
