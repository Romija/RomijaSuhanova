def parbaudit_vardu_uzvardu(teksts):
    return teksts.isalpha() and teksts.strip() #vai burti

def parbaudit_vecumu(vecums):
    return vecums.isdigit() and int(vecums)>0

def parbaudit_atzimi(atzime):
    return atzime.isdigit() and 0<=int(atzime)<=10

def ierobezo_meginajumus(parbaudit_funkcija, ievades_teksts, kludas_teksts):
    #max 3, ievade ar pārbaudi
    for i in range(3):
        dati = input(ievades_teksts)
        if parbaudit_funkcija(dati):
            return dati
        print(kludas_teksts)
    print('Pārsniegts mēģinājumu skaits')
    
def iegut_ierakstu():
    ieraksti = []
    while True:
        vards = ierobezo_meginajumus(parbaudit_vardu_uzvardu,
                                    'Ievadiet vārdu: ',
                                    'Kļūda: Vārdā drīkst būt tikai burti.')
        if not vards:
            break

        uzvards = ierobezo_meginajumus(parbaudit_vardu_uzvardu,
                                    'Ievadiet uzvārdu: ',
                                    'Kļūda: Uzvārdā drīkst būt tikai burti.')
        if not uzvards:
            break

        vecums = ierobezo_meginajumus(parbaudit_vecumu,
                                    'Ievadiet vecumu: ',
                                    'Kļūda: Vecumam jābūt veselam pozitīvam skaitlim.')
        if not vecums:
            break

        atzime = ierobezo_meginajumus(parbaudit_atzimi,
                                    'Ievadiet atzīmi (1-10): ',
                                    'Kļūda: Atzīme ir no 0-10 skaitlis.')
        if not atzime:
            break

        ieraksti.append((vards,uzvards,int(vecums),int(atzime)))

        turpinat = input('Vai turpināt? (j/n): ').lower()
        if turpinat != 'j': 
            break
    return ieraksti

def saglabat_faila(ieraksti, faila_nosaukums='kontroldarbs.txt'):
    #saglabat ar tab starp laukiem
    with open(faila_nosaukums, 'a', encoding='utf8') as file:
        for ieraksts in ieraksti:
            file.write("\t".join(map(str,ieraksts))+"\n") #+ tab
    print(f'Dati daglabāti failā: {faila_nosaukums}')
    
def paradit_sakartotus_datus(ieraksti):
    #sakārtoti dati pēc gala atzīmes
    #definē anonīmo funkciju lambda, kas pieņem vienu argumentu x(katrs ieraksts no saraksta)
    sakartoti_ieraksti=sorted(ieraksti,key=lambda x:x[3]) #0-3, 3 atzime
    print('\nVārds\tUzvārds\tVecums\tAtzīme')
    for ieraksts in sakartoti_ieraksti:
        print("\t".join(map(str,ieraksts))+"\n")

#kārtošana ar atsevisku f-ju
'''def iegut_gala_atzimi(ieraksts):
    return ieraksts[3]'''

'''def paradit_sakartotus_datus(ieraksti):
    #sakārtoti dati pēc gala atzīmes
    #definē anonīmo funkciju lambda, kas pieņem vienu argumentu x(katrs ieraksts no saraksta)
    sakartoti_ieraksti=sorted(ieraksti,key=iegut_gala_atzimi) #0-3, 3 atzime
    print('\nVārds\tUzvārds\tVecums\tAtzīme')
    for ieraksts in sakartoti_ieraksti:
        print("\t".join(map(str,ieraksts))+"\n")'''

def izvelne(): #programmas galvenā daļa
    ieraksti = []

    while True:
        print('Izvēlies opciju: ')
        print('1 - Ievadīt datus ')
        print('2 - Saglabāt datus failā ')
        print('3 - Paradīt datus sakārtotus pēc gala atzīmes (augošā secībā)')
        print('4 - Iziet no programmas')
        izvele = input('Jūsu izvēle: ')

        if izvele == '1':
            ieraksti+=iegut_ierakstu()
        elif izvele == '2':
            if ieraksti:
                saglabat_faila(ieraksti)
            else:
                print('Nav datu, ko saglabāt')
        elif izvele== '3':
            if ieraksti:
                paradit_sakartotus_datus(ieraksti)
            else:
                print('Nav datu, ko parādīt')
        elif izvele == '4':
            print('Tiek pārtraukta')
            break
        else:
            print('Nepareiza izvēle. Lūdzu mēģiniet vēlreiz.')

izvelne()