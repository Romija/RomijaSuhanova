#izveidot klasi BankasKonts
#ielikt 2 atribūtus - vārds un atlikums
#klasei ir 2 metodes - iemaksat(summa) - palielinas konta atlikumu par norādīto summu
#iznemt(summa) - samazina konta atlikumu par norādīto summu, ja pietiek līdzekļi
#objekti - klients Laura sākumā ir 100eiro / iemaksā 50, pārbauda atlikumu
#izņem 30, pēc tam mēģina izņemt 200, lai notestētu gadījumu, kad nav līdzekļu

class BankasKonts:
    def __init__(self, vards, atlikums):
        self.vards = vards #uztaisa laukus
        self.atlikums = atlikums

    def iemaksat(self, summa):
        self.atlikums+=summa #palielina atlikumu
        return f"Iemaksāti {summa} eiro. Jaunais atlikums {self.atlikums}"

    def iznemt(self, summa):
        #parbaude vai ir līdzekļi
        if summa >self.atlikums:
            return "Nepietiek līdzekļu"
        self.atlikums-=summa #samazina atlikumu
        return f"Izņemti {summa} eiro. Atlikums: {self.atlikums}"

konts = BankasKonts("Laura",100)

print(konts.iemaksat(50))
print(konts.iznemt(30))
print(konts.iznemt(200))
