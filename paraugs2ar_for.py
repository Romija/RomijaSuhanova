krasas = {
    'red':'#FF0000',
    'green': '#00800',
    'black': '#000000',
    'white': 'FFFFFF'
}

for atslega in sorted(krasas):
    print(atslega,krasas[atslega])

saraksts = ['viens','divi','telefonus','lukturis','galds']
saraksts_augosi = sorted(saraksts,key=len)#pēc garuma augoši
saraksts_dilstosi = sorted(saraksts,key=len,reverse=True)#pēc garuma dilstoši

print('Sakārtots saraksts augošā secībā pēc garuma: ',saraksts_augosi)
print('Sakārtots saraksts dilstošā secībā pēc garuma: ',saraksts_dilstosi)

gramata = ['Mājkalpotāja','TITĀNIKS','you','AFTER','dune']
gramata.sort()
print('Kārtots',gramata)

print(sorted(gramata, key=str.lower))#ignorē lielos burtus
