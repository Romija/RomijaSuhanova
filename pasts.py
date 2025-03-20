#Abstrakta klase Persona
from abc import ABC,abstractmethod
class Persona(ABC):
    def __init__(self, vards, epasts):
        self.vards = vards
        self.epasts = epasts


class Vestule:
    def __init__(self, no_persona, uz_persona, saturs):
        self.no_persona = no_persona
        self.uz_persona = uz_persona
        self.saturs = saturs

class VestulesSuta(ABC):
    @abstractmethod
    def sutit_vestuli(self, vestule):
        pass

    def sanemt_vestuli(self, vestule):
        pass

#Klase, kas īsteno VēstuļuSujeta abstraktu klasi
class Pastnieks(VestulesSuta):
    def sutit_vestuli(self, vestule):
        print('💌')
        print(f"Vēstule no: {vestule.no_persona.vards} <{vestule.no_persona.epasts}>")
        print(f"Vēstule uz: {vestule.uz_persona.vards} <{vestule.uz_persona.epasts}>")
        print(f"Saturs: {vestule.saturs}")
        print("Vēstule nosūtīta ar pastnieka palīdzību.")

    def sanemt_vestuli(self, vestule):
        print(f"Vēstule saņemta no: {vestule.no_persona.vards} <{vestule.no_persona.epasts}>")
        print(f"Vēstule adresēta uz: {vestule.uz_persona.vards} <{vestule.uz_persona.epasts}>")
        print(f"Saturs: {vestule.saturs}")
        print('💌')


persona1 = Persona("Jānis Zibens", "zibens.sper@svg.lv")
persona2 = Persona("Zane Puķe", "pukes.zied@svg.lv")
vestule = Vestule(persona1, persona2, "Sveiki, vai šodien esat darbā?")

pastnieks = Pastnieks()
pastnieks.sutit_vestuli(vestule)

print()


pastnieks.sanemt_vestuli(vestule)