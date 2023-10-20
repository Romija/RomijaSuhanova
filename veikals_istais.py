stop = '0'
ceks = 'Iepirkšanās čeks: '#izveidots, lai  nebūtu katrei jāraksta
summa_bez_atlaides = 0.0
kopsumma = 0.0 #ar atlaidi

while stop == '0':
    ceks

    precu_skaits = int(input('Ievadiet preču skaitu: '))
    if precu_skaits<0:
        exit()
    produkts = input('Ievadiet produktu nosaukumu: ')
    produkta_cena = round(float(input('Ievadiet cenu 1 preces gab: ')),2)#formatē 2 sk aiz komata
    #atlaides var izvēlēties, ierakstot skaitli 1-5
    print('\n1-Maxima: 30% atlaide\n2-Elvi:40%, ja ir klienta karte\n3-Rimi:20%, bet 50% ja ir karte\n4-Mego: 30% ja pērk 3 un vairāk preces\n5-Aibe: Katra otrā prece par brīvu')

    atlaides_veids = input('Izvēlēties, kurā veikalā iepirksieties(raksties ciparu 1-5)')

    cena_bez_atlaides = produkta_cena*precu_skaits #iegūst cenu bez atlaidēm
    pirkuma_cena = cena_bez_atlaides #no pikuma cenas rēķinās atlaides

    #sākas atlaižu aprēķināšana
    if atlaides_veids == '1': #atlaide maxima
        #pirkuma_cena = pirkuma_cena*0.7
        pirkuma_cena*=0.7 #izmanto salikto reizināšanas operatoru
    elif atlaides_veids == '2':
        klienta_karte = input('Vai Jums ir Elvi karte? (1 ir, 0nav)')
        if klienta_karte == '1':
            pirkuma_cena*=0.6 #atlaide 40%

    elif atlaides_veids == '3': #rimi atlaide
        klienta_karte = input('Vai Jums ir Elvi karte? (1 ir, 0nav)')
        if klienta_karte == '1':
            pirkuma_cena*=0.5 #atlaide 50%
        else:
            pirkuma_cena*=0.8

