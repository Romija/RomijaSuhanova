import math #būs vajadzīga noapaļošanai
kopsumma = 0.00 #kopsumma, kurai laika gaitā pieskaitīs klāt pirkumu cenas

#dotā recepte uz 1kg ābolu, taču programma izrēķinās pārējo attiecīgo sastāvdaļu daudzumu pēc ievadītā ābolu daudzuma
print('Recepte uz 1kg ābolu:\n1kg ābolu, 1kg parastā vai ievārījuma cukura(ievārījuma cukurs paredzēts saldummīļiem), 1l ūdens, 1gab citrona, 10g kanēlis')

#prasa ievadīt ābolu daudzumu un, tad pārbauda, vai derīgi skaitļi ir ievadīti
abolu_daudzums = int(input('Cik veselu kg ābolu Jums ir?: '))
if abolu_daudzums<0:
    print('Cik zināms, ābelēs neaug negatīvi āboli')
    exit()
if abolu_daudzums==0:
    print('Neveiksmīga raža:(')
    exit()

#cena sastāvdaļām
cena_p_cukurs = 1.30#1kg
cena_i_cukurs = 2.60 #1kg
cena_udens = 1 #litrs ūdens
cena_citrons = 0.45
cena_kanelis = 0.60 #10g iepakojumā

#aprēķina vajadzīgo daudzumu pēc ievadītā ābolu daudzuma
p_cukurs = 1*abolu_daudzums
i_cukurs = 1*abolu_daudzums
udens = 1*abolu_daudzums
citrons = 1*abolu_daudzums
kanelis = 10*abolu_daudzums 

#informē lietotāju par to
print(f"Nepieciešamais daudzums:")
print(f"Cukurs: {p_cukurs} kg parastā cukura vai {i_cukurs}kg ievārījums cukura")
print(f"Ūdens: {udens} l")
print(f"Citrons: {citrons} gab.")
print(f"Kanēlis: {kanelis} g")

#pārliecinās cik daudz ūdens lietotājam ir
udens_daudzums = float(input('\nCik l ūdens Jums ir?(pieņem arī decimālskaitļus) '))
noapalots_udens = math.floor(udens_daudzums) #noapaļo ūdens daudzumu, lai tas atbilstu iepakojuma daudzuma iespējām
if udens_daudzums<0: #negatīvo skaitļu ievadi neatļauj
    print('Pirmā dzirdēšana par negatīvu ūdeni')
    exit()

citronu_daudzums = int(input('Cik veselu citronu Jums ir? '))
if citronu_daudzums<0: #negatīvu skaitļu ievadi neatļauj
    print('Negatīvi citroni neaug kokos')
    exit()

kanela_daudzums = int(input('Cik veselu grami kanēļa Jums ir? '))
if kanela_daudzums<0: #negatīvie skaitļi
    print('Pirmā dzirdēšana par negatīvu kanēli')
    exit()
if kanela_daudzums== 0 or kanela_daudzums>9:
    pirmais_cipars_kanelis = int(str(kanela_daudzums)[0]) #noapaļo kanēli atbilstoši tā iepakojuma iespējām
    noapalots_kanelis = int(str(pirmais_cipars_kanelis) + '0')
if 0<kanela_daudzums<10: #ja nav pat viena iepakojuma, tad cita opcija, jo uz šo nedarbojās iepriekš minētā funkcija
    noapalots_kanelis2 = kanela_daudzums 

cukura_izvele = input('Vai Jūs izmantosiet parasto vai ievārījuma cukuru?(p/i) ')
if cukura_izvele == 'p': #pārbauda vai izmantos parasto cukuru
    izvele_parastais = float(input('Cik kg parastā cukura Jums ir?(der arī decimālskaitļi) '))
    if izvele_parastais<0: #negatīvitāti pārbauda
        print('Negatīvs cukurs Latvijas apstākļos nav sastopams')
        exit()
    noapalots_parastais = math.floor(izvele_parastais) #noapaļo cukura daudzumu atbilstoši cukur iepakojuma iespējām

elif cukura_izvele == 'i': #pārbauda vai izmantos ievārījuma cukuru
    izvele_ievarijuma = float(input('Cik kg ievārījuma cukura Jums ir?(der arī decimālskaitļi) '))
    if izvele_ievarijuma<0: #pārbauda negativitāti
        print('Negatīvs cukurs Latvijas apstākļos nav sastopams')
        exit()
    noapalots_ievarijuma = math.floor(izvele_ievarijuma) #moapaļo ievārījuma cukuru atbilstoši cukura iepakojuma iespējām
else:
    print('Ievades datos kļūda')
    exit()
    
#sastāda sarasktu ar lietām, ko vajag
#ja pietiek, tad to paziņo
#ja pietrūkst, tad pasaka, cik pietrūkst un pasaka pirkuma cenu atbilstoši iepakojuma iespējām
print('\n---SARAKSTS AR VAJADZĪGAJĀM LIETĀM---\n')
if udens_daudzums <udens:
    print(f'Nepietiek ūdens. Vēl vajag {udens-udens_daudzums}l ūdens. Tas izmaksās {cena_udens*(udens-noapalots_udens)}euro')
    kopsumma += cena_udens*(udens-noapalots_udens) #kopsummai pieskaita
else:
    print('Pietiekams daudzums ūdens')

#pārbauda cukura izvēli
if cukura_izvele == 'p':
    if izvele_parastais<p_cukurs:
        pirkums_pcukurs = cena_p_cukurs*(p_cukurs-noapalots_parastais)
        print(f'Nepietiek parastais cukurs. Vēl vajag {p_cukurs-izvele_parastais}kg parastā cukura. Tas izmaksās ' "%.2f"%pirkums_pcukurs,'euro')
        kopsumma += cena_p_cukurs*(p_cukurs-noapalots_parastais) #kopsummai pieskaita
    else:
        print('Pietiekami daudz parastā cukura')

elif cukura_izvele == 'i':
    if izvele_ievarijuma<i_cukurs:
        pirkums_icukurs = cena_i_cukurs*(i_cukurs-noapalots_ievarijuma)
        print(f'Nepietiek ievārījuma cukurs. Vēl vajag {i_cukurs-izvele_ievarijuma}kg ievārījuma cukura. Tas izmaksās ' "%.2f"%pirkums_icukurs, 'euro')
        kopsumma += cena_i_cukurs*(i_cukurs-noapalots_ievarijuma) #kopsummai pieskaita
    else:
        print('Pietiekami daudz ievārījuma cukura')

if citronu_daudzums<citrons:
    print(f'Nepietiek citronu. Vēl vajag {citrons-citronu_daudzums}gab citronu. Tas izmaksās {cena_citrons*(citrons-citronu_daudzums)}euro')
    kopsumma += cena_citrons*(citrons-citronu_daudzums) #kopsummai pieskaita
else:
    print('Pietiekami daudz citronu')

#kanēlim ar sazarojumu, nosaka cenu atbilstoši tā iepakojuma iespējām
if kanela_daudzums<kanelis:
    if kanela_daudzums== 0 or kanela_daudzums>9:
        print(f'Nepietiek kanēļa. Vēl vajag {kanelis-kanela_daudzums}g kanēļa. Tas izmaksās {(cena_kanelis*(kanelis-noapalots_kanelis))/10}euro')
        kopsumma += (cena_kanelis*(kanelis-noapalots_kanelis))/10 #kopsummai pieskaita
    if  0<kanela_daudzums<10:
        pirkums_kanelis = cena_kanelis*abolu_daudzums
        print(f'Nepietiek kanēļa. Vēl vajag {kanelis-kanela_daudzums}g kanēļa. Tas izmaksās ' "%.2f"%pirkums_kanelis, 'euro')
        kopsumma += 0.6 #kopsummai pieskaita
else:
    print('Pietiekama daudzuma kanēļa')

print(f'\nKOPSUMMA: ' "%.2f"%kopsumma) #izvada kopsummu

masa = abolu_daudzums + udens+kanelis/1000+citrons*0.120   #aprēķina masu(vidēji citrona masa ir 125g)
#atbilstoši cukura tipam, pieskaita attiecīgo masu
if cukura_izvele == 'p':
    masa += p_cukurs
elif cukura_izvele == 'i':
    masa+= i_cukurs
print('\nJums kopā sanāks ' "%.2f"%masa,'litri\n') #izvada cik litrus iespējams izvārīt ar attiecīgo ābolu daudzumu

#minētā papildfunkcija
burcinas = math.ceil(masa / 0.5) #noapaļo, lai būtu burciņas veselā skaitā
print(f"{masa} litri ir {burcinas} burciņas pa 0.5 litriem.") #informē lietotāju par 0,5l burciņu skaitu


#UZLABOJUMI:
#float pie ābolu daudzuma, bet tad jāapaļo pārējais ar math.ceil