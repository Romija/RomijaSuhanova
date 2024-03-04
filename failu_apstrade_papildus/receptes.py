'''darbu sākt ar funkciju saglabat_recepti(), 
kas ļauj ievadīt nosaukumu un kaloriju saturu. 
Saglabā šos datus failā receptes.txt
funkcija paradit_recepti() atver failu un izvada
visu recepšu nosaukumus;
fun kcija paradit_visas_receptes() parādīs receptes
un kalorijas'''
def saglabat_recepti():
    receptes = {}
    while True:
        nosaukums=input('Īevadiet receptes nosaukumu: (iziet, lai pārtrauktu)')
        if nosaukums.lower()=='iziet':
            break
        kalorijas=float(input('Ievadiet kaloriju daudzumu: '))
        receptes[nosaukums]=kalorijas

    with open('receptes.txt','w',encoding='utf8') as fails:
        for nosaukums, kalorijas in receptes.items():
            fails.write(f'{nosaukums}: {kalorijas}\n')

def paradit_visas_receptes():
    try:
        with open('receptes.txt','r',encoding='utf8') as fails:
            print('Pieejamās receptes: ')
            for rinda in fails:
                nosaukums, kalorijas=rinda.strip().split(': ')
                print(f'{nosaukums}-{kalorijas} kcal.')
    except FileNotFoundError:
        print('Nav pieejamu recpšu, lūdzu papildiniet: ')

#lai apskatītu vienu recepti
def paradi_recepti():
    try:
        with open('receptes.txt','r',encoding='utf8') as fails:
            receptes={}
            for rinda in fails:
                nosaukums,kalorijas=rinda.strip().split(': ')
                receptes[nosaukums]=float(kalorijas)
        
        print('Pieejamās receptes: ')
        for nosaukums in receptes:
            print(nosaukums)
        izvele=input('Izvēlieties recepti(varēs redzēt kalorijas) ')
        if izvele in receptes:
            print(f'{izvele} kaloriju saturs: {receptes[izvele]} kcal')

        else:
            print('Recepte nav atrasta. ')

    except FileNotFoundError:
        print('Nav pieejamu recpšu, lūdzu papildiniet: ')
    
def galvenais():
    print('Šī ir DIY recepšu programma')
    while True:
        darbiba=input('1-Saglabāt receptes, 2-redzēt visas recept, 3-sīkāka info par konkrētu, q- beigas')
        if darbiba=='1':
            saglabat_recepti()
        elif darbiba == '2':
            paradit_visas_receptes()
        elif darbiba == '3':
            paradi_recepti()
        elif darbiba.lower() == 'q':
            break
        else:
            print('Nepareiza datu ievade. Jāizvēlas darbība no saraksta')
galvenais()