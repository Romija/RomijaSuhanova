import requests
vards = input("Ievadi vārdu: ")

url = f"https://api.agify.io/?name={vards}&country_id=LV"
atbilde = requests.get(url)

if atbilde.status_code == 200:
    dati=atbilde.json()

    print(f"\nVārds: {dati['name']}")
    print(f"\nIespējamais vecums: {dati['age']}")
    print(f"\nSkaits: {dati['count']} cilvēki ar šo vārdu")
else:
    print("Nav datu!")