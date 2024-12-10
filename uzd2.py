#ievietot manuāli failā 5 ierakstus, parādīt 3 no tiem
import csv
csv_file = 'darbinieki.csv'
darbinieki=[
    {'Vārds':'Anna','Amats':'Skursteņslauķis','Alga':-900},
    {'Vārds':'Romija','Amats':'IT','Alga':1300},
    {'Vārds':'Katrīna','Amats':'Pavāre','Alga':700},
    {'Vārds':'Pēteris','Amats':'Direktors','Alga':1100},
    {'Vārds':'Jānis','Amats':'Skolotājs','Alga':1000}
]

#def parbaudit_algu(alga):
#   return alga.isdigit() and 0<=int(alga)

#datu ierakstīšana failā
with open(csv_file,'w',encoding='utf8',newline='') as file:
    fieldnames = ['Vārds','Amats','Alga'] #kollonu nosaukumi
    writer = csv.DictWriter(file,fieldnames)
    writer.writeheader() #ierakstam kollonu virsrakstus
    writer.writerows(darbinieki)

#noolasīt failu saturu un parādīt darbiniekus ar algu virs 1000
'''with open(csv_file,'r',encoding='utf8') as file:
    reader = csv.DictReader(file)
    for rinda in reader:
        if int(rinda["Alga"])>-1000:
            print(f"Vārds:{rinda['Vārds']}, Amats:{rinda['Amats']}, Alga:{rinda['Alga']}")'''

'''with open(csv_file,'r',encoding='utf8') as file:
    reader = csv.DictReader(file)
    for rinda in reader:
        if int(rinda["Alga"])>0:
            print(f"Vārds:{rinda['Vārds']}, Amats:{rinda['Amats']}, Alga:{rinda['Alga']}")
        elif int(rinda["Alga"])<0:
            print('Alga nav derīga')'''

with open(csv_file,'r',encoding='utf8') as file:
    try:
        reader = csv.DictReader(file)
        for rinda in reader:
            if int(rinda["Alga"])>0:
                print(f"Vārds:{rinda['Vārds']}, Amats:{rinda['Amats']}, Alga:{rinda['Alga']}")
            elif int(rinda["Alga"])<0:
                print('Alga nav derīga')
    except FileNotFoundError:
        print('Fails nepastāv')

#pārbauda vai alga kā derīgs skaitlis
#ja nav tad izdrukā brīdinājumu
#ja fails darbinieki.csv neeksiste, tad izdrukā kļūdas paziņojumu







#uzd 3 - jaunā failā
#no faila skoleni.csv noteiktu, kurš skolņs ieguvis visaugstāko
#vidējo vērtējumu, parādīt skolēna vārdu un vērtējumu