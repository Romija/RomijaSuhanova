skaitli = [] #tukšs saraksts
skaits = int(input('Ievadiet skaitļu skaitu (ne mazāk kā 3): ')) #ievadīt skaitu
while skaits <3: #ja ievadītais skaits ir mazāks par 3, tad jautā atkārtoti līdz ir 3 vai vairāk
    skaits = int(input('Ievadiet skaitļu skaitu (ne mazāk kā 3): '))

for i in range(1, skaits+1, 1): #šis ir, lai parāda, kurš pēc kārtas skaitlis
    skaitlis = int(input(f'Ievadi {i} skaitli: ')) #prasa ievadīt skaitli
    skaitli.append(skaitlis) #pievieno skaitli sarakstam

print(f'Saraksts ar skaitliem {skaitli}') #izdrukā sarakstu
print("Lielākais ievadītais skaitlis ir: ", max(skaitli)) #atrod un izdrukā lielāko skaitli

