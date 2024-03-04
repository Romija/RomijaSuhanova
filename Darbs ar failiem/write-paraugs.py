fails = open('dati.txt','w+',encoding='utf-8') #w izveidos failu
fails.write('Mācos rakstīt failā!\n')

fails.write('Kaut kāds teikums')

fails = open('dati.txt','r',encoding='utf-8') 
#fails.seek(3)
print(fails.read()) #datus nolasa un parāda konsolē

fails = open('dati.txt','w+',encoding='utf-8')
fails.write('Ziema\n')