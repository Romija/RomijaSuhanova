dati = {
    '1. decembris': 23,
    '2. decembris': 24,
    '3. decembris': 25,
    '4. decembris': 26,
    '5. decembris': 27,
    '6. decembris': 28,
    '7. decembris': 29,
}

skaits = 0  # mēģinājumu skaits

while skaits < 5:
    datums = input('Ievadiet datumu (piemēram, 1. decembris): ')
    if datums in dati:
        temperature = dati[datums]
        result = temperature * 2
        print(f"Sareizinātā temperatūra: {result}")
        break
    else:
        print('Nepareiza atslēga')  # ja nav vārdnīcā, tad pieskaita mēģinājumu skaitam 1
        skaits += 1

if skaits == 5:
    print("Jūs esat izsmēluši visus mēģinājumus.")
