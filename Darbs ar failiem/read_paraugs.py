#r režīmā failam jābūt mapē
#r atver failu lasīšanai
#jābūt atvērtai tikai šai mapei
'''file = open('demo.txt','r',encoding='utf 8')
print(file.read()) #izdrukā faila saturu'''

'''file = open('demo.txt','r',encoding='utf 8')
print(file.readline()) #nolasīs pirmo rindiņu'''

file = open('demo.txt','r',encoding='utf 8')
print(file.read(10)) #atgriež 10 simbolus, ieskaitot atstarpes

file.close() #darba beigās aizver failu
