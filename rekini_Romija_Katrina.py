#importējam nepieciešamo
import csv
from datetime import datetime

class Rekins: #klases izveide
    def __init__(self, klients, veltijums, izmers, materials): #konstruktora izveide
        self.klients = klients
        self.veltijums=veltijums
        self.izmers = izmers
        self.materials = materials
        #laika iegūšana, ko izmantos rēķinā
        self.laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #izdrukā rēķinu konsolē
    def izdruka(self, klients, veltijums, izmers, materials, laiks, summa):
        print(f"\nRēķins: ")
        print(f"Klients: {klients}")
        print(f"Veltījums: {veltijums}")
        print(f'Izmēri (cm): {izmers}')
        print(f'Materiāla cena (eiro/cm^3): {materials}')
        print(f"Rēķina izveidošanas laiks: {laiks}")
        print(f"Apmaksas summa: {summa}") 

    #funkcija apreiķinās kastītes summu, balstoties uz ievadītajiem parametriem
    def aprekins(izmers, materials, veltijums): 
        darba_samaksa = 15
        PVN = 21
        veltijums_simbolos = len(veltijums) #nosaka simbolu skaitu veltījumā 

        platums, garums, augstums = izmers.rstrip().split(",") #noņem atstarpes un pārveido par listu
        produkta_cena = (veltijums_simbolos) * 1.2 + (platums / 100 * garums / 100 * augstums / 100) / 3 * materials
        PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        return rekina_summa

#lietotāja ievades dati
print("Katrīna teica sveiki!\n")
vards = input('Klienta vārds: ')
veltijums = input('Veltījums: ')
izmers = input('Izmēri kastītes (3 vesali skaitļi atdalīti ar atsarpēm) (cm): ')
materialaCena = float(input('Materiāla cena (eiro/cm^3): '))

#objekta izveide
klients1 = Rekins(vards, veltijums, izmers, materialaCena)
#izsauc atbilstošās metodes
summa = klients1.aprekins(izmers, materialaCena,veltijums)
klients1.izdruka(vards, veltijums, izmers, materialaCena, summa)


    