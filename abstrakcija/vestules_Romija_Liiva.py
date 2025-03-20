
from abc import ABC , abstractclassmethod

#@abstractclassmethod
class Persona(ABC):
    def __init__(self, vards, epasts):
        self.vards = vards
        self.epasts = epasts

class Vestule():
    def __init__(self, sanemejs, sutitajs, saturs):
        self.sanemejs = sanemejs
        self.sutitajs = sutitajs
        self.saturs = saturs

#@abstractclassmethod
class VestuleSuta(Vestule):
    def __init__(self, sanemejs, sutitajs, saturs):
        super().__init__(sanemejs, sutitajs, saturs)
    
    def sutit_vestuli(self):
        pass

    def sanemt_vestuli(self):
        pass

class Pastnieks(VestuleSuta):

    def sanemt_vestuli(self):
        print("Vēstule no: ", self.sutitajs)
        print('Vēstule uz: ', self.sanemejs)
        print('Saturs: ', self.saturs)

    def sanemt_vestuli(self):
        print("Vēstule saņemta no: ", self.sutitajs)
        print('Vēstule adresēta: ', self.sanemejs)
        print('Saturs: ', self.saturs)

#objektu izveide
pirmais = Persona('Pipars Kaķis', 'pipars.kakis@svg.lv')
otrais = Persona('Lora Suns', 'lora.suns@svg.lv')
vestule = Pastnieks(pirmais, otrais , 'Gribi desu?')

vestule.sanemt_vestuli()
vestule.sutit_vestuli()
