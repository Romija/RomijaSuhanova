
#Uzdevums: viena funkcija spēj strādāt ar dažādiem objektiem, ja tiem visiem ir metode darbiba()

class Printeris:
    def darbiba(self):
        print("Printeris drukā dokumentu.")

class Skeneris:
    def darbiba(self): #taa pati metode, bet atgriez citu tesktu
        print("Skeneris skenē attēlu.")

class Kamera:
    def darbiba(self):
        print("Kamera fotografē objektu.")


#funkcija, kas saņem jebkuru objektu
def izpildi_darbibu(obj):
    obj.darbiba() #Funkcija izsauc objekta metodi darbiba()

#katrai klasei savs objekts un txt drukas atkariba no ta, kurai klasei objets izveidots
ierice1 = Printeris()
ierice2 = Skeneris()
ierice3 = Kamera()

#katru objektu padodam vienai un tai pašai funkcijai
izpildi_darbibu(ierice1)
izpildi_darbibu(ierice2)
izpildi_darbibu(ierice3)