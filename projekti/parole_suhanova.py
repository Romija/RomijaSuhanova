pareizs_lietotajvards = 'skolens' #pareizais lietotājvārds
pareiza_parole = '12345' #pareizā parole
i = 0 #skaitīs, cik reizes lietotājs ievada (max 5)
lietotajvards = input('Ievadiet lietotājvārdu: ')
parole = input('Ievadiet paroli: ')
varda_garums = len(parole) #paroles garums
while i<=5: #neatļauj vairāk par 5 reizēm, ja kļūdās
    if pareizs_lietotajvards == lietotajvards and pareiza_parole==parole: #pārbauda vai pareizi viss
        print('Pieslēgšanās veiksmīga!') #turpinās 2.uzdevums
        skaitlis1 = int(input('Ievadi pirmo veselo skaitli: '))
        skaitlis2 = int(input('Ievadi otro veselo skaitli: '))
        if skaitlis1<0 or skaitlis2<0: #nevar būt negatīvi
            print('Nedrīkst būt negatīvs skaitlis!')
        elif skaitlis1>skaitlis2: #pirmajam jābūt mazākam
            print('0')
        else:
            while skaitlis1<skaitlis2: #kamēr pirmais skailtis ir mazāks pie pirmā skaitļa pieskaita 1
                summa = skaitlis2 + skaitlis1
                nakamais_skaitlis = skaitlis1+1 #katrs nākamais skaitlis
                print('Veselu secīgi pieaugušo skaitļu no',skaitlis1,'līdz',skaitlis2, 'summa ir: ',summa)
                break #programma apstājas

    elif pareizs_lietotajvards != lietotajvards or pareiza_parole != parole: #pārbauda vai pareizs
        for num in range(4,0,-1): #ja nepareizi, tad sākas mēģinājumu atskaite
            print(f'Vēl atlikuši {num} mēģinājumi! ')
            i+=1
            lietotajvards = input('Ievadiet lietotājvārdu: ')
            parole = input('Ievadiet paroli: ')
        if num == 0:
            print('Atļauts pieslēgties tikai 5 reizes!')
            break #beidzas atskaite
        if varda_garums!=5: #ja parolē nav 5 cipari, tad parādas paziņojums
            print('Parolē ir 5 rakstzīmes!')

    elif lietotajvards == 'stop' or parole == 'stop' or skaitlis1 == 'stop' or skaitlis2 == 'stop': #ja ievada stop, exit
        exit()

    '''elif varda_garums!=5:
        print('Parolē ir 5 rakstzīmes!')
    #varda_garums = len(teksts)'''

    



