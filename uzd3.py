#uzd 3 - jaunā failā
#no faila skoleni.csv noteiktu, kurš skolēns ieguvis visaugstāko
#vidējo vērtējumu, parādīt skolēna vārdu un vērtējumu
import csv

with open('skoleni.csv', 'r', encoding='utf8') as file:
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
    augstakais_vid = max(videjais)
    print(augstakais_vid)

