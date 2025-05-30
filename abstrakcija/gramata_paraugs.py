from abc import ABC, abstractmethod

#vispārīga datu struktūra, kas nepieciešama visām grāmatām

class Gramata(ABC): #abstraktā klase ar metodi gramatas_dati
    @abstractmethod
    def gramatas_dati(self):
        pass

#izveidot 2 apakšklases, kur katra metodi(gramatas_dati) realizē citādāk

class Hobits(Gramata):
    def gramatas_dati(self):
        print("Hobits, 654 lpp")

class DaVinciKods(Gramata):
    def gramatas_dati(self):
        print("Da Vinci koda autors ir Dens Brauns")

gramata1=Hobits()
gramata1.gramatas_dati()

gramata2 = DaVinciKods()
gramata2.gramatas_dati()
