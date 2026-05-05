import requests

print('\n----1.uzdevums----')
url = f"https://restcountries.com/v3.1/name/latvia"
response = requests.get(url)#atver mājaslapu
if response.status_code == 200:#pārbauda, vai mājaslapu var atvērt
    data = response.json()#iegūst datus no mājaslapas
    print(data[0]['name']['official']) #iegūst datus no json faila
else:
    print('Neizdevās Iekļūt❌')



print('\n----2.uzdevums----')
url = f"https://restcountries.com/v3.1/name/latvia"
response = requests.get(url)#atver mājaslapu
if response.status_code == 200:#pārbauda, vai mājaslapu var atvērt
    data = response.json()#iegūst datus no mājaslapas
    print(f"Valsts: {data[0]['name']['official']}") #iegūst datus no json faila
    print(f"Galvaspilsēta: {data[0]['capital'][0]}")    
    print(f"Reģions: {data[0]['region']}")
else:
    print('Neizdevās Iekļūt❌')



print('\n----3.uzdevums----')
valsts = input('Ievadi valsts nosaukumu angliski: ')
url = f"https://restcountries.com/v3.1/name/{valsts}"
response = requests.get(url)#atver mājaslapu
if response.status_code == 200:#pārbauda, vai mājaslapu var atvērt
    data = response.json()#iegūst datus no mājaslapas
    print(f"Valsts: {data[0]['name']['official']}") #iegūst datus no json faila
    print(f"Galvaspilsēta: {data[0]['capital'][0]}") 
else:
    print('Neizdevās Iekļūt❌')



print('\n----4.uzdevums----')
url = f"https://restcountries.com/v3.1/name/latvia"
response = requests.get(url)#atver mājaslapu
if response.status_code == 200:#pārbauda, vai mājaslapu var atvērt
    data = response.json()#iegūst datus no mājaslapas
    skaits = data[0]['population'] #iegūst datus no json faila
    print(f'Iedzīvotāju skaits: {skaits}')
    if skaits > 5000000:#pārbauda
        print('Liela valsts')
    else:
        print('Neliela valsts')
else:
    print('Neizdevās Iekļūt❌')



print('\n----5.uzdevums----')
valstis = ['latvia','estonia','lithuania']
for i in valstis:#iziet cauri katram saraksta elementam
    url = f"https://restcountries.com/v3.1/name/{i}"
    response = requests.get(url)#atver mājaslapu
    if response.status_code == 200:#pārbauda, vai mājaslapu var atvērt
        data = response.json()#iegūst datus no mājaslapas
        print(data[0]['name']['official'],' - ',data[0]['capital'][0]) #iegūst datus no json faila
    else:
        print('Neizdevās Iekļūt❌')

