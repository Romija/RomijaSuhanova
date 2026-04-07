import math
#Klase nedrīkst prasīt input(), jo klases uzdevums ir loģika, nevis saruna ar lietotāju, kritērijos kā 'slikta struktūra'

#Ievade=progammas galvena dala(lietotaja saskarne)
#Klase=aprēķini

class Kvadratvienadojums:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminants(self): 
        return self.b**2 - 4*self.a*self.c

    def risinat(self):
        if self.a == 0:
            return "Tas nav kvadrātvienādojums."

        D = self.diskriminants()

        if D > 0:
            x1 = (-self.b + math.sqrt(D))/(2*self.a)
            x2 = (-self.b - math.sqrt(D))/(2*self.a)
            return f"x1 = {x1:.2f}, x2 = {x2:.2f}"

        elif D == 0:
            x = -self.b / (2*self.a)
            return f"x = {x:.2f}"

        else:
            return "Sakņu nav."


#lietotāja ievade
a = float(input("Ievadi a: "))
b = float(input("Ievadi b: "))
c = float(input("Ievadi c: "))

#objekts
vienadojums = Kvadratvienadojums(a, b, c)

#rezultāts
print(vienadojums.risinat())
