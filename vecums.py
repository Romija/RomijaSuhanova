#funkcija, kas nosaka vecuma statusu atkarībā no ievadītajiem datiem
def parbaudit_vecumu(vecums):
    if vecums <18:
        print('Tu esi nepilngadīgs.')
    elif vecums>=18 and vecums<65:
        print('Tu esi pieaugušais.')
    else:
        print('Tu esi seniors. ')

liet_vecums=int(input('Ievadiet savu vecumu: '))
parbaudit_vecumu(liet_vecums)