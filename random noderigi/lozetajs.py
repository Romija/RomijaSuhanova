'''Izveido lozēšanas spēli
kur lietotājs mēģina uzminēt skaitli no 1 līdz 10.
 Programma izvada atbilstošus paziņojumus atkarībā no lietotāja ievades.'''
import random
minejums = int(input('Ievadiet minējumu: '))
skaitlis = random.randint(1,10)
while skaitlis>0:
    if minejums !=skaitlis:
        print('Neuzminējāt')
        minejums = int(input('Ievadiet minējumu: '))
    elif skaitlis == minejums:
        print('Uzminējāt')
        break
