#bankas sistēmas simulācija
class bankasKonts:
    def __init__(self, konta_numurs, ipasnieks, atlikums = 0.0):
        self.konta_numurs = konta_numurs
        self.ipasnieks = ipasnieks
        self.atlikums = atlikums

        self.darijumu_vesture = []

#metode konta info
    def paradit_info(self):
        print("Konta info.:")
        print(f"Konta numurs: {self.konta_numurs}")
        print(f"Īpašnieks: {self.ipasnieks}")
        print(f"Atlikums: {self.atlikums} EUR")

    def iemaksat(self, summa):
        if summa>0:
            self.atlikums+=summa
            self.darijumu_vesture.append(f"Iemaksa: +{summa} EUR")
        else:
            print("Kļūda: summai jābūt lielākais par nulli!")

    def iznemt(self, summa): #pārbaudīt, vai summa nav mazāka par < un atlikumu
        #pievienot darījumu sarakstam
        if 0<summa<=self.atlikums:
            self.atlikums-= summa
            self.darijumu_vesture.append(f"Izņemts: -{summa} EUR")
        print("Kļūda: Kontā nepietiek līdzekļu")

    def parskaitit(self,merka_konts, summa):
        if 0<summa<=self.atlikums:
            self.atlikums-=summa
            merka_konts.iemaksat(summa)
            self.darijumu_vesture.append(f"Pārskaitījums uz kontu {merka_konts.konta_numurs} : {summa}EUR")
        else:
            print("Kļūda: nepietiek līdzekļu")

    def paradit_vesturi(self):
        print("Transakciju vēsture:")
        #pārbaudīt, vai nav tukšs saraksts
        if len(self.darijumu_vesture)==0:
            print("Nav neviena darījuma.")
        else:
            for darijums in self.darijumu_vesture:
                print(darijums)
#------------------------
class Banka:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.konti = {}

    def pievienot_kontu(self, konts):
        #atslēga konta nr ; vērtība pats konta objekts
        #var atrast kontu pēc numura
        self.konti[konts.konta_numurs]=konts

    def nonemt_kontu(self, konta_numurs):
        #pārbauda, vai konts ir vārdnīcā
        if konta_numurs in self.konti:
            del self.konti[konta_numurs]

    def paradit_visus_kontus(self):
        print(f"Banka: {self.nosaukums}")
        for konta_numurs, konts in self.konti.items():
            print(f"Konts: {konta_numurs}")
            konts.paradit_info()
            print()

#izveido banku un kontus
banka = Banka("Banka ABC")
konts1 = bankasKonts("001", "Jānis Bērziņš")
konts2 = bankasKonts("002", "Anna Liepiņa")

banka.pievienot_kontu(konts1)
banka.pievienot_kontu(konts2)



#izvēles izveidne
while True:
    print("\nDarbības")
    print("1. Parādīts konta informāciju: ")
    print("2. Veikt iemaksu: ")
    print("1. Parādīts konta informāciju: ")
    print("3. Veikt izmaksu: ")
    print("4. Veikt pārskaitījumu: ")
    print("5. Parādīt darījumu vēsturi: ")
    print("6. iziet no programmas: ")

    izvele = input("Izvēlies darbību: ")
    if izvele == "1": #parādīs konta nr, ja eksistē
        konta_numurs=input("\nIevadi konta nr: ")
        if konta_numurs in banka.konti:
            banka.konti[konta_numurs].paradit_info()
        else:
            print("Kļūda")

    #jāmēģina iemaksāt kontā konkrēta summa (float)
    #nedrīkst nebūt skaitlis
    elif izvele == "2":
        konta_numurs=input("\nIevadi konta nr: ")
        if konta_numurs in banka.konti:
            try:
                summa = float(input("Ievadi summu iemaksai: "))
                banka.konti[konta_numurs].iemaksat(summa)
            except:
                print("Jāievada skaitlis.")
        else:
            print("KOnta nr. neeksistē.")

    elif izvele == "3": #mēģina izņemt naudu
        konta_numurs=input("\nIevadi konta nr: ")
        if konta_numurs in banka.konti:
            try:
                summa = float(input("Ievadi summu izmaksai: "))
                banka.konti[konta_numurs].iznemt(summa)
            except:
                print("Jāievada skaitlis.")
        else:
            print("KOnta nr. neeksistē.")

    elif izvele == "4": #pārskaita naudu
        no_konta = input("\nIevadi savu konta nr: ")
        uz_kontu = input("\nIevadi saņēmēja konta nr: ")
        try:
            if no_konta in banka.konti and uz_kontu in banka.konti:
                summa = float(input("Ievadi pārskaitīuma summu: "))
                banka.konti[no_konta].parskaitit(banka.konti[uz_kontu],summa)
        except:
                print("Jāievada skaitlis.")
        else:
            print("Konta nr. neeksistē.")

    elif izvele == "5": 
        konta_numurs=input("\nIevadi konta nr: ")
        if konta_numurs in banka.konti:
            banka.konti[konta_numurs].paradit_vesturi()
        else:
            print("Kļūda")
    elif izvele == "6":
        print("Atā")
        break
        
