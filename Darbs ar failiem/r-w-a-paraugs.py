#ar w+ izveidot failu dati2.txt
file = open('dati2.txt','w+',encoding='utf-8')

#ierakstīt failā sarakstu ar 3 pilsētām
saraksts = ['Rīga\n','Sigulda\n','Valmiera\n']
file.writelines(saraksts) #ieraksta vairākas rindiņas

#ierakstīt vienu virkni Hello, World
file.write('Hello, World')

file = open('dati2.txt','a+',encoding='utf-8')
#pievienot vārdnīcu ar valstīm un galvaspilsētām
valstis = {
    '\nLatvija': 'Rīga',
    '\nSomija': 'Helsinki',
    '\nIgaunija': 'Tallina'
}
file.writelines(str(valstis))