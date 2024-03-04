saraksts1 = []
saraksts2 = []

ievade = int(input('Ievadi, cik elementi būs sarakstā: '))
for i in range(1, ievade+1,1):
    ievade1 = int(input('Ievadi elementus: '))
    saraksts1.append(ievade1)

ievade = int(input('Ievadi, cik elementi būs sarakstā: '))
for i in range(1, ievade+1,1):
    ievade2 = int(input('Ievadi elementus: '))
    saraksts2.append(ievade2)

if sum(saraksts1) > sum(saraksts2):
    starpiba= sum(saraksts1)-sum(saraksts2)
    print("Pirmā saraksta summa lielāka par: ",starpiba)
elif sum(saraksts1) < sum(saraksts2):
    starpiba= sum(saraksts2)-sum(saraksts1)
    print("Otrā saraksta summa lielāka par: ",starpiba)
else:
    print('Vienādi. Starpība ir 0')