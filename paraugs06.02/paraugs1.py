#ielasīt programmā faila saturu
import sys
def nolasit_failus(failins):
    try:
        with open(failins,'r',encoding='utf8')as file:
            saturs=file.read() #glabā faila saturu
            return saturs
    except FileNotFoundError as e:
        print(f'Fails {failins} nav atrasts',file=sys.stderr)

#funkcija, kas skaita simbolus failā
def saskaitit(saturs):
    return len(saturs)

#funkcija, kas izvada pirmo un pēdējo simbolu
def pirmais_un_pedejais(saturs):
    return saturs[0], saturs[-1]

def lasit_simbolus(failins, garums):
    try:
        with open(failins,'r',encoding='utf8')as file:
            saturs=file.read(int(garums))
            return saturs
    except FileNotFoundError:
        print(f'Fails {failins} nav atrasts',file=sys.stderr)
    except ValueError:
        return "'Garums' jābūt skaitlim."
    
#funkcija, kas nolasa pirmo rindiņu no faila satura
def drukat_pirmo(failins):
    try:
        with open(failins,'r',encoding='utf8')as file:
            pirma_rinda=file.readline()
            print(pirma_rinda)
    except FileNotFoundError:
        print(f'Fails {failins} nav atrasts',file=sys.stderr)

failins = input('Lūdzu, ievadiet faila nosaukumu: ')
saturs = nolasit_failus(failins)

if saturs:
    print('1) Simbolu skaits: ',saskaitit(saturs))
    print('2) Pirmais un pēdējais: ',pirmais_un_pedejais(saturs))
    
    garums = input('Lūdzu, ievadiet garumu: ')
    print('3) Simboli no sākuma līdz garumam: ',lasit_simbolus(failins, garums))

    print('\nPirmā rinda: ')
    drukat_pirmo(failins)