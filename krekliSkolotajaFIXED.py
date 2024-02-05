try:
    skaitsA = int(input("Kreklus skaits: "))
    apdrukaA = int(input("Apdruka \n1.Teksts (5 EUR)\n2.Zīme (7 EUR),\n3.Foto (20EUR): "))
    piegadeA = input('Ar piegadi? (ja/ne): ')
except ValueError:
    print("Jāievada skaitlis!")
    exit()

if piegadeA not in ["ja","ne"] or apdrukaA not in [1, 2, 3] or skaitsA<0: #pārbauda ievadi
    print("Jāievada pareizi dati!")
    exit()
    
if piegadeA == 'ja':
    piegadeA = True
else:
    piegadeA = False
    
def pasutiKreklus(skaits, apdruka, piegade):
    krekli= skaits*[5, 7, 20] [apdruka-1] #apreiķina cenu bez atlaides
    #apreiķina piegādes maksu
    if krekli>=50 and piegadeA == True: 
        piegade=0
    elif krekli<50 and piegadeA == True: 
        piegade=0
    else:
        piegade = 'Nav'
        
    #apreiķina atlaidi
    if krekli>100:
        atlaide = round(krekli*0.05, 2)
    else:
        atlaide=0
        
    kopsumma=krekli-atlaide
    
    if type(piegade) != str:
        kopsumma=kopsumma+piegade
    
    if type(piegade) == int:
        piegade=str(float(piegade))+'EUR'
    return [krekli, piegade, atlaide, kopsumma]
        

rez = pasutiKreklus(skaitsA, apdrukaA, piegadeA)
print('----IZMAKSAS----')
print('Kopējā cena-', rez[3],'EUR\n', 'Krekli- ', float(rez[0]), 'EUR\n', 'piegāde - ', rez[1], '\n', 'Atlaide', rez[2], 'EUR')

