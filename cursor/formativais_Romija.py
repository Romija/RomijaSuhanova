#funkcija pārbauda, vai vārds atbilst korektas atbildes principiem jeb vai satur tikai burtus
def parbaudit_vardu(vards):
    meginajums = 0
    while meginajums <4:
        if not vards.isalpha():
            print('Vārdā drīkst būt tikai burti')
            meginajums +=1
            return False
        if vards == 'stop':
            print('Programma pārtrauc darbību')
            exit()
        return True
    exit()

#funkcija, kas pārbauda, vai vecums ir derīgs jeb vesels pozitīvs skaitlis
def parbaudit_vecumu(vecums):
    if str(vecums) == 'stop':
        print('Programma pārtrauc darbību')
        exit()
    if not vecums.isdigit():
        print('Vecumam jābūt veselam pozitīvam skaitlim')
        return False
    if int(vecums)<=0:
        print('Vecumam jābūt veselam pozitīvam skaitlim')
        return False
    return True

#funkcija, kas pārbauda, vai atzime ir vesels skaitlis 1-10
def parbaudit_atzimi(atzime):
    if str(atzime) == 'stop':
        print('Programma pārtrauc darbību')
        exit()
    if not atzime.isdigit():
        print('Atzīmei jābūt veselam pozitīvam skaitlim 1-10')
        return False
    if int(atzime)<=0:
        print('Atzīmei jābūt veselam pozitīvam skaitlim 1-10')
        return False
    if int(atzime)>10:
        print('Atzīmei jābūt veselam pozitīvam skaitlim 1-10')
        return False
    return True

#funkcija, kas apstrada vardu jeb pieliek lielo sākumburtu un noņem liekās atstarpes
def normalizet_vardu(vards):
    return vards.strip().capitalize()

#funkcija, kas pārbauda, vai tieši šāds ieraksts jau ir izveidots
def dublikats(vards, uzvards, vecums, atzime, faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        ieraksts = f"{vards},{uzvards},{vecums},{atzime}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False

#funkcija, kas prasa ievadīt datus
def ievadit_datus(faila_nosaukums):
    while True:
        vards = input('Ievadiet vārdu: ')
        if parbaudit_vardu(vards):
            vards=normalizet_vardu(vards)
            break
            
    while True:
        uzvards = input('Ievadiet uzvārdu: ')
        if parbaudit_vardu(uzvards):
            uzvards= normalizet_vardu(uzvards)
            break

    while True:
        vecums = input('Ievadiet vecumu: ')
        if parbaudit_vecumu(vecums):
            break

    while True:
        atzime= input('Ievadiet gala atzīmi: ')
        if parbaudit_atzimi(atzime):
            break

    #ja atbilde ir ja, tad bezgalīgi jautā ievadīt datus, ja ne, tad prasa izvēlēties no izveles opciju
    turpinat = input('Vai vēlaties turpināt? (ja/ne)')
    if turpinat == 'ja':
        ievadit_datus(faila_nosaukums)
    elif turpinat == 'ne':
        izvele()
    else:
        print('Ievadiet ja / ne')

    if dublikats(vards, uzvards, vecums, atzime, faila_nosaukums):
        print('Šis ieraksts jau pastāv')

#funkcija, kas saglabā failā ierakstīto informāciju
def saglabat_faila(vards, uzvards, vecums, atzime, faila_nosaukums):
    with open(faila_nosaukums, 'a', encoding='utf8') as file:
        file.write(f'{vards},{uzvards},{vecums},{atzime}\n')
        print('Dati ir pievienoti')
        return vards

#funkcija, kas konsolē parāda datus
def paradit_datus(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati:
            print('Fails ir tukšs. Pievienojiet datus.')
        else:
            print('Dati no faila: ')
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f'Fails {faila_nosaukums} nepastāv.')

#funkcija, kas iegūst atzīmi no datiem
def iegut_atzimi_no_datiem(ieraksts):
    try:
        atzime = int(ieraksts.strip().split(",")[-1])
        return atzime
    except(IndexError, ValueError):
        return 0

#funkcija, kas sakārto augošā secībā pēc atzīmes
def sakartot_un_paradit(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati:
            print('Fails ir tukšs. Pievienojiet datus.')
        else:
            sakartoti_dati = sorted(dati,key=iegut_atzimi_no_datiem)
            print('Pēc atzīmes sakārtoti dati: ')
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f'Fails {faila_nosaukums} nepastāv.')


#galvenā izvēle, kas izsauc pārējās funkcijas, piedāvājot izvēles
def izvele():
    faila_nosaukums = 'kontroldarbs.txt'

    while True:
        print('Izvēlies opciju: ')
        print('1 - Ievadīt datus ')
        print('2 - Saglabāt datus failā ')
        print('3 - Paradīt datus sakārtotus pēc gala atzīmes (augošā secībā)')
        print('4 - Iziet no programmas')

        izvele = input('Jūsu izvēle: ')
        if izvele == '1':
            ievadit_datus(faila_nosaukums)
        elif izvele == '2':
            saglabat_faila(faila_nosaukums)

        elif izvele== '3':
            sakartot_un_paradit(faila_nosaukums)
            
        elif izvele == '4':
            print('Tiek pārtraukta')
            break
        else:
            print('Nepareiza izvēle. Lūdzu mēģiniet vēlreiz.')

izvele()
