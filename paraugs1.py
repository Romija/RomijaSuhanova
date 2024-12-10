#saglabāt datus sarakstā
'''names=[]
for i in range(3):
    names.append(input('Whats your name?: '))
#atgriež sakārtotus
for name in sorted(names):
    print(f'Hello, {name}')'''

#info no konsoles ieraksta failā
'''name = input('Whats your name?: ')
file=open('names.txt', 'a', encoding='utf8') #w izveido failu un ieraksta datus failā
#a izveido failu, bet info pievieno klāt
file.write(f'{name}\n')
file.close() #ja izmanto file=open, tad aizver ciet failu'''
#lieto context maneger-fails, nu ka nav jāaizver
'''name = input('Whats your name?: ')
with open('names.txt', 'a', encoding='utf8') as file:
    file.write(f'{name}\n')'''

#nolasīt info no faila
'''with open('names.txt',encoding='utf') as file: #r var nerakstīt jo default
    for line in file: #var line vietā jebko rakstīt
        print('Hello,',line.rstrip()) # rstrip nogriež liekās rindiņas, atsarpes
'''
#atgriezt sakārtotus datus no faila
names=[]
with open('names.txt',encoding='utf') as file:
    for line in file:
        names.append(line.rstrip())
#atgriež sakārtotus
for name in sorted(names):
    print(f'Hello, {name}')