kopsumma = 0.00
koslenes = input('Košļenes ir aizliegtas! Vai Jums mutē ir košļene? (j/n): ') 
if koslenes == 'j':
    print('Lūgums izmest košļeni!')
elif koslenes == 'n':
    skaits = input('Vai taksī ir vairāk par 4 cilvēkiem? (j/n): ')
    if skaits == 'j': 
        print('Pārsniegts pasažieru skaits!(max var būt 4)')
    elif skaits != 'n' and 'j':
        print('Lūgums ievadīt derīgus datus!')
        exit()
    elif skaits == 'n': 
        laiks = int(input('Lūgums ievadīt pulksteņa laiku. (1-24): ')) 
        if laiks>24:
            print('Lūgums ievadīt derīgus datus!')
        if laiks <5 or laiks==24 or laiks==23: 
            nakts = 0.87 
        elif 5<laiks<23 or laiks==5: 
            diena = 0.47 
        if laiks > 0: 
            noligsana = input('Vai stāvlaukumā redzat taksi? (j/n): ') 
            if noligsana == 'n':
                nav_taksis = 1.20 + 2.40 
            elif noligsana == 'j': 
                ir_taksis = 1.20 
            elif noligsana != 'j' and 'n':
                print('Lūgums ievadīt derīgus datus!')
                exit()
            if noligsana == 'j' or 'n':
                gaidisana = input('Vai Jūs vēlatos pa ceļam piestāt kaut kur? (j/n): ') 
                if gaidisana == 'n':
                    kopsumma
                elif gaidisana == 'j':
                    gaidit_laiks = int(input('Ievadiet, cik min šoferim būs jāgaida: ')) 
                    if gaidit_laiks>0:
                        maksa_gaidit = gaidit_laiks * 0.15
                    else:
                        print('Lūgums ievadīt derīgus datus!')
                        exit()
                if gaidisana != 'n' and gaidisana!= 'j':
                    print('Lūgums ievadīt derīgus datus!')
                    exit()
                if gaidisana == 'j' or 'n':
                    km = int(input('Cik km jābrauc: ')) 
                    if km<0:
                        print('Lūgums ievadīt derīgus datus!')
                        exit()
                    elif km > 0:
                        print('\n\t********************\n\t\tČEKS')
                        if laiks <5 or laiks==24 or laiks==23:
                            kopsumma += nakts*km
                            print('Nakts tarifs par 1km: 0,87Euro \nNobrauktie km: ',km,'\nPar ceļu jāmaksā: ',nakts*km)
                        elif 5<laiks<24 or laiks==5:
                            kopsumma+=diena*km
                            print('Nakts tarifs par 1km: 0,47Euro  \nNobrauktie km: ',km,'\nPar ceļu jāmaksā: ',diena*km)
                            if noligsana == 'n':
                                kopsumma += nav_taksis
                                print('Par nolīgšanu un izsaukšanu: ' "%.2f"%nav_taksis)
                            elif noligsana == 'j':
                                kopsumma += ir_taksis
                                print('Par nolīgšanu jāmaksā: ' "%.2f"%ir_taksis)
                    if gaidisana =='j':
                        kopsumma += maksa_gaidit
                        print('0,15Euro par katru gaidīšanas minūti.\nJūs gaidīja: ',gaidit_laiks,' minūtes\nPar gaidīšanu kopā jāmaksā: ' "%.2f"%maksa_gaidit,'\n')
                    elif gaidisana == 'n':
                        print('')
                    
    print('Jūs kopsumma: ' "%.2f"%kopsumma,'\nPaldies par braucienu!\n\n\t********************')
else:
    print('Kļūda')