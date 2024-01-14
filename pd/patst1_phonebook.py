kontakti = {'vards': [], 'numurs':[]} #kā vērtības(value) sākumā ielikt tukšus sarakstus
kontakti['vards'] = ['Anna','Zane','Jānis','Gustavs']  
kontakti['numurs'] = ['12547865', '45697456', '26588965','12365445'] 

#key ir name un vērtība ir tukšs saraksts, tas pats ar numuru(numurs ir key un value tukšs saraksts)
#tālāk kontaktos varēs likt iekšā
#jo atslēgas nevar dublēties, tad tiks tikai updeitota iepriekšējā vērtība

while True:
    izvelne= input("""Ko vēlaties darīt?
                   1-drukāt 
                   2-pievienot 
                   3-izdzēst
                   4-iziet \n """) #programma darbojas līdz lietotājs uzspiež 4 jeb exit
    izvelnes_atbilde = int(izvelne) 

    if izvelnes_atbilde == 1: #ja lietotājs ievada 1, tad uz ekrāna izdrukāt visus vārdus un numurus kā rādīts paraugā
      
        print('Jūs uzspiedāt taustiņu 1: jūsu kontakti uz ekrāna: ')
        #for i in range(0,4):
            #print(f"Vārds: {kontakti['vards'][i]}\nNumurs:{kontakti['numurs'][i]}")
        print(kontakti)
        print('-----------------------------------')
        
    #ja lietotājs ievada 2, tad ir iespēja pievienot jaunu vārdu un telefona numuru

    elif izvelnes_atbilde == 2:
        print('Jūs uzspiedāt taustiņu 2: pievieno jaunu kontaktu:')
        vards = input('Ievadi vārdu: ')
        numurs = input('Ievadi numuru: ')
        kontakti['vards'].append(vards)
        kontakti['numurs'].append(numurs)
        #print(f"Vārds: {kontakti['vards'][i]}\nNumurs:{kontakti['numurs'][i]}")
        print('-----------------------------------')
    elif izvelnes_atbilde == 3:
        print('Jūs uzspiedāt taustiņu 3 :izdzēst kontaktu:')
        vards = input('Ievadi vārdu: ')
        index = kontakti['vards'].index(vards)  #metode index paņem mainīgo name un atrod atbilstošo
        #remove metode nestrādās, jo izdzēsīs tikai vienu
        kontakti['vards'].pop(index) #pop prasa konkrēto indeksu 
        kontakti['numurs'].pop(index) #
    elif izvelnes_atbilde == 4:
        print('Jūs uzspiedāt taustiņu 4: Paldies, ka izmantojāt šo programmu!')
        exit()
