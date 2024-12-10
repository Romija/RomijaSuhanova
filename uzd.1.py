def ierakstit_faila():
    with open('fails.txt','w',encoding='utf8') as file:
        for i in range(1,7):
            vards = input(f'Ieraksti {i} vardu.')
            file.write(vards+'\n')
    print('Saglabāta')
#ierakstit_faila()

def nolasit_ar_for():
    try:
        with open('fails.txt','r',encoding='utf8') as file:
            print('Faila saturs: ')
            for i in file:
                print(i.strip())
    except FileNotFoundError:
        print('Fails nepastāv')

#nolasit_ar_for()

#izveidot sarakstu ar 3 vārdiem
# pievienot šo sarakstu failam
#paradīt konsolē cik vārdi pievienoti

def vardi_manuali():
    jauni_vardi = ['romija','katrina','alise']
    with open('fails.txt','a',encoding='utf8') as file:
            for i in jauni_vardi:
                file.write(i+'\n')
            print(f"{len(jauni_vardi)} jauni vārdi")
#vardi_manuali()

#ievadīt vārdu, ko meklē failā un informēt lietotāju vai tāds ir

def atrast_vardu():
    vards = input('Ievadi vārdu, ko meklē: ')
    try: 
        with open('fails.txt','r',encoding='utf8') as file:
            saturs = file.read()
        if vards in saturs:
            print(f'Vārds {vards} ir failā')
        else:
            print(f'Vārds {vards} nav failā.')
    except FileNotFoundError():
        print('Neeksistējošs fails.')

#atrast_vardu()

#sakārtot failā esošos datus dilstošā secībā

def sakartot_dilstosa():
    #try:
    with open('fails.txt','r',encoding='utf8') as file:
        saturs = file.read()
        with open('fails.txt','a',encoding='utf8') as file:
            sakartoti_dati = sorted(saturs)
            file.write(sakartoti_dati)
    #except FileNotFoundError():
        #print('Neeksistējošs fails')

def kartot_dilstosi():
    try:
        with open('fails.txt','r',encoding='utf8') as file:
            saturs = file.readlines()
        kartots = sorted(saturs, reverse = True)
        with open('fails.txt','w',encoding='utf8') as file:
            file.writelines(kartots)
        print('Sakārtots dilstošā secībā')
    except FileNotFoundError():
        print('Neeksistējošs fails')

kartot_dilstosi()