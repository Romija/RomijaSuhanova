#vārdnīca
kontakti = {
    'vards':[],
    'numurs':[]
}

#vārdnīcas elementi
kontakti['vards'] = ['Anna', 'Zane', 'Jānis','Gustavs']
kontakti['numurs'] = ['2222222','333333','444444','555555']

#izvēles
print('Ko vēlaties darīt? ')
print('\t\t\t1-drukāt')
print('\t\t\t2-pievienot')
print('\t\t\t3-izdzēst')
print('\t\t\t4-iziet')

#kamēr nav 4, kods turpinās
izvele = 0
while izvele != '4':
    izvele = input('Ievadiet atbilstošo ciparu: ')
    if izvele == '1': #izdrukā sarakstu
        print(f'Jūs uzspiedāt taustiņu  1: jūsu kontakti uz ekrāna:/n{kontakti}')

    elif izvele == '2': #pievieno klontaktu
        print('Jūs uzspiedāt taustiņu 2: pievieno jaunu kontaktu: ')
        vards = input('Ievadi vārdu: ')
        numurs = input('Ievadi numuru: ')
        kontakti.update({vards:numurs}) #pievieno beigās

    elif izvele == '3': #izdzēš
        print(f'Jūs uzspiedāt taustiņu  3: izdzēst kontaktu')
        izdzestais_vards = input('Ievadi vārdu, ko izdzēst: ')
        if izdzestais_vards in kontakti: #ja vārds ir vārdnīcā
            kontakti.pop(izdzestais_vards)
        else: #ja vārds nav vārdnīcā
            print('Tāds vārds nav vārdnīcā')

    elif izvele == '4': #exit
        print('Jūs uzspiedāt taustiņu 4: paldies, ka izmantojāt šo programmu ')
        exit()
        