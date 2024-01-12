darzeni = ['burkāni','kartupeļi','brokoļi','kāposti']
#ar sorted() izveido jaunu sakārtotu sarakstu, neaiztiekot eošo
print('Orģinālais: ',darzeni)
print('Ar sorted sakārtot: ',sorted(darzeni))

darzeni.sort() #maina saraksta struktūru

viens = [5,6,2,5,3,5]
print(sorted(viens)) #atgriež jaunu sakārtotu sarakstu, nemainot oriģinālo
print(viens)

darzeni_apgriezts = sorted(darzeni, reverse=True)#dilstošā secībā
print('Apgrieztā secība: ',darzeni_apgriezts)