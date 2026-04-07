#saprast, kā dažādi objekti var izmentot vienu un to pašu metodi
#izveidot 3 klases: PDFdok, WordDoc, Exceldok
#katrai klasei būs konstruktors ar vienu parametru: nosaukums
#metode atvērt(): katrai klasei parāda citu tekstu
#izveido 3 objektus, ielikt tos sarakstā, ar ciklu izsaukt atvert()

class PDFDokuments:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def atvert(self):
        print(f"PDF dokuments '{self.nosaukums}' tiek atvērts pārlūkā.")

class WordDokuments:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def atvert(self):
        print(f"Word dokuments '{self.nosaukums}' tiek atvērts Word pārlūkā.")

class ExcelDokuments:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def atvert(self):
        print(f"Excel dokuments '{self.nosaukums}' tiek atvērts Excel pārlūkā.")

#izveidot 3 objektus
dok1 = PDFDokuments("atskaite.pdf")
dok2 = WordDokuments("domraksts.docx")
dok3 = ExcelDokuments("dati.xlsx")

#objektus ieliek sarakstā
dokumenti = [dok1, dok2, dok3]

for i in dokumenti:
    i.atvert()