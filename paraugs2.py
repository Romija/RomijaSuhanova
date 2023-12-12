valstis = {
    'Somija':['Helsinki','Tampere','Rovaniemi','Kemijarvi','Jyvaskyle'],
    'Norvēģija': ['Oslo','Bargena','Trumse','Molde','Arendāla'],
    'Dānija': ['Kopenhāgena','Ronne','Odense','Aarhus','Esbjerga']
}

#izdrukāt vārdnīcas elementus, piekļūstot vardnīca konkrētai atslegai
for i in valstis['Dānija']:
    print(i)

for i in valstis['Norvēģija']:
    print(i)

for i in valstis['Somija']:
    print(i)


#izdrukāt pirmās 3 pilsētas no somija
print(valstis['Somija'][:3])

#iegūt pēdējās divas no norvēģijas
print(valstis['Norvēģija'][-2:])

#iegūt visas pilsētas no Somijas iznemot pedejas 3
print(valstis['Somija'][:-3])

#iegūt no otrās līdz 5pilsētai no Dānijas
print(valstis['Dānija'][1:6])
