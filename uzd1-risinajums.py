#nolasīt csv faila saturu
#aprēķināt vidējo vērtējumu
#jāpievieno jauns lauks Vidējais, to visu saglabā jaunā csv failā
import csv

ievades_dati = 'skoleni.csv'
izvades_dati = 'skoleni_videjais.csv'

with open(ievades_dati,'r',encoding='utf8') as file: #file tgd attēlo saturu
    #nolasa csv failu un izveido vārdnīcu, atslega - kollona, vertiba - atbilstošā rinda
    reader = csv.DictReader(file)
    skoleni = list(reader) #skoleni ir python saraksts
    #katrs saraksta elements ir 1 ieraksts no csv

#rēķina vidējo un pievieno jaunu lauku
for skolens in skoleni:
    matematika=int(skolens['Matemātika'])
    anglu_valoda = int(skolens['Angļu valoda'])
    sports = int(skolens['Sports'])
    videjais = round((matematika+anglu_valoda+sports)/3,2)
    #katram sk ierakstam pievieno jauns lauks vidējais
    skolens['Vidējais']=videjais

#saglabā datus jaunā failā
with open(izvades_dati,'w',encoding='utf8',newline='') as file: #newline noņem liekas atstarpes
    field_names = skoleni[0].keys() #atgriež 1.kollonas atslēga nosaukumu
    #objekts, kas raksta csv failā
    writer = csv.DictWriter(file,field_names)
    #ieraksta pirmo rindu, kas ir nosaukums kollonai

    writer.writeheader()
    writer.writerows(skoleni) 

print(f'Jauns fails ir saglabāts kā {izvades_dati}.')
