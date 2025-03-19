from abc import ABC , abstractmethod

class SkolasDarbinieks(ABC):
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards

    @abstractmethod
    def apraksts(self): #abstrakta metode
        pass

class Skolotajs(SkolasDarbinieks):
    def __init__(self, vards, uzvards, prieksmets):
        super().__init__(vards, uzvards)
        self.prieksmets = prieksmets

    def apraksts(self):
        print(f"Skolotājs {self.vards} {self.uzvards} māca {self.prieksmets}.")

class Pavars(SkolasDarbinieks):
    def __init__(self, vards, uzvards,pusdienas):
        super().__init__(vards, uzvards)
        self.pusdienas = pusdienas

    def apraksts(self):
        print(f"Pavārs {self.vards} {self.uzvards} gatavo {self.pusdienas}.")

class Apkopejs(SkolasDarbinieks):
    def __init__(self, vards, uzvards, telpa):
        super().__init__(vards, uzvards)
        self.telpa = telpa

    def apraksts(self):
        print(f"Apkopējs {self.vards} {self.uzvards} tīra {self.telpa}.")

darbinieki = [Skolotajs("Uldis", "Vanags", "Mūzika"), Pavars("Rudzīte", "Puķe", "kartupeļi"), Apkopejs("Nīca", "Ziliņa", "pagrabs")]

faila_nosaukums = "Darbinieki.txt"
with open(faila_nosaukums,"w",encoding='utf8') as fails:
    for i in darbinieki:
        cilveks = i.apraksts()
        print(cilveks)
        print("----------------------")
        fails.write(cilveks)