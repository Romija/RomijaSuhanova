'''prasīt ievadīt datus līdz brīdim, kamēr ievada tukšu rindu.
datus saglabā failā'''
dati = []
while True:
    ievades_dati=input('Ievadiet datus(iziet-lai izietu),Enter, lai beigtu rakstīt: ')
    if ievades_dati.lower()=='iziet':
        print('Programma pārtraukta pēc jūsu lūguma! ')
        break
    #pārtrauc ciklu, ja ievada tukšu rindu jeb enter
    elif not ievades_dati:
        break
    dati.append(ievades_dati)

    #atvērt failu, lai ierakstītu datus
    with open('jaunais_fails.txt','w',encoding='utf8') as file:
        #ieraksta katru savā rindā
        for line in dati:
            file.write(line+'\n')
    print('Dati ierakstīti jaunajā failā')
