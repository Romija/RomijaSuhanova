#izveidot tukšo vārdnīcu
vardnica = {
    'a':1,
    'b':2
}

ievade_atsl = input('Ievadiet atslēgu: ')
ievade_vert = input('Ievadiet atslēgu: ')

#pārbauda lietotāja ievadi un rediģē vārdnīcu
if ievade_atsl in vardnica:
    vardnica[ievade_atsl] =ievade_vert
    print('Vārdnīca atjautnināta! ')

else:
    vardnica[ievade_atsl] = ievade_vert
    print('Jauns pāris tika pievienots vārdnīcai')


print('atjaunotā vārdnīca:',vardnica)