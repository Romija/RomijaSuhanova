import random
# akmems, sķēres papirs
gajieni = ['akmens','papirs','skeres']#saraksts
while True:
    cilveka_gajiens = input('Ievadi savu gājienu:')
    datora_gajiens = random.choice(gajieni)
    print('Cilvēks:',cilveka_gajiens,'vs Dators:',datora_gajiens)
    if cilveka_gajiens == datora_gajiens:
        print('Neizšķirts')
    elif cilveka_gajiens == 'akmens' and datora_gajiens == 'skeres':
        print('Cilvēks uzvar')
    elif cilveka_gajiens == 'skeres' and datora_gajiens == 'papirs':
        print('Cilvēks uzvar')
    elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens':
        print('Cilvēks uzvar')
    else:
        print('Dators uzvar')