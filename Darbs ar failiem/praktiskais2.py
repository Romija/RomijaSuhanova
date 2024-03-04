import csv
'''Uzrakstīt programmu, kas strukturē datus no viena faila,
atjaunina un ieraksta jaunā failā'''

sakotnejie_dati_fails='sakotnejie_dati.csv'
jaunie_dati_fails='jaunie_dati.csv'

#mēģina atvērt sākotnējo failu un lasa datus

try:
    with open(sakotnejie_dati_fails,'r',encoding='utf8') as sakotnejie_fails:
        lasitajs = csv.DictReader(sakotnejie_fails)
        sakotnejie_dati = list(lasitajs)
        #atjaunot datus
        for persona in sakotnejie_dati:
            persona['vecums']=int(persona['vecums'])+1 #palielina +1 vecumu
            #ieraksta datus jaunā failā
    with open(jaunie_dati_fails,'w', encoding= 'utf8') as jaunie_fails:
        rakstitajs = csv.DictWriter(jaunie_fails,fieldnames=['vards','uzvards','vecums'])
        rakstitajs.writeheader()
        rakstitajs.writerows(sakotnejie_dati)
    print(f'Dati ir atjaunināti un saglabāti failā {jaunie_dati_fails}')

except FileNotFoundError:
    print(f'Kļūda: Fails{sakotnejie_dati_fails} nav atrasts')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda = {e}')
        
