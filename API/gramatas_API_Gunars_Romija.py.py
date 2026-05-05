import requests
import random

#aizpildīt kodu atbilstoši prasībām‼️‼️‼️
#un salabot formatējumu, ja nepieciešams ‼️‼️‼️


#Šī adrese atgriež sarakstu ar grāmatām JSON formātā
gramatu_url = "https://pro2025.azurewebsites.net/books"

#URL adrese, no kuras iegūstam žurnālu datus.
zurnalu_url = "https://pro2025.azurewebsites.net/journals"


#4.1. uzdevums
url = f"https://pro2025.azurewebsites.net/books"
response = requests.get(url)
if response.status_code == 200:
    print('Mājaslapa atvērta👌')
else:
    print('Neizdevās Iekļūt❌')

#4.2. uzdevums
gramatas = response.json()
#pārvērtīs json par python vārdnīcu
for i in gramatas:
    nosaukums = i['name']
    gads = i['year_published']
    lpp = i['pages']
    print(f'Grāmata "{nosaukums}" ({gads}), {lpp}')
    #dati no api laukiem
    #name-grāmatas nosaukums
    #year_published-izdošanas gads
    #pages-lappušu skaits


#4.3. uzdevums
#Izveido sarakstu, kurā būs tikai grāmatu nosaukumi
nosaukumi = []
for i in gramatas:
    nosaukumi.append(i['name'])

#Ieraksti nosaukumus teksta failā.
#encoding="utf-8" vajadzīgs, lai pareizi saglabātos latviešu burti(ja buus)
with open("nosaukumi.txt", "w", encoding="utf-8") as fails:
    for nosaukums in nosaukumi:
        fails.write(nosaukums + "\n")
print("\n4.3. Grāmatu nosaukumi ierakstīti failā nosaukumi.txt")





#4.4. uzdevums: visvecaākā grāmata
    #year_published API datos ir teksts, tāpēc tāpēc jāparbeido par int
gads = 999999999999999999
nosaukums = ''
for i in gramatas:
    jaunais_gads = int(i['year_published'])
    if jaunais_gads < gads:
        gads = jaunais_gads
        nosaukums = i['name']
print("\n4.4. Visvecākā grāmata:", nosaukums)






#4.5. uzdevums:visu lappusu kopejais skaits un videjais aritmetiskais
kopejais_lappusu_skaits = 0
kopeja_cena = 0
skaits=0
for gramata in gramatas:
    kopejais_lappusu_skaits+=int(gramata['pages'])
    kopeja_cena+=int(gramata['price'])
    skaits += 1
    #pages un price API datos ir teksta veidā, tāpēc tie jāpārveido par skaitļiem
videja_cena = kopeja_cena/skaits

print("\n4.5. Kopējais lappušu skaits:", kopejais_lappusu_skaits)
print("4.5. Vidējā aritmētiskā cena:", round(videja_cena, 2))



def garakais_nosaukums(gramatas):
    garums = 0
    for i in gramatas:
        jaunais_garums = len(i['name'])
        if jaunais_garums > garums:
            garums = jaunais_garums
            return i

#4.6. uzdevums: gramata ar garako nosaukumu+autors un gads
#Izsauc iepriekš izveidoto funkciju
gramata_ar_garako_nosaukumu = garakais_nosaukums(gramatas)
#Funkcija, kas atrod un atgriež grāmatu ar garāko nosaukumu
#Parametrs "gramatas" ir saraksts ar visām grāmatām

print("\n4.6. Grāmatas ar garāko nosaukumu autors:", gramata_ar_garako_nosaukumu["author"])
print("4.6. Grāmatas ar garāko nosaukumu gads:", gramata_ar_garako_nosaukumu["year_published"])


#4.7. uzdevums
#Izveidojam jaunu datu struktūru(šajā piemērā var ņemt vienkārši sarakstu) ar visiem datiem par visām grāmatām
#Ja autoram ir tukšs teksts, tad ierakstām "Nav norādīts"
gramatu_dati = []

for i in gramatas:
    if i['author'] == '':
        i['author'] = 'Nav norādīts'
    gramatu_dati.append(i)
print("\n4.7. Izveidots saraksts ar visām grāmatām.")



#4.8.uzdevums
#izvadi visu grāmatu autorus alfabētiskā secībā (A–Z) (1 punkts), turklāt nodrošinot, ka autori neatkārtojas

    #Pārbauda, vai autors jau nav sarakstā-tas nodrošina, ka autori neatkārtojas

#Sakārtot autorus alfabētiskā secībā
print("\n4.8. Autori alfabētiskā secībā:")
autori = []
for i in gramatu_dati:
    autors = i['author']
    if autors not in autori:
        autori.append(autors)
for i in sorted(autori):
    print(i)

'''
#4.9. uzdevums
#Izveidojam vārdnīcu, kur atslēga būs autors, vērtība būs šī autora grāmatu nosaukumu saraksts

vardnica = {}
for i in gramatu_dati:
    if vardnica[i['author']] == '':
        vardnica[i['author']] = list(i['name'])
    else:
        vardnica[i['author']]= vardnica[i['author']].append(i['name'])

print(vardnica)




print(f'\n4.9. Autors, kuram ir visvairāk grāmatu ({gramatu_skaits}), - {autors_ar_visvairak_gramatam}:')



#4.10. uzdevums
#Iegūst žurnālu datus no otrās API adreses



#Nejauši izvēlas 10 žurnālus no visa žurnālu saraksta
#random.sample neatkārto vienu un to pašu elementu vairākas reizes
nejauši_zurnali = random.sample(visi_zurnali, 10)

#Izveidojam jaunu sarakstu, kur katram žurnālam glabājas tikai nosaukums un izdevējs
zurnalu_saraksts = []

#pievieno jaunu žurnālu

print("\nŽurnālu saraksts pēc jaunā žurnāla pievienošanas sākumā:")


#dzēš pēdējo žurnālu no saraksta


print("Žurnālu saraksts pēc pēdējā žurnāla dzēšanas:")
'''
