import csv
from datetime import datetime

class Rekins: #self neiet pie parametriem
    def __init__(self, klients, veltijums, izmers, materials):
        self.klients = klients #taisam laukus
        self.veltijums=veltijums
        self.izmers = izmers
        self.materials = materials
        self.laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.darba_samaksa = 15
        self.PVN = 21
        self.summa = self.aprekins() #aprēķinās pēc objekta izveodošanas, pamatojoties uz citiem parametriem

    def aprekins(self): #self atsaucas uz pašreizējo objektu, tātad uz visiem atribūtiem, kas tam objektam pieejami
        #izpakot izmērus
        platums, garums, augstums = self.izmers
        veltijuma_garums = len(self.veltijums)
        produkta_cena = (veltijuma_garums*1.20) + (platums/100) * (garums/100) * (augstums/100)/3 * self.materials
        PVN_summa = (produkta_cena + self.darba_samaksa) * self.PVN / 100
        rekina_summa = (produkta_cena + self.darba_samaksa) + PVN_summa
        return round(rekina_summa, 2)

    def izdruka(self):
        print(f"\nRēķins: ")
        print(f"Rēķina izveidošanas laiks: {self.laiks}")
        print(f"Klients: {self.klients}")
        print(f"Veltījums: {self.veltijums}")
        print(f'Izmēri (cm): platums={self.izmers[0]}, garums = {self.izmers[1]}, augstums = {self.izmers[2]}')
        print(f'Materiāla cena (eiro/cm^3): {self.materials}')
        print(f"Darba samaksa: {self.darba_samaksa}")
        print(f"PVN: {self.PVN}")
        print(f"Apmaksas summa: {self.summa}")

    def saglabat(self):
        datnes_nosaukums = f"rekins_{self.klients}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(datnes_nosaukums, 'w',newline='',encoding='utf8') as fails:
            rakstitajs = csv.writer(fails)
            rakstitajs.writerow(["Izveidošanas laiks", "Klients","Veltījums","Izmērs", "Cena (Euro/m^2)","Darba samaksa","PVN(%)","Summa (euro)"])
            rakstitajs.writerow([self.laiks, self.klients, self.veltijums, 
                                f"{self.izmers[0]} x {self.izmers[1]} x {self.izmers[2]}",
                                self.materials, self.darba_samaksa, self.PVN, self.summa])
            print(f"Rēķins saglabāts failā: {datnes_nosaukums}")

klients = input('Klienta vārds: ')
veltijums = input('Veltījums: ')
platums = int(input('Platums: '))
garums = int(input('Garums: '))
augstums = int(input('Augstums: '))
materials = float(input('Materiāla cena (eiro/cm^3): '))

#jaunā rēķina objekta izveidošana
#jāizveido 1 objekts
rekins = Rekins(klients,veltijums,[platums,garums,augstums],materials)

#saglabāt un izdrukāt rēķinu

rekins.saglabat()
rekins.izdruka()
#aprekins jau pie izdrukas izsaukts