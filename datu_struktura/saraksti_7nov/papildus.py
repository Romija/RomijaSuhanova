#piemērs sarakstam ar dažādiem datu tipiem
mixed_list = ['suns',7.25,8, True]
print(mixed_list[2]) #izdrukāsies otris indeks

#apgriezt skaitļu sarakstu
skaitli = [1,2,4,5,6,7,3,4,7,8,9,10]
apgriezts = list(reversed(skaitli))
print(apgriezts)

#filtrēt tikai pāra skaitļus
para_skaitli = [num for num in skaitli if num%2 ==0]
print(para_skaitli)

#iegūst saraksta garumu
videjais = sum(skaitli)/len(skaitli)
print(f'Vidējais skaitlis: {videjais}')

#mazākais un lielākais skaitlis jāatrod
max = max(skaitli)
print(f'Lielākais skaitlis: {max}')

min = min(skaitli)
print(f'Mazākais skaitlis: {min}')

augli = ['citrons', 'ananass', 'apelsīns','mango','bumbieri']
#atrast vārdus, kas sākas ar konkrētu burtu
varda_sakums = [vards for vards in augli if vards.startswith('a')]
print(f'Vārdi, kas sākas ar a: {varda_sakums}')
