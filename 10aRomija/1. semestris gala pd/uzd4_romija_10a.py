skaitli = [] #tukš saraksts
p=0 #pāra skaitļu skaits
n=0 #nepāra skaitļu skaits
for i in range(1, 11, 1): #pieprasa ievadīt 10 skaitļus
    skaitlis = int(input('Ievadi skaitli, ko vēlies pievienot sarakstam: '))
    skaitli.append(skaitlis) #pievieno ierakstītos skaitlus tukšajā sarakstā

print(skaitli) 

for j in skaitli: #iziet cauri sarakstam ar 10 skaitļiem
    if j %2 == 0: #ja dalās ar 2, tad pāra skaitļu skaitam pieskaita 1 skaitli un tā tas atkārtojas visu laiku ejot cauri sarakstam
        p+=1
    else: #ja nedalās, tad tas ir nepāra skaitlis un pie nepāra skaitļu skaita pieskaita 1, izejot visam sarakstam cauri
        n+=1

print(f'Pāra skaitļu skaits: {p}') #izprintē pāra skaitļus
print(f'Nepāra skaitļu skaits: {n}') #izprintē nepāra skaitļus
