dati = { #dotā vārdnīca
    '1. decembris': 23,
    '2. decembris': 24,
    '3. decembris': 25,
    '4. decembris': 26,
    '5. decembris': 27,
    '6. decembris': 28,
    '7. decembris': 29,
    }

skaits = 0 #mēģinājumu skaits
    
datums = input('Ievadiet datumu (piemēram, 1. decembris): ')
while skaits <5:
    if datums != dati.get(datums):
        print('Nepareizē atslēga') #ja nav vārdīcā, tad pieskaita mēģinājumu skaitam 1
        skaits+=1
        datums = input('Ievadiet datumu (piemēram, 1. decembris): ')
else:
    index = list(dati).index(datums) #ja ir tad atrod vērtību atblstošo
