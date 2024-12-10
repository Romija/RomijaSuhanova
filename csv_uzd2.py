#funkcija, kas izveido csv failu un ieraksta 3 rindas
import csv

def izveidot_csv():
    with open('dati.csv','w',newline='',encoding='utf8') as file:
        rakstitajs = csv.writer(file)
        rakstitajs.writerow(['ID',"Vārds", "Vecums"])
        rakstitajs.writerows([[1,'Alise',25],[2,'Jānis',28],[3,'Ance',39]])
    print('Fails ir izveidots')

#izveidot_csv()

#parāda csv faila saturu

def nolasit():
    try:
        with open('dati.csv','r',encoding='utf8') as file:
            reader = csv.reader(file)
            for i in reader:
                print(*i) #*noņem komatus
    except FileNotFoundError():
        print('Nav faila')
    
#nolasit()

#pievienot jaunu id, vardu, vecumu ar input

def pievienot():
    with open('dati.csv','a',encoding='utf8') as file:
        writer = csv.writer(file)
        id = input('ID: ')
        vards = input('Vārds: ')
        vecums = input('Vecums: ')
        writer.writerow([id,vards,vecums])
    print('Pievienots')
pievienot()

#atjaunināt ir a