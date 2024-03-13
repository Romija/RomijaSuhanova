#izveidot f-ju ar nosaukumu myFunction, kurai nav parametru
#šī f-ja pie izsaukšanas izdrukā Hello World

#izsaukt, ja ievadītie skaitļi (a, b) ir vienādi
#pretējā gadījumā parādīt uz ekrāna tekstu 'Nesanāca'

def myFunction():
    print('Hello, world')

a = int(input('Ievadi skaitli: '))
b = int(input('Ievadi otro skaitli: '))

if a == b:
    myFunction()
else:
    print('Nesanāca')


def info(vards, vecums, darbs):
    print('Vārds: ',vards)
    print('Vecums: ',vecums)
    print('Amats: ',darbs)
    return
info(vards='Jānis',vecums='35',darbs='pavārs')

#uzrakstīt programmā f-ju, kas saskaita visus skaitļus sarakstā
list = [1, 2, 7,9,5,7]
def summa():
    print(sum(list))
summa()
    
