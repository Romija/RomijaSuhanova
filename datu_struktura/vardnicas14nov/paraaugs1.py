#vienādas atslēgas nevar būt vārdnīcās
telefons = {
    'Jānis':2343455,
    'Rita':45345,
    'Anna': 324545
}

#jānim ir 2 telefona numuri
telefons.update({'Jānis': 2222222})
print('Šis ir Ritas numurs',telefons['Rita'])
print('Šis ir Jāņa numurs',telefons['Jānis'])
print('Šis ir Annas numurs',telefons['Anna'])

#izveidot vārdnīcu ar atslēgu rindu fromkeys() metodi
#vārdnīca, nenorādot ierakstu vērtības
kk = ('viens','divi','trīs')
dd = dict.fromkeys(kk)
print(dd)
val = 0 #šī vērtība visai vārdnīcai
dd = dict.fromkeys(kk,val)
print(dd)

#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Tampere','Rovaniemi'],
    'Norvēģija': ['Oslo','Bargena','Trumse'],
    'Dānija': ['Kopenhāgena','Ronne','Odense']
}
for atslega , vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))
    print('👌') #windows semikols ir, lai emoji dabūtu
