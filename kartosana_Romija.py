skaitli = [1,5,7,9,2,5]
skaitli.sort()
print('Augošā secībā: ',skaitli)

skaitli_apgriezts = sorted(skaitli, reverse=True)
print('Diltošā secībā: ',skaitli_apgriezts)

words = ['apple', 'bed', 'table', 'computer', 'food']
words.sort()
print('Alfabētiskā secībā: ',words)

vardu_garums = sorted(words,key=len)
print('Pēc vārdu garumiem: ',vardu_garums)

skaitli2 = [2, -4, 5,9,0]
absoluta_vertiba = sorted(skaitli2, key=abs)
print('Sakārtots pēc absolūtās vērtības: ',absoluta_vertiba)

vardnica = {
    'Evelīna' : '3',
    'Romija': '5',
    'Atis': '4',
    'Marks': '8'
}

vardnica_dilstosi  = sorted(vardnica,key=vardnica.get)
vardnica_kartots = {}
for atslega in vardnica_dilstosi:
    '''vardnica_kartots[key]=vardnica[key]
    print(vardnica_kartots)'''
