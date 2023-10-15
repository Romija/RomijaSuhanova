import random
kopsumma1=0
kopsumma2=0
vards1 = input('Ievadiet pirmā spēlētāja vārdu: ')
vards2 = input('Ievadiet otrā  spēlētāja vārdu: ')
gajienu_skaits = int(input('Ievadiet gājienu skaitu: '))
for i in range(1,gajienu_skaits,1):
    rezultats1 = random.randint(1,6)
    rezultats2 = random.randint(1,6)
    print('Pirmais spēlētājs:',vards1,'\t',i,' gājiens: ',rezultats1)
    print('Otrais spēlētājs: ',vards2,'\t',i,' gājiens: ',rezultats2)
    kopsumma1 += rezultats1
    kopsumma2 += rezultats2
print('\n',vards1,'nopelnījis ',kopsumma1,'punktus kopā')
print('',vards2,'nopelnījis ',kopsumma2,'punktus kopā')