#uzd1- ierakstīt .txt failā ar input metodi, failu izveido programma

faila_nosaukums = 'uzdevums_viens.txt'


def ieraksti_faila():
    dati = input('Raksti te: ')
    with open(faila_nosaukums, 'w', encoding='utf8') as fails:
        fails.write(dati)
    print('Informācija saglabāta!')

#ieraksti_faila()

#uzd2 - nolasīt tekstu no faila, Ja nav atrasts fails - infotmāt lietotāju
def nolasit_failu():
    try:
        with open(faila_nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.read()
            print('Faila saturs: ')
            print(saturs)
    except FileNotFoundError: #atceries izmantot File no faound error
        print('Fails netika atrasts!')

nolasit_failu()
