import statistics
skaitli = [] #skaitļu saraksts ar ko veiks darbības
n=0
skaits = int(input('Ievadi, cik skaitļus vēlies ievadīt: '))
while n<skaits:
    ievadi_skaitli=input('Ievadiet skaitli (iziet- pārtaukšana)')
    n+=1
    if ievadi_skaitli.lower()=='iziet':
        print('Programma pārtraukta pēc jūsu lūguma! ')
        break
        #pārtrauc ciklu, ja ievada tukšu rindu jeb enter
    elif not ievadi_skaitli:
        break
    skaitli.append(ievadi_skaitli)

        #atvērt failu, lai ierakstītu datus
    with open('skaitli_istie.txt','w',encoding='utf8') as file:
            #ieraksta katru savā rindā
        for line in skaitli:
            file.write(line+'\n')
    print('Dati ierakstīti jaunajā failā')

def summa(): #saskaitīšanas funkcija
    kopeja_summa = sum(skaitli)
    print(f'Kopsumma: {kopeja_summa}')

def videjais():
    aritmetiskais =statistics.mean(skaitli)




