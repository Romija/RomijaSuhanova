kopsumma = 0.00 #kopsumma
masa = 0.00
print('Pieejamas 2 receptes')
print('Pirmā recepte: 3kg ābolu, 2kg parastā cukura vai 1kg ievārījuma cukura, 500ml ūdens, 1gab citrona, 5ml mandeļu ekstrakta, 10g kanēlis')
print('Otrā recepte: 3kg ābolu, 1kg ievārījuma cukura vai 2kg parāstā, 500ml ūdens, 10g kanēlis')

recepte = int(input('Kuri no receptēm Jūs izvēlaties? (1/2): ')) #izvēlas recepti

if recepte == 1: #prasa visu ievadīt pirmajai receptei
    abolu_daudzums = int(input('Cik kg ābolu Jums ir? '))
    udens_daudzums = int(input('Cik ml ūdens Jums ir? '))
    citronu_daudzums = int(input('Cik citronu Jums ir? '))
    mandelu_daudzums = int(input('Cik ml Jums ir ar mandeļu ekstraktu? '))
    kanela_daudzums = int(input('Cik grami kanēļa Jums ir? '))
    cukura_izvele = input('Vai Jūs izmantosiet parasto vai ievārījuma cukuru? ')

#pārbauda, kuru cukuru izmantos
    if cukura_izvele== "parasto": 
        parasta_cukura_daudzums= int(input('Cik kg ar parasto cukuru Jums ir? '))
    elif cukura_izvele=='ievārījuma':
        ievarijuma_cukura_daudzums = int(input('Cik kg Jums ir ar parasto ievārījumu? '))
    else:
        print('Ievadiet pareizus datus!')
        exit()

    print('\n------------------\nSaraksts ar lietām un cenām: \n') #saraksta ar lietām, ko vajag pirkt un cenas klāt
#pārbauda vai pietiekami, un, ja nē, tad aprēķina cik jāpērk vēl un cik tas izmaksās
    if abolu_daudzums >=3:
        print('Jums ir pietiekami daudz ābolu')
    elif abolu_daudzums<3 and abolu_daudzums>=0:
        aboli_japerk=3-abolu_daudzums
        aboli_maksa=aboli_japerk*0.60 #cena 0.6euro par kg
        print('Jums vajag vēl',aboli_japerk,'kg ābolus. Tas izmaksās',aboli_maksa,'Euro')
        kopsumma+=aboli_maksa
    else:
        print('Ievadiet pareizus datus!')
        exit()


    if udens_daudzums >=500: #duadzumu pārbauda
        print('Jums ir pietiekami daudz ūdens')
    elif udens_daudzums<500:
        udens_japerk=500-udens_daudzums
        udens_maksa=0.50 #cena
        print('Jums vajag vēl',udens_japerk,'ml ūdens. Tas izmaksās',udens_maksa,'Euro')
        kopsumma+=udens_maksa
    else:
        print('Ievadiet pareizus datus!')
        exit()

    
    if cukura_izvele == 'parasto': #pārbauda vai parasto cukuru izmantos
        if parasta_cukura_daudzums>=2:
            print('Pietiekami daudz parastā cukura')
        elif parasta_cukura_daudzums<2:
            parastais_cukurs_japerk=2-parasta_cukura_daudzums
            parasta_cukura_maksa=parastais_cukurs_japerk*1.20 #cena 
            print('Jums vajag vēl',parastais_cukurs_japerk,'kg parastā cukura. Tas izmaksās',parasta_cukura_maksa,'Euro')
            kopsumma+=parasta_cukura_maksa
        else:
            print('Ievadiet pareizus datus')
            exit()
    elif cukura_izvele=='ievārījuma':
        if ievarijuma_cukura_daudzums>=1.00:
            print('Pietiekami daudz ievārījuma cukura')
        elif ievarijuma_cukura_daudzums<1.00:
            ievarijuma_cukurs_japerk=1.00-ievarijuma_cukura_daudzums
            ievarijuma_cukura_maksa = 2.59
            print('Jums vajag vēl',ievarijuma_cukurs_japerk,'kg ievārījuma cukura. Tas izmaksās',ievarijuma_cukura_maksa,'Euro')
            kopsumma+=ievarijuma_cukura_maksa
        else:
            print('Ievadiet pareizus datus')
            exit()
    else:
        print('Ievadi pareizus datus')
        exit()

    if citronu_daudzums>1:
        print('Jums ir pietiekami daudz citronu')
    elif citronu_daudzums<1:
        print('Jums vajag vēl 1gab citrona. Tas izmaksās',0.45,'Euro')
        kopsumma+=0.45
    else:
        print('Ievadiet pareizus datus')
        exit()

    if mandelu_daudzums>=5:
        print('Jums ir pietiekami daudz mandeļu ekstrakta')
    elif mandelu_daudzums<5:
        print('Jums bajag nopirkt mandeļu ekstraktu. Tas izmkasās',6.39,'Euro')
        kopsumma+=6.39
    else:
        print('Ievadiet pareizus datus')
        exit()

    if kanela_daudzums>=10:
        print('Jums ir pietiekams daudzums kanēļa')
    elif kanela_daudzums<10:
        print('Jums vajag nopikt kanēli. Tas izmaksās',1.19,'Euro')
        kopsumma+=1.19
    else:
        print('Ievadiet pareizus datus')
        exit()


if recepte == 2:
    abolu_daudzums = int(input('Cik kg ābolu Jums ir? '))
    udens_daudzums = int(input('Cik ml ūdens Jums ir? '))
    kanela_daudzums = int(input('Cik grami kanēļa Jums ir? '))
    cukura_izvele = input('Vai Jūs izmantosiet parasto vai ievārījuma cukuru? ')

    if cukura_izvele== "parasto":
        parasta_cukura_daudzums= int(input('Cik kg ar parasto cukuru Jums ir? '))
    elif cukura_izvele=='ievārījuma':
        ievarijuma_cukura_daudzums = int(input('Cik kg Jums ir ar parasto ievārījumu? '))
    else:
        print('Ievadiet pareizus datus!')
        exit()

    print('\n------------------\nSaraksts ar lietām un cenām: \n') 

    if abolu_daudzums >=3:
        print('Jums ir pietiekami daudz ābolu')
    elif abolu_daudzums<3:
        aboli_japerk=3-abolu_daudzums
        aboli_maksa=aboli_japerk*0.60
        print('Jums vajag vēl',aboli_japerk,'kg ābolus. Tas izmaksās',aboli_maksa,'Euro')
        kopsumma+=aboli_maksa
    else:
        print('Ievadiet pareizus datus!')
        exit()


    if udens_daudzums >=500:
        print('Jums ir pietiekami daudz ūdens')
    elif udens_daudzums<500:
        udens_japerk=500-udens_daudzums
        udens_maksa=0.50
        print('Jums vajag vēl',udens_japerk,'ml ūdens. Tas izmaksās',udens_maksa,'Euro')
        kopsumma+=udens_maksa
    else:
        print('Ievadiet pareizus datus!')
        exit()

    
    if cukura_izvele == 'parasto':
        if parasta_cukura_daudzums>=2:
            print('Pietiekami daudz parastā cukura')
        elif parasta_cukura_daudzums<2:
            parastais_cukurs_japerk=2-parasta_cukura_daudzums
            parasta_cukura_maksa=parastais_cukurs_japerk*1.20
            print('Jums vajag vēl',parastais_cukurs_japerk,'kg parastā cukura. Tas izmaksās',parasta_cukura_maksa,'Euro')
            kopsumma+=parasta_cukura_maksa
        else:
            print('Ievadiet pareizus datus')
            exit()
    elif cukura_izvele=='ievārījuma':
        if ievarijuma_cukura_daudzums>=1.00:
            print('Pietiekami daudz ievārījuma cukura')
        elif ievarijuma_cukura_daudzums<1.00:
            ievarijuma_cukurs_japerk=1.00-ievarijuma_cukura_daudzums
            ievarijuma_cukura_maksa = 2.59
            print('Jums vajag vēl',ievarijuma_cukurs_japerk,'kg ievārījuma cukura. Tas izmaksās',ievarijuma_cukura_maksa,'Euro')
            kopsumma+=ievarijuma_cukura_maksa
        else:
            print('Ievadiet pareizus datus')
            exit()
    else:
        print('Ievadi pareizus datus')
        exit()

    if kanela_daudzums>=10:
        print('Jums ir pietiekams daudzums kanēļa')
    elif kanela_daudzums<10:
        print('Jums vajag nopikt kanēli. Tas izmaksās',1.19,'Euro')
        kopsumma+=1.19
    else:
        print('Ievadiet pareizus datus')
        exit() 

else:
    print('Ievadi pareizus datus')

print('Kopā tas izmaksās: ' "%.2f"%kopsumma)

if recepte == '1':
    if cukura_izvele == 'parasto':
        print('Iespējamssavārīt 5,7kg ievārījuma')
    elif cukura_izvele == '2':
        print('Iespējams izvārīt 4,7kg ievārījuma')
    else:
        print('Ievadi korektus datus')
elif recepte == '2':
    if cukura_izvele == 'parasto':
        print('Iespējam izvārīt 5,5kg ievārījuma')
    elif cukura_izvele == 'ievārījuma':
        print('Iespējams uzvārīt 4,5kg ievārījuma')
    else:
        print('Korektus datus ievadīt')
else:
    print('Ievadi korektus datus')

#vēl vajadzētu izrēķināt kopsummu ar if else un skatīties kādu cukuru izmanto, jo atšķiras masa
#ieteikums nākšajai reizei: lai ome pati ievada un tad programma skatās, kas viņai sanāk(tur varētu izmantot sarakstu bet nez kā var ar vairākiem vārdiem)
