'''aboli = input('Vai Jums mājās ir āboli? (j/n)')
if aboli == 'n':
    print('Šai receptei vajag ābolus. Kad nopērciet, atgriežieties un varēsiet turpināt.')
    exit()
elif aboli == 'j':
    abolu_daudzums = int(input('Cik kg mājās ir ābolu?: '))'''

print('Pirmā recepte: \n3k ābolu \n1kg cukurs \n500ml ūdens \n1gab citrons \n5ml mandeļu ekstrakts \n10g kanēlis')
print('Otrā recepte: \n3k ābolu \n1kg cukurs \n500ml ūdens \n10g kanēlis')
recepte = int(input('Kuru no receptēm vēlies taisīt? (1/2): '))
if recepte == 1:
    aboli = input('Vai Jums mājās ir āboli? (j/n)')
if aboli == 'n':
    print('Šai receptei vajag ābolus. Kad nopērciet, atgriežieties un varēsiet turpināt.')
    exit()
elif aboli == 'j':
    abolu_daudzums = int(input('Cik kg mājās ir ābolu?: '))
    if abolu_daudzums <3:
        print('Vajag vairāk ābolu')
    elif abolu_daudzums >= 3:
        cukurs = input
