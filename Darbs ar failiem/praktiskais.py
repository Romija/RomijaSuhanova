'''uzrakstīt programmu,
kas lasa katru rindiņu un sadala to vārdos
programma pārbauda vai ir pietiekams datu skaits,
lai izvadītu info un pēc tam izvada datus uz ekrāna'''

#uzdevums sadalīts sīkāk:
#izveido savā mapē faulu vardi.txt

faila_nosaukums = 'vardi.txt'

#atvērt failu un nolasīt datus
try:
    with open(faila_nosaukums,'r',encoding='utf 8') as fails:
#katru rindu sadala pa vārdiem, izmantojot atstarpes kā atdalītājus
        for rindina in fails:
            dati = rindina.split()
#pārbaudīt vai ir pietiekams datu skaits(vārds, uzvārds, vecums)
            if len(dati) >= 3:
                vards = dati[0]
                uzvards = dati[1]
                vecums = dati[2]
#parādīt datus uz ekrāna
                print(f'Vārds:{vards},Uzvārds:{uzvards},Vecums: {vecums}')
            else:
                print('Kļūda: failā nepietiek datu.')

except FileNotFoundError:
    print(f'Kļūda: Fails{faila_nosaukums} nav atrasts')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda = {e}')