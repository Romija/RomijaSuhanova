#definēt klasi Printeris ar vienu metodi drukat(), kas izdruka tekstu
class Printeris:
    def drukat(self, teksts):
        print(teksts)

#objektu izveide
printeris = Printeris()
printeris.drukat("Kā ieeet?")



#definē klasi suns ar vienu īpašību (piemēram, vārds). Klasei izveido 2 objektus
class Suns:
    def __init__(self, vards):
        self.vards = vards

suns1 = Suns("Maksis")
print("1.suņa vārds: ", suns1.vards)
suns2 = Suns("Reksis")
print("2.suņa vārds: ", suns2.vards)



#definēt klasi grāmata, jabut 3 laukiem (jebko, piem, autors, lpp, zanrs), metode info() - izdruka info par grāmatu. Izveidot 2 objektus
class Gramata:
    def __init__(self, autors, zanrs, lpp):
        self.autors = autors
        self.zanrs = zanrs
        self.lpp = lpp
    
    def info(self):
        print(f"Autors, žanrs, lpp skaits: {self.autors},{self.zanrs},{self.lpp}")

gramata1 = Gramata("Nāve uz Nīlas", "Agata Kristi",345)
gramata2 = Gramata("Būris", "Alberts Bels",240)

gramata1.info()
gramata2.info()
