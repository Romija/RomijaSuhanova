koslenes = input('Taksī nevar košļāt košļenes! Vai Jums mutē ir košļene?(j/n)') #papildus funkcija, pārbauda vai ir košļenes
if koslenes == 'j': #ja ir košļenes, tad neturpina
    print('Izmetiet košļeni!')
elif koslenes == 'n':#ja nav košļenes tad turpina programmu
    skaits = input('Vai mašīnā ir vairāk par 4 cilvēkiem? (j/n) ')
    if skaits == 'j': #ja mašīnā virs 4 cilvēkiem tad neturpina
        print('Pārsniegts pasažieru skaits!(max var būt 4)')
    elif skaits == 'n': #Ja nav pārsniegts tad turpina
        laiks = int(input('Kāds ir pulksteņa laiks? (laiku ievadīt veselos skaitļos)')) #paprasa ievadīt laiku
        if laiks <5 or laiks==23: #salīdzina vai nakts tarifs jāmaksā
            nakts = laiks * 0.87 #aprēķina nakts laikā cenu par brauciena laiku
        elif laiks <23 and laiks >5: #pārbauda vai dienas laiks
            diena = laiks * 0.47 #aprēķina dienas laikā tarifu par brauiena laiku
        if laiks > 0: #pārbauda vai ievadīts korekts laiks 
            noligsana = input('Vai Jūs stāvlaukumā redzat taksi? (j/n)') #lietotājs ievada vai izsaukuma maksa būs jāmaksā
            if noligsana == 'n':#pārbauda vai jāmaksā izsaukuma maksa
                nav_taksis = 1.20 + 2.40 #izsaukuma maksa + nolīgšana
            elif noligsana == 'j': 
                ir_taksis = 1.20 #ja nav jāizsauc
            if noligsana == 'j' or 'n':
                gaidisana = input('Vai Jūs pa ceļam vēlaties piestāt kaut kur? (j/n)') #jautā vai jāgaida
                if gaidisana == 'j':
                    gaidit_laiks = int(input('Ievadi, cik min būs jāgaida')) #jautā, cik minūtes jāgaida
                if gaidisana == 'n': #ja lietotājs ievada ka negrib gaidīt tad nav par gaidīšanu maksa
                    print('Nav jāmaksā gaidīšanas maksa') 
                if gaidisana == 'j' or 'n':
                    km = int(input('Cik km jābrauc: ')) #jautā cik km brauks
                    if km > 0:
                        print('\n\t********************\n\t\tČEKS')
                        if laiks <5 or laiks==23:
                            print ('Nakts tarifs: 0,87Euro par 1km. \nNobrauktie km: ',km)
                        elif laiks <23 and laiks >5:
                            print('Nakts tarifs: 0,47Euro par 1km. \nNobrauktie km: ',km)
                            
else:
    print('Kļūda')


            
