gads = int(input('Ievadi gadu: ')) #lietotājs ievada gadu
if gads<0: #gads nevar būt negatīvs skaitlis
    print('Nekorekti dati')
    exit()
elif gads == 0: #gads nevar būt nulle
    print('Nav tāda gada')
    exit()
else:
    if gads %4 == 0: #ja gads dalās ar 4, tas ir garais gads
        print(f'{gads} ir garais gads.')
    else: #ja nedalās, tad tas ir īsais gads
        print(f'{gads} ir īsais gads.') 