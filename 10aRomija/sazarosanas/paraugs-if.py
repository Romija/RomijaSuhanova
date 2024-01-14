#izveidot vārdnīcu ar datiem par automašīnu(4)
auto = {
    'Zīmols':'Volvo',
    'Krāsa': 'Balts',
    'Gads': 2021,
    'Modelis': 'xc90'
}

dati = input('Ievadiet zīmolu, lai pārbaudītu: ')
if  dati == auto['Zīmols']:
    print('Ir vārdnīcā')

elif dati == auto.values():
    print('🚗Auto ir kā vērtība')

else:
    print('Šāda auto nav')
