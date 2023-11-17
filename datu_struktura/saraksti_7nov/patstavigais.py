'''
>izveidot 3 sarakstus: lietotajs pats norādīs,
cik elementus likt sarakstā.
>pirmā un otrā saraksta vērtības ievada lietotājs
>Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus
>Katra saraksta saturu glīti parādīt uz ekrāna.
'''

elementu_skaits1 = int(input('Ievadiet elementu skaitu 1. sarakstā: '))
saraksts1 = []
for i in range(1,elementu_skaits1+1,1):
    elements1= input('Ievadi elementu: ')
    saraksts1.append(elements1)


elementu_skaits2 = int(input('Ievadiet elementu skaitu 2. sarakstā: '))
saraksts2 = []
for j in range(1,elementu_skaits2+1,1):
    elements2= input('Ievadi elementu: ')
    saraksts2.append(elements2)


saraksts3 = saraksts1 + saraksts2


print('1.saraksts: ',saraksts1)
print('2.saraksts: ',saraksts2)
print('3.saraksts: ',saraksts3)