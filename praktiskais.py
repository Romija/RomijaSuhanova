#ierakstīt teksta failā (no programmaas) vārdu, uzvārdu, vecumu.
#dot iespēju izvēlēties : 1-pievienot datus, 
# 2 - nolasīt datus
# 3- parādīt, sakārtot datus pēc vecuma
# 4 - iziet
#apstrādāt kļūdas
#def pievienot_datus_failam(), def sakartot_pec_vecuma(), def paradit_sakartotus_datus()

while True:
    print('Izvēlies opciju: ') #sakārtošana parasti ir augstākam vērtējumam
    print('1 - pievienot datus ')
    print('2 - paradīt datus ')
    print('3 - iziet')

    izvele = input('Izvēle: ')
    if izvele == '1':
        vards = input('Ievadiet vārdu: ')
        uzvards = input('Ievadiet uzvārdu: ')
        vecums = int(input('Ievadiet vecumu: '))
        #datus saglabāt teksta failā
        with open('dati.txt', 'a', encoding='utf8') as file: #file vietā var arī ko citu
            file.write(f'{vards} {uzvards} {vecums} \n')
        print('Dati ir pievienoti')

    elif izvele == '2':
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
            print('Fails nepastāv.')

    elif izvele == '3':
        print('Izvēle tiek pārtraukta. ')
        break
        
    else:
        print('Nepareiza izvēle. Mēģiniet vēlreiz.')