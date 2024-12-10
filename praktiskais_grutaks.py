#ierakstīt teksta failā (no programmaas) vārdu, uzvārdu, vecumu.
#dot iespēju izvēlēties : 1-pievienot datus, 
# 2 - nolasīt datus
# 3- parādīt, sakārtot datus pēc vecuma
# 4 - iziet
#apstrādāt kļūdas
#def pievienot_datus_failam(), def sakartot_pec_vecuma(), def paradit_sakartotus_datus()

def parbaudit_vardu(vards): #pārbauda vai dati sastāv tikai no burtiem
    if not vards.isalpha():
        print('Vārdā drīkst būt tikai burti')
        return False
    return True

def parbaudit_vecumu(vecums): #pārbauda vai derīgi dati
    if not vecums.isdigit():
        print('Vecumam jābūt kā skaitlim')
        return False
    if int(vecums)<=0:
        print('Ievadi pozitīvu skaitli')
        return False
    return True

def normalizet_vardu(vards):
    return vards.strip().capitalize() #noņem lieko, uzliek lielo burtu

def dublikats(vards, uzvards, vecums,faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as file:
            dati = file.readlines()
        ieraksts = f"{vards},{uzvards},{vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False #jo fails nav izveidots

def pievienot_datus_failam(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'a', encoding='utf8') as file:
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
        #datus saglabāt teksta failā
            if dublikats(vards, uzvards, vecums, faila_nosaukums):
                print('Šis ieraksts jau pastāv')


            file.write(f'{vards},{uzvards},{vecums}\n')
            print('Dati ir pievienoti')

    except Exception as e:
        print(f'Kļūda, saglabājot datus failā {e}')

def paradit_datus(faila_nosaukums):
    try:
        with open('dati.txt', 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati: #ja nav dati
            print('Fails ir tukšs. Pievienojiet datus.')
        else:
            print('Dati no faila: ')
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f'Fails {faila_nosaukums} nepastāv.')

def iegut_vecumu_no_datiem(ieraksts):
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
        #ja formāts nav pareizs, atgriež 0
    except(IndexError, ValueError):
        return 0

def sakartot_un_paradit(faila_nosaukums): #nesakārto failā, bet konsolē
    try:
        with open('dati.txt', 'r', encoding='utf8') as file:
            dati = file.readlines()
        if not dati: #ja nav dati
            print('Fails ir tukšs. Pievienojiet datus.')
        else:
            #kārtošana
            sakartoti_dati = sorted(dati,key=iegut_vecumu_no_datiem)
            print('Pēc vecuma sakārtoti dati: ')
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f'Fails {faila_nosaukums} nepastāv.')


#programmas galvenā daļa
def izvele():
    faila_nosaukums = 'dati.txt'

    while True:
        print('Izvēlies opciju: ') #sakārtošana parasti ir augstākam vērtējumam
        print('1 - pievienot datus ')
        print('2 - paradīt datus ')
        print('3 - Paradīt sakārtotus datus pēc vecuma')
        print('4 - iziet')

        izvele = input('Izvēle: ')
        if izvele == '1':
            pievienot_datus_failam(faila_nosaukums)
        elif izvele == '2':
            paradit_datus(faila_nosaukums)

        elif izvele== '3':
            sakartot_un_paradit(faila_nosaukums)
            
        elif izvele == '4':
            print('Tiek pārtraukta')
            break
        else:
            print('Nepareiza izvēle. Lūdzu mēģiniet vēlreiz.')

izvele()