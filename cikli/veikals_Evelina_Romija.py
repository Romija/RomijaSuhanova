
pirkums = input('Vai tu vēl kaut ko gribi nopirkt?: (j/n)')
while pirkums == 'j':
    prece = input('Ko vēlaties nopirkt?: ')
    daudzums = float(input('Cik vēlaties nopirkt?: '))
    cena = float(input('Ievadi cenu: '))
    if daudzums>0:
        maksa = cena*daudzums
    else:
        exit()
    pirkums = input('Vai tu vēl kaut ko gribi nopirkt?: (j/n)')
else:
    print('----------ČEKS----------')
    
veikals = input('Ievadi veikalu: (rimi/maxima/elvi/top/lats)')
if veikals == 'rimi':
    veikala_maksa= maksa *0.7
elif veikals == 'maxima':
    karte = input('vai Jums ir paldies karte? (j/n)')
    if karte == 'j':
        veikala_maksa = maksa *0.6
    elif karte == 'n':
        veikala_maksa= maksa
    else:
        print('Ievadi korektus datus')
elif veikals == 'elvi':
    elvi_karte = input('Vai Jums ir elvi karte?: ')
    if elvi_karte == 'j':
        veikala_maksa = maksa *0.5
    elif elvi_karte =='n':
        veikala_maksa= maksa*0.8
    else:
        print('Ievadi korektus datus')
elif veikals == 'top':
    if daudzums>=3:
        veikala_maksa = maksa * 0.70
    elif daudzums<3:
        veikala_maksa=maksa
    else:
        print('Ievadi korektus datus')

print('Tava cena ',veikals,' būs: ',veikala_maksa,'!')