def ievadi_ediena_datus():
    global nosaukums, kalorijas_uz_100g, grami
    nosaukums = input("Ievadiet ēdiena nosaukumu: ")

    while True:
        try:
            kalorijas_uz_100g = float(input("Ievadiet kaloriju daudzumu uz 100 gramu: "))
            if kalorijas_uz_100g > 0:
                break
            else:
                print("Kalorijām jābūt lielākām par 0!")
        except ValueError:
            print("Nederīga ievade! Lūdzu, ievadiet derīgu skaitli.")

    while True:
        try:
            grami = float(input("Ievadiet apesto daudzumu gramos: "))
            if grami > 0:
                break
            else:
                print("Gramiem jābūt lielākiem par 0!")
        except ValueError:
            print("Nederīga ievade! Lūdzu, ievadiet derīgu skaitli.")

def aprekinat_apestas_kalorijas():
    global kalorijas
    kalorijas = kalorijas_uz_100g * grami 
    print(f'{nosaukums} satur {kalorijas} kalorijas.')

def saglabat_kaloriju_paterinu():
    global kalorijas
    print(f'Kopējais kaloriju daudzums ir: {kalorijas} kalorijas.')

def ievadi_pareizu_dzimumu():
    global dzimums
    while True:
        dzimums = input('Ievadiet savu dzimumu (sieviete/vīrietis): ')
        if dzimums == 'sieviete' or dzimums == 'vīrietis':
            break
        else:
            print('Lūgums atkārtot ievadi.')

def ievadi_pareizu_aktivitates_limenis():
    global aktivitates_limenis
    while True:
        aktivitates_limenis = input('Ievadiet savu aktivitātes līmeni (zems/videjs/augsts):')
        if aktivitates_limenis == 'zems' or aktivitates_limenis == 'videjs' or aktivitates_limenis == 'augsts':
            break
        else:
            print('Lūgums atkārtot ievadi.')

def aprekinat_ieteikto_kaloriju_daudzumu():
    global ieteiktais_kaloriju_daudzums, svars, vecums, dzimums
    if dzimums == 'vīrietis':
        ieteiktais_kaloriju_daudzums = 66 + (svars * 13.7) + (5 * 170) - (6.8 * vecums)
    elif dzimums == 'sieviete':
        ieteiktais_kaloriju_daudzums = 655 + (svars * 9.6) + (1.8 * 160) - (4.7 * vecums)

def sniegt_parskatu():
    global kalorijas, ieteiktais_kaloriju_daudzums
    if kalorijas < ieteiktais_kaloriju_daudzums:
        print('Jūsu kaloriju daudzums ir zem normas robežas.')
    elif kalorijas > ieteiktais_kaloriju_daudzums:
        print('Jūsu kaloriju daudzums ir virs normas robežas.')
    else:
        print('Jūsu kaloriju daudzums ir iekļaujas normas robežās.')

ievadi_ediena_datus()
aprekinat_apestas_kalorijas()
svars = float(input('Ievadiet savu svaru (kg): '))
vecums = int(input('Ievadiet savu vecumu: '))
ievadi_pareizu_dzimumu()
ievadi_pareizu_aktivitates_limenis()
aprekinat_ieteikto_kaloriju_daudzumu()
saglabat_kaloriju_paterinu()
sniegt_parskatu()
