import math

linoleja_daudzumi = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
kopejais_linoleja_daudzums = 0.00

izmaksas_kopejas = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
kopsumma = 0.00

atlikusie_linoleji = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
atlikumi = 0.00 #kopējais atlikušais linolejs

while True:
    izvele = input('Vai vēlaties rēķināt? (j/n): ')

    if izvele.lower() != 'n' and izvele.lower() != 'j':
        print('Nekorekti dati')
        exit()

    if izvele.lower() == 'n':
        break

    linolejs_cena = float(input('Ievadi linoleja cenu par kvadrātmetru: '))
    rulla_platums = float(input('Ievadi ruļļa platumu: '))
    rulla_garums = float(input('Ievadi ruļļa garumu: '))
    rulla_platiba = rulla_platums*rulla_garums
    istabas_garums = float(input('Ievadi istabas garumu: '))
    istabas_platums = float(input('Ievadi istabas platumu: '))
    istabas_platiba = istabas_garums*istabas_platums
    linoleja_daudzums = istabas_platiba
    izmaksas_linolejs = (math.ceil(linoleja_daudzums))*linolejs_cena
    atlikusais_linolejs =  rulla_platiba-istabas_platiba

    linoleja_daudzumi.append(linoleja_daudzums)
    kopejais_linoleja_daudzums+=linoleja_daudzums

    izmaksas_kopejas.append(izmaksas_linolejs)
    kopsumma+=izmaksas_linolejs

    atlikusie_linoleji.append(atlikusais_linolejs)
    atlikumi+=atlikusais_linolejs
    
for i, num in enumerate(linoleja_daudzumi, start=1):
    print(f'Linoleja daudzums {i}: {num}')
print(f'Kopējais linoleja daudzums ir {kopejais_linoleja_daudzums} m2')

for j, number in enumerate(izmaksas_kopejas, start=1):
    print(f'Izmaksas {j}: {number}')
print(f'Kopsumma šim pirkumam ir {kopsumma} Euro')

for a, numm in enumerate(atlikusie_linoleji, start=1):
    print(f'Atlikušais linolejs {a}: {numm}')
print(f'Kopā atliek {atlikumi} m2 linoleja')

if atlikumi<0:
    print('Nepietiek linolejs')
