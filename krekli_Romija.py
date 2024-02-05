cena = 0
piegades_maksa=0
def pasuti_tkreklus(skaits, apdruka, piegade):
    if apdruka == 'TEKSTS':
        print('Cena: 5Eiro')
        cena=+5
    elif apdruka == 'ZIME':
        print('Cena: 7Eiro')
        cena=+7
    elif apdruka == 'FOTO':
        print('Cena: 20Eiro')
        cena=+20

    if piegade==True and kopsumma<50:
        piegades_maksa = 15

    elif piegade== True and kopsumma >= 50 and kopsumma<100:
        piegades_maksa=0

    elif piegade == True and kopsumma>=100:
        piegades_maksa = kopsumma*0.95

ievadi_skaitu = int(input('Ievadi, cik kreklus vēlies pasūtīt: '))
ievadit_apdruku = input('Ievadi, ko vēlies uzdrukāt uz krekla: (TEKSTS/ZIME/FOTO) ')
ievadit_piegadi = input('Vai vēlies piegādi?: (j/n)')
if ievadit_piegadi == "j":
    piegade=True
elif ievadit_piegadi == 'n':
    piegade=False

kopsumma = ievadi_skaitu*cena

pasuti_tkreklus(ievadi_skaitu, ievadit_apdruku,ievadit_piegadi)
print(kopsumma+piegades_maksa)

