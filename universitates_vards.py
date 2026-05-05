#sīkākus nosacījumus skatīt izdales lapā

import requests

#Reģioni ar valstīm (nemainīt)
regions = {
    "Baltijas valstis": ["Latvia", "Lithuania", "Estonia"],
    "Ziemeļeiropa": ["Denmark", "Finland", "Iceland", "Norway", "Sweden"],
    "Centrāleiropa": ["Poland", "Czech Republic", "Slovakia", "Austria", "Hungary"]
}
'''
url = f"http://universities.hipolabs.com/search?country={country}"
'''

#Funkcija: reģiona izvēle
def select_region():
    #parādīt reģionus, nodrošināt lietotāja izvēli ar ievades pārbaudi
    while True:
        print("Pieejamie reģioni: ")
        print("1. Baltijas valstis")
        print("2. Ziemeļeiropa")
        print("3. Centrāleiropa")

        choice = input("Ievadi reģiona numuru: ")
        if choice == "1":
            region_name = "Baltijas valstis"
            #pēc reg nosauk paņem attiecīgo valstu sarakstu no vārdnīcas
            countries = regions[region_name]
            return region_name, countries

        elif choice == "2":
            region_name = "Ziemeļeiropa"
            countries = regions[region_name]
            return region_name, countries

        elif choice == "3":
            region_name = "Centrāleiropa"
            countries = regions[region_name]
            return region_name, countries

        else:
            print("Ievades kļūda.")

select_region()

#Funkcija: universitāšu datu iegūšana 
def get_universities(countries):
    #izmantot API un apkopot universitātes no vairākām valstīm
    universities = []
    for country in countries:
        url = f"http://universities.hipolabs.com/search?country={country}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            universities.extend(data)
        else:
            print("Neizdevās iegūt datus par valsti: ", country)
    return universities

#Funkcija: universitāšu kārtošana
def sort_universities(univesities): #var kļūdīties 2x
    #piedāvāt kārtošanas iespējas (1–3), apstrādāt kļūdainu ievadi
    meginajumi = 0
    while meginajumi<3:
        print("\nIzvēlies kārtošanas veidu: ")
        print("1. Alfabētiski pēc universitātes")
        print("2. Pēc valsts nosaukuma")
        print("3. Pēc universitātes nosaukuma garuma")

        option = input("Ievadi izvēli 1-3: ")
        if option == "1":
            return sorted(univesities, key = get_name)

        elif option == "2":
            return sorted(univesities, key=get_country)

        elif option == "3":
            return sorted(univesities, key=get_name_length)
        
        else:
            print("Nepareiza izvēle")
            meginajumi+=1

    print("Pārsniegts kļūdu skaits. Noklusētā kārtošana: pēc nosaukuma.")

    #noklusēti kārtojam pē univesritātes nosaukuma
    return sorted(univesities, key = get_name)

#university['name'] paņem universitātes nosaukumu no API datiem
def get_name(university):
    return university['name']

def get_country(university):
    return university['country']

def get_name_length(university):
    return len(university['name'])

#Funkcija: universitāšu izvadīšana ---
def display_results(universities, region_name):
    #izdrukāt pirmās 20 universitātes ar prasīto informāciju
    #pēc prasītās informācijas attēlošanas parādīt kopējo universitāšu skaitu reģionā
    print(f"\nPirmās 20 universitātes reģionā '{region_name}':\n")

    for uni in universities[:20]:
        #uni ir 1 universiāte-vārdnīca ar dažādiem laukiem
        print("Valsts: ", uni["country"])
        print("Nosaukums: ", uni["name"])
        print("Mājaslapa(s):",', '.join(uni['web_pages']))

    print(f"Kopējais skaits: {len(universities)}")

region_name, countries = select_region()
universities=get_universities(countries)
kartots = sort_universities(universities)
display_results(kartots, region_name)

# Galvenā daļa
def galvena():
    #:izsaukt iepriekš definētās funkcijas pareizā secībā
    pass


