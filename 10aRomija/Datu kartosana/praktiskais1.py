#ir izveidota vārdnīca, kas glabā 6 grāmatas nosaukumu kā atsēgu un lappušu skaitu kā vērtību
#ar for, sakārto vārdnīcu pēc atslēgas(alfabēta secībā)
#uz ekrāna parādīt gan atslēgu, gan vērtību
#sakārtot pēc lappušu skaita augošā un dilsošā secībā(get būs jāliek)

gramatas = {
    'Kronis': '100',
    'Poters': '120',
    'You': '234',
    'After':'486',
    'Abece': '875',
    'Mājkalpotāja': '64'
}

for atslega in sorted(gramatas):
    print((atslega,gramatas[atslega]))

print('------------------')

#sort tikai sarakstos

gramatas_augosi  = sorted(gramatas,key=gramatas.get)
gramatas_kartots = {}
for atslega in gramatas_augosi:
    
